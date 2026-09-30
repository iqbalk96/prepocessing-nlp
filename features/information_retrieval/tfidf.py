import math
from collections import Counter


class TFIDFCalculator:
    def calculate_tf(
        self,
        tokens: list[str],
        terms: list[str],
    ) -> dict[str, float]:
        """
        Menghitung Term Frequency (TF).

        TF = jumlah kemunculan term dalam dokumen
             / jumlah seluruh token dalam dokumen
        """

        counter = Counter(tokens)
        total_tokens = len(tokens)

        if total_tokens == 0:
            return {term: 0.0 for term in terms}

        return {term: counter.get(term, 0) / total_tokens for term in terms}

    def calculate_df(
        self,
        tokenized_documents: dict[str, list[str]],
        terms: list[str],
    ) -> dict[str, int]:
        """
        Menghitung Document Frequency (DF).

        DF = jumlah dokumen yang mengandung term.
        """

        return {
            term: sum(1 for tokens in tokenized_documents.values() if term in tokens)
            for term in terms
        }

    def calculate_idf(
        self,
        total_documents: int,
        df: dict[str, int],
    ) -> dict[str, float]:
        """
        Menghitung Inverse Document Frequency (IDF).

        IDF = log(N / DF)
        """

        return {
            term: (
                math.log(total_documents / document_frequency)
                if document_frequency > 0
                else 0.0
            )
            for term, document_frequency in df.items()
        }

    def calculate(
        self,
        tokenized_documents: dict[str, list[str]],
        terms: list[str],
    ) -> dict:
        """
        Menghitung TF, DF, IDF, dan TF-IDF.
        """

        total_documents = len(tokenized_documents)

        df = self.calculate_df(
            tokenized_documents,
            terms,
        )

        idf = self.calculate_idf(
            total_documents,
            df,
        )

        tf = {}

        tfidf = {}

        for document_id, tokens in tokenized_documents.items():
            document_tf = self.calculate_tf(
                tokens,
                terms,
            )

            tf[document_id] = document_tf

            tfidf[document_id] = {term: document_tf[term] * idf[term] for term in terms}

        return {
            "terms": terms,
            "total_documents": total_documents,
            "tf": tf,
            "df": df,
            "idf": idf,
            "tfidf": tfidf,
        }
