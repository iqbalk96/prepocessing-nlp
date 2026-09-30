import features.nltk as nltk


def setup():
    nltk.download("punkt")
    nltk.download("punkt_tab")
    nltk.download("stopwords")
    nltk.download("wordnet")


if __name__ == "__main__":
    setup()
