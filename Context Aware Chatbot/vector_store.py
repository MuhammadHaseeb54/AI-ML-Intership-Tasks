# vector_store.py

from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
import os

def create_vector_store(data_path="data/knowledge_base.txt", persist_path="faiss_index"):
    # Load text file
    loader = TextLoader(data_path)
    docs = loader.load()

    # Split into chunks
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = splitter.split_documents(docs)

    # Create embeddings
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Create vector store
    vector_store = FAISS.from_documents(split_docs, embedding=embeddings)

    # Save FAISS index
    vector_store.save_local(persist_path)
    print("✅ Vector store created at:", persist_path)
