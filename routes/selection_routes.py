from fastapi import APIRouter

from services.selection_service import generate_from_node

router = APIRouter()


@router.get("/generate/{node_id}")
def generate(node_id: int):

    return generate_from_node(node_id)