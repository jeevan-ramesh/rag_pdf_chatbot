from fastapi import FastAPI, UploadFile, File
from backend.document_loader import extract_text_from_pdf
from backend.vector_store import vector_store
from backend.query_handler import get_mistral_response

app = FastAPI()

@app.post("/upload_pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    content = await file.read()
    with open(file.filename, "wb") as f:
        f.write(content)

    text = extract_text_from_pdf(file.filename)
    vector_store.add_texts(text.split("\n"))
    
    return {"message": "PDF uploaded & processed successfully!"}

@app.get("/ask/")
async def ask_question(query: str):
    response = get_mistral_response(query)
    return {"response": response}
