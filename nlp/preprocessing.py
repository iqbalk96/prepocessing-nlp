import re

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory


class NLPProcessor:
    def __init__(self):
        self.stop_words = set(stopwords.words("indonesian"))

        factory = StemmerFactory()
        self.stemmer = factory.create_stemmer()

        self.lemmatizer = WordNetLemmatizer()

        self.normalization_dict = {
            "gk": "tidak",
            "ga": "tidak",
            "nggak": "tidak",
            "gak": "tidak",
            "tdk": "tidak",
        }

    def process(self, text: str) -> dict:
        # 1. Case Folding
        case_folding = text.lower()

        # 2. Cleaning
        cleaning = re.sub(
            r"[^a-zA-Z\s]",
            "",
            case_folding,
        )

        # 3. Tokenization
        tokens = word_tokenize(cleaning)

        # 4. Stopword Removal
        tokens_no_stopword = [
            word
            for word in tokens
            if word not in self.stop_words
        ]

        # 5. Stemming
        stemmed = [
            self.stemmer.stem(word)
            for word in tokens_no_stopword
        ]

        # 6. Lemmatization
        lemmatized = [
            self.lemmatizer.lemmatize(word)
            for word in tokens_no_stopword
        ]

        # 7. Normalization
        normalized = [
            self.normalization_dict.get(word, word)
            for word in tokens_no_stopword
        ]

        # 8. Remove Duplicate
        unique_words = list(dict.fromkeys(normalized))

        return {
            "original_text": text,
            "case_folding": case_folding,
            "cleaning": cleaning,
            "tokenization": tokens,
            "stopword_removal": tokens_no_stopword,
            "stemming": stemmed,
            "lemmatization": lemmatized,
            "normalization": normalized,
            "unique_words": unique_words,
        }