class Vocabulary:
    def build(
        self,
        tokenized_documents: dict[str, list[str]],
    ) -> list[str]:

        terms = set()

        for tokens in tokenized_documents.values():
            terms.update(tokens)

        return sorted(terms)
