from .document import Document
from .matrix import TermDocumentMatrix
from .posting_list import PostingList
from .inverted_index import InvertedIndex
from .preprocessing import IRPreprocessor
from .tfidf import TFIDFCalculator
from .vocabulary import Vocabulary


class IRService:
    def __init__(self):
        self.preprocessor = IRPreprocessor()
        self.vocabulary_builder = Vocabulary()
        self.matrix_builder = TermDocumentMatrix()
        self.tfidf_calculator = TFIDFCalculator()
        self.posting_list_builder = PostingList()
        self.inverted_index_builder = InvertedIndex()

    def build_matrix(
        self,
        documents: list[Document],
    ) -> dict:
        tokenized_documents = {
            document.id: self.preprocessor.process(document.content)
            for document in documents
        }

        vocabulary = self.vocabulary_builder.build(tokenized_documents)

        matrix = self.matrix_builder.build(
            tokenized_documents,
            vocabulary,
        )

        return {
            "documents": [
                {
                    "id": document.id,
                    "title": document.title,
                }
                for document in documents
            ],
            "tokenized_documents": tokenized_documents,
            "vocabulary": vocabulary,
            "matrix": matrix["matrix"],
        }

    def build_tfidf(
        self,
        documents: list[Document],
        terms: list[str],
    ) -> dict:
        tokenized_documents = {
            document.id: self.preprocessor.process(document.content)
            for document in documents
        }

        normalized_terms = [term.strip().lower() for term in terms]

        result = self.tfidf_calculator.calculate(
            tokenized_documents,
            normalized_terms,
        )

        return {
            "documents": [
                {
                    "id": document.id,
                    "title": document.title,
                }
                for document in documents
            ],
            "tokenized_documents": tokenized_documents,
            **result,
        }

    def build_posting_list(
        self,
        documents: list[Document],
    ) -> dict:
        tokenized_documents = {
            document.id: self.preprocessor.process(document.content)
            for document in documents
        }

        posting_list = self.posting_list_builder.build(tokenized_documents)

        return {
            "documents": [
                {
                    "id": document.id,
                    "title": document.title,
                }
                for document in documents
            ],
            "tokenized_documents": tokenized_documents,
            "posting_list": posting_list,
        }

    def build_inverted_index(
        self,
        documents: list[Document],
    ) -> dict:
        tokenized_documents = {
            document.id: self.preprocessor.process(document.content)
            for document in documents
        }

        inverted_index = self.inverted_index_builder.build(tokenized_documents)

        return {
            "documents": [
                {
                    "id": document.id,
                    "title": document.title,
                }
                for document in documents
            ],
            "tokenized_documents": tokenized_documents,
            "inverted_index": inverted_index,
        }
