from collections import Counter


class InvertedIndex:
    def build(
        self,
        tokenized_documents: dict[str, list[str]],
    ) -> dict[str, dict[str, int]]:
        """
        Membuat inverted index.

        Struktur:
        {
            "term": {
                "document_id": frequency
            }
        }
        """

        index: dict[str, dict[str, int]] = {}

        for document_id, tokens in tokenized_documents.items():
            term_frequency = Counter(tokens)

            for term, frequency in term_frequency.items():
                if term not in index:
                    index[term] = {}

                index[term][document_id] = frequency

        return {
            term: dict(sorted(document_frequency.items()))
            for term, document_frequency in sorted(index.items())
        }
