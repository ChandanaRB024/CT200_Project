from fastapi import APIRouter

from services.document_service import (
    import_document,
    cleanup_duplicates
)

router = APIRouter()


@router.post("/import/v1")
def import_v1():

    return import_document(
        "data/ct200_manual.md",
        "CT200 Manual",
        1
    )


@router.post("/import/v2")
def import_v2():

    return import_document(
        "data/ct200_manual_v2.md",
        "CT200 Manual",
        2
    )


@router.post("/cleanup")
def cleanup():

    return cleanup_duplicates()