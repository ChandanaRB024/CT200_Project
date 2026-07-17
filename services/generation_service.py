from database.database import SessionLocal
from models.document import Document
from models.node import Node

from utils.diff_utils import compare_versions


def compare_document_versions():

    db = SessionLocal()

    version1 = (
        db.query(Document)
        .filter(Document.version == 1)
        .first()
    )

    version2 = (
        db.query(Document)
        .filter(Document.version == 2)
        .first()
    )

    if not version1 or not version2:

        db.close()

        return {
            "message": "Both versions are required."
        }

    version1_nodes = (
        db.query(Node)
        .filter(Node.document_id == version1.id)
        .all()
    )

    version2_nodes = (
        db.query(Node)
        .filter(Node.document_id == version2.id)
        .all()
    )

    result = compare_versions(
        version1_nodes,
        version2_nodes
    )

    db.close()

    return result