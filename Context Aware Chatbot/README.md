# 🧠 Context-Aware Chatbot using LangChain and Streamlit

## ✅ Objective of the Task

The goal of this project is to build a **Context-Aware Chatbot** capable of answering questions based on a **custom set of documents**. Unlike traditional chatbots that rely solely on model knowledge, this one uses **Retrieval-Augmented Generation (RAG)** to provide accurate, contextual responses. It was deployed using **Streamlit** to create a user-friendly web interface.

---

## 🔍 Methodology / Approach

### 1. 📄 Document Ingestion
- Load user documents (text files in this version).
- Use `LangChain`’s `TextLoader` to read the files.
- Split text into manageable chunks using `CharacterTextSplitter`.

### 2. 🧠 Embedding + Vector Store
- Use `HuggingFaceEmbeddings` to convert text into numerical vectors.
- Store embeddings in **FAISS** (Facebook AI Similarity Search) for fast retrieval.

### 3. 🤖 Context-Aware Q&A
- When the user asks a question:
  - Retrieve relevant chunks from FAISS using semantic similarity.
  - Use `ConversationalRetrievalChain` (LangChain) to combine context with the question.
  - Generate answers using **OpenAI’s LLM** (or replaceable with HuggingFace models).

### 4. 🌐 Deployment with Streamlit
- A minimal frontend using `Streamlit` allows:
  - Uploading documents
  - Typing questions
  - Viewing chat history and contextual responses

---

## 📊 Key Results or Observations

- ✅ The chatbot accurately retrieved context from uploaded documents and answered questions specific to the content.
- ⚡ FAISS enabled **real-time** document search with low latency.
- 🤝 LangChain made it easy to create a memory-aware, conversational interface.
- 📎 Can be extended to support PDF, DOCX, or large datasets with minimal changes.
- 🧪 Successfully tested on `.txt` files with varying document sizes and question types.

---

## 🚀 Tech Stack

- Python
- Streamlit
- LangChain
- FAISS
- Sentence Transformers
- OpenAI (or HuggingFace)

---

## 📂 Run Locally

```bash
# Activate environment
venv\Scripts\activate  # or source venv/bin/activate (Mac/Linux)

# Install requirements
pip install -r requirements.txt

# Run the app
streamlit run app.py
