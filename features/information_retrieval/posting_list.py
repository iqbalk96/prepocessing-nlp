class PostingList:
    def build(
        self,
        tokenized_documents: dict[str, list[str]],
    ) -> dict[str, list[str]]:
        """
        Membuat posting list.

        Setiap term memiliki daftar ID dokumen
        yang mengandung term tersebut.
        """

        posting_list: dict[str, list[str]] = {}

        for document_id, tokens in tokenized_documents.items():
            unique_terms = set(tokens)

            for term in unique_terms:
                if term not in posting_list:
                    posting_list[term] = []

                posting_list[term].append(document_id)

        return {
            term: sorted(document_ids) for term, document_ids in posting_list.items()
        }
