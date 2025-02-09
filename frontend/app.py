import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("📄 RAG Chatbot")

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
if uploaded_file:
    files = {"file": uploaded_file.getvalue()}
    response = requests.post(f"{API_URL}/upload_pdf/", files=files)
    st.success(response.json()["message"])

# Chatbot Input
query = st.text_input("Ask a question:")
if st.button("Submit"):
    response = requests.get(f"{API_URL}/ask/", params={"query": query})
    st.write("🤖:", response.json()["response"])
