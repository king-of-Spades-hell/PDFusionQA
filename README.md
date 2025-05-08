# 🚀 PDFusionQA — Chat with Your PDF using NVIDIA LLMs + LangChain

Unlock the knowledge hidden in your PDF documents with **PDFusionQA** — an intelligent and interactive PDF Question Answering system powered by **NVIDIA's LLaMA-3.3-70B-Instruct**, **LangChain**, and **FAISS**. Whether it’s research papers, business docs, or manuals — just upload, ask, and get answers instantly. 🔥

---

## 🔥 Features

- 🤖 **NVIDIA LLaMA-3.3-70B-Instruct** for accurate and context-aware answers  
- 📄 Upload any PDF and ask natural language questions  
- 🧠 Embedding-based search using **HuggingFace MiniLM**  
- ⚡ Vector indexing with **FAISS** for lightning-fast retrieval  
- 🌐 Language detection and smart chunking for precision  
- 💻 Sleek and responsive UI built with **Streamlit**  

---

## 🛠 Tech Stack

- Python  
- Streamlit  
- LangChain  
- FAISS  
- HuggingFace Transformers  
- NVIDIA AI Endpoints  
- PyTorch  
- PDF parsing (`PyPDF2`, `unstructured`, `pytesseract`, `pdf2image`)  

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/PDFusionQA.git
cd PDFusionQA
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Add NVIDIA API Key

Create a `.env` file in the root directory:

```env
NVIDIA_API_KEY=your_nvidia_api_key_here
```

### 4. Run the App

```bash
streamlit run finalapp.py
```

---

## 💡 How It Works

- **PDF Upload**: Upload any PDF document.
- **Text Extraction & Language Detection**: Extracts all text and detects the document language.
- **Chunking & Embedding**: Chunks the content and embeds each chunk using HuggingFace’s MiniLM.
- **FAISS Vector Store**: Chunks are stored in a FAISS index locally for fast semantic search.
- **NVIDIA LLM QA**: Top-k relevant chunks are passed to LLaMA-3.3-70B for answering your question.

---

## 📁 Project Structure

```bash
.
├── app.py              # Core logic (vectorstore + QA chain)
├── finalapp.py         # Streamlit frontend
├── utils.py            # PDF loading, splitting, language detection
├── data/               # Uploaded PDFs and vectorstore
├── .env                # NVIDIA API key
├── requirements.txt    # Project dependencies
```

---

## 📸 Demo Questions

- "What is the main idea on page 5?"
- "Summarize the results section."
- "List all definitions in the introduction."

---

## 🚧 Roadmap

- [ ] Add token streaming support
- [ ] Multilingual PDF Q&A
- [ ] Support DOCX and scanned image OCR
- [ ] Deploy on Hugging Face Spaces

---

## 👨‍💻 Author

Built with passion by **Ojas Ganesh More**  
📬 Feel free to connect or fork, star ⭐, and contribute!

---

## 📜 License

This project is licensed under the **MIT License**.