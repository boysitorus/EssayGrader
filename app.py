from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer, util

app = FastAPI()
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

class EssayRequest(BaseModel):
    reference: str
    essay: str

@app.post("/evaluate/")
async def evaluate(data: EssayRequest):  # Pastikan parameter berasal dari request body
    emb1 = model.encode(data.reference, convert_to_tensor=True)
    emb2 = model.encode(data.essay, convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(emb1, emb2).item()
    return {"similarity_score": similarity}