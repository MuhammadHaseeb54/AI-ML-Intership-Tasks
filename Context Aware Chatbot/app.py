# app.py

import streamlit as st
from chatbot import load_qa_chain

st.set_page_config(page_title="Context-Aware Chatbot")
st.title("🧠 Context-Aware Chatbot with RAG")

# Load chain
qa_chain = load_qa_chain()

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input
user_query = st.text_input("You:", key="input")

if user_query:
    # Run query
    response = qa_chain.run({"question": user_query})
    st.session_state.chat_history.append(("You", user_query))
    st.session_state.chat_history.append(("Bot", response))

# Display history
for speaker, message in st.session_state.chat_history:
    st.markdown(f"**{speaker}:** {message}")
