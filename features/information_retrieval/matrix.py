from collections import Counter


class TermDocumentMatrix:
    def build(
        self,
        tokenized_documents: dict[str, list[str]],
        vocabulary: list[str],
    ) -> dict:

        document_ids = list(tokenized_documents.keys())

        matrix = []

        for document_id in document_ids:
            counter = Counter(tokenized_documents[document_id])

            row = [counter.get(term, 0) for term in vocabulary]

            matrix.append(row)

        return {
            "documents": document_ids,
            "terms": vocabulary,
            "matrix": matrix,
        }
