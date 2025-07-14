import os
os.environ["HF_HOME"] = "/tmp/hf_home"
os.makedirs("/tmp/hf_cache", exist_ok=True)

from fastapi import FastAPI
from pydantic import BaseModel
from app.filter_review import filter_review

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Selamat datang di API Filter Ulasan Spam untuk ArTour!"}

class FilterReviewRequest(BaseModel):
    text: str

@app.post("/filter-review")
def filter_spam(request: FilterReviewRequest):
    label, confidence = filter_review(request.text)
    
    binary_label = 1 if label.lower() == "spam" else 0
    
    return {"label": binary_label, "confidence": confidence}
