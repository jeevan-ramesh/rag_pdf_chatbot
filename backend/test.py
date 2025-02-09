import requests

API_KEY = "qkat04Xqv1cpvUFnTy03k90KV2j5rZHj"  # Replace with your actual API key
API_URL = "https://api.mistral.ai/v1/models"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

response = requests.get(API_URL, headers=headers)

if response.status_code == 200:
    print("✅ Available Models:", response.json())
else:
    print(f"❌ Error {response.status_code}: {response.text}")
