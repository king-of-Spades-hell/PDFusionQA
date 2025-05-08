# # finalapp.py
# import os
# import streamlit as st
# from utils import load_and_split_pdf
# from app import get_vectorstore, get_qa_chain
# import torch

# # Prevent Streamlit from scanning problematic torch classes
# import types
# torch.classes.__path__ = types.SimpleNamespace(_path=[])
# st.set_page_config(page_title="PDF Q&A with NVIDIA", layout="wide")
# st.title("📄 Ask Questions from Your PDF (NVIDIA LLM + LangChain + OCR)")

# uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

# if uploaded_file:
#     pdf_path = os.path.join("data", uploaded_file.name)
#     with open(pdf_path, "wb") as f:
#         f.write(uploaded_file.getbuffer())
#     st.success("✅ PDF uploaded successfully!")

#     if "vectorstore" not in st.session_state:
#         with st.spinner("🔍 Processing PDF, running OCR and generating embeddings..."):
#             try:
#                 docs, language = load_and_split_pdf(pdf_path)
#                 st.session_state.vectorstore = get_vectorstore(docs, uploaded_file.name)
#                 st.session_state.qa_chain, st.session_state.retriever = get_qa_chain(st.session_state.vectorstore)
#                 st.write(f"📘 Language detected: **{language.upper()}**")
#                 st.success(f"✅ Total chunks: {len(docs)}")
#             except Exception as e:
#                 st.error(f"❌ Error: {str(e)}")

#     query = st.text_input("Ask a question based on the PDF:")
#     if query and "qa_chain" in st.session_state:
#         with st.spinner("🧠 Generating response..."):
#             response = st.session_state.qa_chain.run(query)
#             st.markdown(f"**Answer:**\n\n{response}")


#         with st.expander("📄 Similar document snippets used"):
#             docs = st.session_state.retriever.get_relevant_documents(query)
#             for i, doc in enumerate(docs):
#                 st.markdown(f"**Snippet {i+1} (Page {doc.metadata.get('page', 'N/A')}):**")
#                 st.write(doc.page_content[:500])


# finalapp.py
import os
import streamlit as st
from utils import load_and_split_pdf
from app import get_vectorstore, get_qa_chain
import torch

import types
torch.classes.__path__ = types.SimpleNamespace(_path=[])

st.set_page_config(page_title="PDF Q&A with NVIDIA", layout="wide")
st.title("📄 Ask Questions from Your PDF (NVIDIA LLM + LangChain)")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file:
    pdf_path = os.path.join("data", uploaded_file.name)
    os.makedirs("data", exist_ok=True)
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("✅ PDF uploaded successfully!")

    if "vectorstore" not in st.session_state:
        with st.spinner("🔍 Processing PDF and generating embeddings..."):
            try:
                docs, language = load_and_split_pdf(pdf_path)
                st.session_state.vectorstore = get_vectorstore(docs, uploaded_file.name)
                st.session_state.qa_chain, st.session_state.retriever = get_qa_chain(st.session_state.vectorstore)
                st.write(f"📘 Language detected: **{language.upper()}**")
                st.success(f"✅ Total chunks: {len(docs)}")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

    query = st.text_input("Ask a question based on the PDF:")
    if query and "qa_chain" in st.session_state:
        with st.spinner("🧠 Generating response..."):
            response = st.session_state.qa_chain.run(query)
            st.markdown(f"**Answer:**\n\n{response}")

        with st.expander("📄 Similar document snippets used"):
            docs = st.session_state.retriever.get_relevant_documents(query)
            for i, doc in enumerate(docs):
                st.markdown(f"**Snippet {i+1} (Page {doc.metadata.get('page', 'N/A')}):**")
                st.write(doc.page_content[:500])
