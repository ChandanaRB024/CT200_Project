from fastapi import APIRouter, HTTPException

from services.selection_service import generate_from_node

router = APIRouter(
    prefix="/generate",
    tags=["Test Case Generation"]
)


@router.get("/{node_id}")
def generate_test_cases(node_id: int):
    """
    Generate test cases for a selected document node.
    If test cases already exist in the database,
    they are returned instead of calling the LLM again.
    """

    result = generate_from_node(node_id)

    if result.get("message") == "Node not found.":
        raise HTTPException(status_code=404, detail="Node not found.")

    return result