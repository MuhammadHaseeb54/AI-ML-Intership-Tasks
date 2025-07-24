# chatbot.py
from langchain.chains import ConversationalRetrievalChain # or HuggingFaceHub
from langchain.memory import ConversationBufferMemory
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import OpenAI

def load_qa_chain(persist_path="faiss_index"):
    # Load vector store
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.load_local(persist_path, embeddings)

    # Setup memory
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    # QA Chain
    chain = ConversationalRetrievalChain.from_llm(
        llm=OpenAI(temperature=0),  # Replace with your OpenAI key or HuggingFace
        retriever=vector_store.as_retriever(),
        memory=memory
    )
    return chain
