from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ai_core.gemini_generator import generate_legal_document


router = APIRouter()


class DocumentRequest(BaseModel):
    document_type: str
    parties: str
    terms: str
    dates: str


@router.post("/generate")
def generate_document(request: DocumentRequest):
    try:
        document = generate_legal_document(
            request.document_type,
            request.parties,
            request.terms,
            request.dates
        )

        return {
            "document_type": request.document_type,
            "document": document
        }
    except Exception as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc)
        ) from exc