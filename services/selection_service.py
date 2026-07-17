from database.database import SessionLocal

from models.node import Node
from models.test_case import TestCase

from llm.llm_service import generate_test_cases


def generate_from_node(node_id):

    db = SessionLocal()

    try:

        node = (
            db.query(Node)
            .filter(Node.id == node_id)
            .first()
        )

        if not node:
            return {
                "message": "Node not found."
            }

        # Check if test cases already exist
        existing = (
            db.query(TestCase)
            .filter(TestCase.node_id == node_id)
            .first()
        )

        if existing:

            return {
                "node_id": node.id,
                "heading": node.heading,
                "test_cases": existing.content,
                "source": "database"
            }

        text = ""

        if node.heading:
            text += node.heading + "\n\n"

        if node.body:
            text += node.body

        # Generate from Groq
        result = generate_test_cases(text)

        # Save to DB
        new_test_case = TestCase(
            node_id=node.id,
            content=result
        )

        db.add(new_test_case)
        db.commit()

        return {
            "node_id": node.id,
            "heading": node.heading,
            "test_cases": result,
            "source": "groq"
        }

    finally:
        db.close()