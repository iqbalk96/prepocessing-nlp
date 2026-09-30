from io import BytesIO

from fastapi import APIRouter, File, HTTPException, UploadFile
from pydantic import BaseModel
from pypdf import PdfReader

from .preprocessing import NLPProcessor


router = APIRouter()

processor = NLPProcessor()


class ProcessTextRequest(BaseModel):
    text: str


@router.post("/process-text")
def process_text(request: ProcessTextRequest):
    text = request.text

    if not text.strip():
        raise HTTPException(
            status_code=400,
            detail="Text tidak boleh kosong.",
        )

    return processor.process(text)


@router.post("/process-pdf")
async def process_pdf(file: UploadFile = File(...)):

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="File harus berupa PDF.",
        )

    content = await file.read()

    reader = PdfReader(BytesIO(content))

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    text = text.strip()

    if not text:
        raise HTTPException(
            status_code=400,
            detail="Tidak dapat mengekstrak text dari PDF.",
        )

    return processor.process(text)