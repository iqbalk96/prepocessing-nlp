from .preprocessing import NLPProcessor
from .pdf import extract_text_from_pdf


def print_result(result: dict):
    print("\n" + "=" * 60)
    print("BASIC NLP PREPROCESSING")
    print("=" * 60)

    print("\n[Original Text]")
    print(result["original_text"])

    print("\n[1. Case Folding]")
    print(result["case_folding"])

    print("\n[2. Cleaning]")
    print(result["cleaning"])

    print("\n[3. Tokenization]")
    print(result["tokenization"])

    print("\n[4. Stopword Removal]")
    print(result["stopword_removal"])

    print("\n[5. Stemming]")
    print(result["stemming"])

    print("\n[6. Lemmatization]")
    print(result["lemmatization"])

    print("\n[7. Normalization]")
    print(result["normalization"])

    print("\n" + "=" * 60)


def run():
    processor = NLPProcessor()

    print("=" * 60)
    print("BASIC NLP PROCESSOR")
    print("=" * 60)

    print("\nPilih input:")
    print("1. Text")
    print("2. PDF")

    choice = input("\nPilihan [1/2]: ")

    if choice == "1":
        text = input("\nMasukkan text:\n")

    elif choice == "2":
        file_path = input("\nMasukkan path PDF:\n")

        text = extract_text_from_pdf(file_path)

    else:
        print("Pilihan tidak valid.")
        return

    if not text.strip():
        print("Text kosong.")
        return

    result = processor.process(text)

    print_result(result)
