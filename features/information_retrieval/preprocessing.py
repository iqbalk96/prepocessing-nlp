import re

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


class IRPreprocessor:
    def __init__(self):
        self.stop_words = set(stopwords.words("indonesian"))

    def process(self, text: str) -> list[str]:
        text = text.lower()

        text = re.sub(
            r"[^a-zA-Z\s]",
            " ",
            text,
        )

        tokens = word_tokenize(text)

        tokens = [token for token in tokens if token not in self.stop_words]

        return tokens
