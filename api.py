from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from features.nltk.router import router as nltk_router
from features.information_retrieval.router import (
    router as ir_router,
)


app = FastAPI(
    title="NLP & Information Retrieval API",
    description="API untuk NLP dan Information Retrieval",
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    nltk_router,
    prefix="/api/nltk",
    tags=["NLTK"],
)

app.include_router(
    ir_router,
    prefix="/api/ir",
    tags=["Information Retrieval"],
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "API is running",
    }