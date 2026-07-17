from fastapi import APIRouter

from services.node_service import get_document_nodes

router = APIRouter()


@router.get("/nodes/{document_id}")
def get_nodes(document_id: int):

    return get_document_nodes(document_id)