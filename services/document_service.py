from database.database import SessionLocal
from models.document import Document
from models.node import Node

from parser.markdown_parser import parse_markdown


def import_document(file_path, document_name, version):

    db = SessionLocal()

    existing_document = (
        db.query(Document)
        .filter(
            Document.name == document_name,
            Document.version == version
        )
        .first()
    )

    if existing_document:
        db.close()
        return {
            "message": f"Version {version} already exists."
        }

    document = Document(
        name=document_name,
        version=version
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    nodes = parse_markdown(file_path)

    inserted_nodes = {}

    for node in nodes:

        parent_id = None

        if node["parent"] is not None:
            parent = inserted_nodes.get(node["parent"])

            if parent:
                parent_id = parent.id

        new_node = Node(
            heading=node["heading"],
            body=node["body"],
            level=node["level"],
            content_hash=node["content_hash"],
            parent_id=parent_id,
            document_id=document.id
        )

        db.add(new_node)
        db.commit()
        db.refresh(new_node)

        inserted_nodes[node["heading"]] = new_node

    db.close()

    return {
        "message": "Document Imported Successfully"
    }


def cleanup_duplicates():

    db = SessionLocal()

    documents = db.query(Document).order_by(Document.id).all()

    seen = {}

    for document in documents:

        key = (document.name, document.version)

        if key not in seen:
            seen[key] = document
        else:

            db.query(Node).filter(
                Node.document_id == document.id
            ).delete()

            db.delete(document)

    db.commit()

    db.close()

    return {
        "message": "Duplicate documents removed successfully."
    }