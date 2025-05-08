# app.py
import os
from dotenv import load_dotenv
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

load_dotenv()

API_KEY = os.getenv("NVIDIA_API_KEY")

llm = ChatNVIDIA(
    model="meta/llama-3.3-70b-instruct",
    api_key=API_KEY,
    temperature=0.2,
    top_p=0.7,
    max_tokens=1024,
)

def get_vectorstore(docs, pdf_name):
    if not docs:
        raise ValueError("No content found in the PDF after splitting. Cannot build vectorstore.")

    vector_path = f"data/{pdf_name}_vectorstore"

    if os.path.exists(vector_path):
        return FAISS.load_local(vector_path, HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"))

    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(docs, embedding_model)
    vectorstore.save_local(vector_path)
    return vectorstore

def get_qa_chain(vectorstore):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain, retriever
