from fastapi import FastAPI
from sentence_transformers import SentenceTransformer, util

app = FastAPI()
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

@app.post("/evaluate/")
async def evaluate(reference: str, essay: str):
    emb1 = model.encode(reference, convert_to_tensor=True)
    emb2 = model.encode(essay, convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(emb1, emb2).item()
    return {"similarity_score": similarity}