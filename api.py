from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from nlp.preprocessing import NLPProcessor
from pypdf import PdfReader
from io import BytesIO


app = FastAPI(
    title="Basic NLP API",
    description="API untuk preprocessing teks menggunakan NLP",
    version="1.0.0",
)


# ==========================================
# CORS
# ==========================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


processor = NLPProcessor()


# ==========================================
# Health Check
# ==========================================


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "NLP API is running",
    }


# ==========================================
# PROCESS TEXT
# ==========================================


@app.post("/api/nlp/process-text")
def process_text(text: str):
    if not text.strip():
        raise HTTPException(
            status_code=400,
            detail="Text tidak boleh kosong.",
        )

    return processor.process(text)


# ==========================================
# PROCESS PDF
# ==========================================


@app.post("/api/nlp/process-pdf")
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

    result = processor.process(text)

    return result
