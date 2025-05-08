# # utils.py
# import os
# import pytesseract
# from langdetect import detect
# from langchain_community.document_loaders import UnstructuredPDFLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter

# # Optional: Windows users, set Tesseract path
# if os.name == 'nt':
#     pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# def detect_language(text):
#     try:
#         return detect(text)
#     except:
#         return "unknown"

# def load_and_split_pdf(path):
#     # loader = UnstructuredPDFLoader(path, strategy="hi_res")  # OCR + layout awareness
#     loader = UnstructuredPDFLoader(path, strategy="fast")
#     documents = loader.load()

#     if not documents:
#         raise ValueError("No pages could be read from PDF.")

#     all_text = " ".join([doc.page_content for doc in documents])
#     language = detect_language(all_text)

#     splitter = RecursiveCharacterTextSplitter(
#         separators=["\n\n", "\n", ".", " "],
#         chunk_size=500,
#         chunk_overlap=50
#     )
#     chunks = splitter.split_documents(documents)

#     if not chunks:
#         raise ValueError("Text found, but failed to split into chunks.")

#     return chunks, language

# utils.py
from langdetect import detect
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def detect_language(text):
    try:
        return detect(text)
    except:
        return "unknown"

def load_and_split_pdf(path):
    loader = PyPDFLoader(path)
    documents = loader.load()

    if not documents:
        raise ValueError("No pages could be read from PDF.")

    all_text = " ".join([doc.page_content for doc in documents])
    language = detect_language(all_text)

    splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ".", " "],
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(documents)

    if not chunks:
        raise ValueError("Text found, but failed to split into chunks.")

    return chunks, language

