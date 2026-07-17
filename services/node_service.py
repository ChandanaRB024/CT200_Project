from database.database import SessionLocal
from models.node import Node


def get_document_nodes(document_id):

    db = SessionLocal()

    nodes = (
        db.query(Node)
        .filter(Node.document_id == document_id)
        .all()
    )

    result = []

    for node in nodes:
        result.append({
            "id": node.id,
            "heading": node.heading,
            "body": node.body,
            "level": node.level,
            "parent_id": node.parent_id,
            "document_id": node.document_id
        })

    db.close()

    return result
