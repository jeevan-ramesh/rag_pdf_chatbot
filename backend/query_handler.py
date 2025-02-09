import requests
from backend.config import MISTRAL_API_KEY
from backend.vector_store import vector_store

MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"

def get_mistral_response(query):
    relevant_texts = vector_store.search(query)  # Get relevant chunks
    context = "\n".join(relevant_texts)

    payload = {
        "model": "ministral-3b-2410",
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": f"Context: {context}\nQuestion: {query}"}
        ]
    }
    
    headers = {"Authorization": f"Bearer {MISTRAL_API_KEY}", "Content-Type": "application/json"}
    response = requests.post(MISTRAL_API_URL, headers=headers, json=payload)
    
    return response.json()["choices"][0]["message"]["content"]
