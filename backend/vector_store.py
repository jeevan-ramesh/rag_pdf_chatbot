from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")  # Lightweight

# Store document embeddings
class VectorStore:
    def __init__(self):
        self.embeddings = []
        self.texts = []
        self.index = None

    def add_texts(self, texts):
        self.texts.extend(texts)
        embeddings = model.encode(texts)
        self.embeddings.extend(embeddings)
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(np.array(self.embeddings))

    def search(self, query, k=3):
        query_embedding = model.encode([query])
        distances, indices = self.index.search(query_embedding, k)
        return [self.texts[i] for i in indices[0]]

vector_store = VectorStore()
