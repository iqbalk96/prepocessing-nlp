from fastapi import APIRouter

from .document import Document
from .schemas import (
    BuildInvertedIndexRequest,
    BuildMatrixRequest,
    BuildPostingListRequest,
    BuildTFIDFRequest,
)

from .service import IRService

router = APIRouter()

service = IRService()


@router.post("/matrix")
def build_matrix(request: BuildMatrixRequest):

    documents = [
        Document(
            id=document.id,
            title=document.title,
            content=document.content,
        )
        for document in request.documents
    ]

    return service.build_matrix(documents)


@router.post("/tfidf")
def build_tfidf(request: BuildTFIDFRequest):
    documents = [
        Document(
            id=document.id,
            title=document.title,
            content=document.content,
        )
        for document in request.documents
    ]

    return service.build_tfidf(
        documents,
        request.terms,
    )


@router.post("/posting-list")
def build_posting_list(
    request: BuildPostingListRequest,
):
    documents = [
        Document(
            id=document.id,
            title=document.title,
            content=document.content,
        )
        for document in request.documents
    ]

    return service.build_posting_list(documents)

@router.post("/inverted-index")
def build_inverted_index(
    request: BuildInvertedIndexRequest,
):
    documents = [
        Document(
            id=document.id,
            title=document.title,
            content=document.content,
        )
        for document in request.documents
    ]

    return service.build_inverted_index(documents)