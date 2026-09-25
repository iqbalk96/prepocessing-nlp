# Basic NLP API

Simple Natural Language Processing (NLP) preprocessing API built with
Python and FastAPI.

Project ini dibuat untuk mempelajari dan mengimplementasikan proses dasar
NLP pada teks Bahasa Indonesia, baik dari input text maupun dokumen PDF.

## Features

- Text preprocessing
- PDF text extraction
- Case Folding
- Cleaning
- Tokenization
- Stopword Removal
- Stemming
- Lemmatization
- Normalization
- Duplicate Removal
- REST API
- Swagger API Documentation
- CORS support

## Tech Stack

- Python 3.14+
- FastAPI
- Uvicorn
- NLTK
- Sastrawi
- pypdf

## Project Structure

```text
basic-nlp/
├── nlp/
│   ├── __init__.py
│   ├── preprocessing.py
│   └── pdf.py
│
├── main.py
├── api.py
├── setup_nltk.py
├── requirements.txt
├── .gitignore
└── README.md