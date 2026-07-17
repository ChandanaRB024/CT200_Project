from fastapi import APIRouter

from services.generation_service import compare_document_versions

router = APIRouter()


@router.get("/compare")
def compare_versions():

    return compare_document_versions()