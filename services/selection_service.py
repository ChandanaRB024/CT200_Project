from database.database import SessionLocal
from models.node import Node

from llm.llm_service import generate_test_cases


def generate_from_node(node_id):

    db = SessionLocal()

    node = (
        db.query(Node)
        .filter(Node.id == node_id)
        .first()
    )

    if not node:
        db.close()
        return {
            "message": "Node not found."
        }

    text = ""

    if node.heading:
        text += node.heading + "\n\n"

    if node.body:
        text += node.body

    result = generate_test_cases(text)

    db.close()

    return {
        "node_id": node.id,
        "heading": node.heading,
        "test_cases": result
    }