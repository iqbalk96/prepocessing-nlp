from pydantic import BaseModel, Field


class DocumentInput(BaseModel):
    id: str = Field(
        min_length=1,
        description="ID unik dokumen",
    )

    title: str = Field(
        min_length=1,
        description="Judul dokumen",
    )

    content: str = Field(
        min_length=1,
        description="Isi dokumen",
    )


class BuildMatrixRequest(BaseModel):
    documents: list[DocumentInput]


class BuildTFIDFRequest(BaseModel):
    documents: list[DocumentInput]

    terms: list[str] = Field(
        min_length=5,
        max_length=5,
        description="Tepat 5 kata yang akan dihitung TF-IDF",
    )


class BuildPostingListRequest(BaseModel):
    documents: list[DocumentInput]


class BuildInvertedIndexRequest(BaseModel):
    documents: list[DocumentInput]
