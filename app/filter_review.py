import os
os.environ["HF_HOME"] = "./tmp/hf_home"
os.makedirs("./tmp/hf_cache", exist_ok=True)

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

MODEL_FINETUNED = "yondikavl/artour-spam-filter"

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = AutoModelForSequenceClassification.from_pretrained( MODEL_FINETUNED)
tokenizer = AutoTokenizer.from_pretrained(MODEL_FINETUNED)
model.eval()

def filter_review(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
    inputs = {k: v.to(device) for k, v in inputs.items()}
    with torch.no_grad():
        outputs = model(**inputs)
        probs = F.softmax(outputs.logits, dim=1)
        pred = torch.argmax(probs, dim=1).item()
    label = "spam" if pred == 1 else "non-spam"
    confidence = probs[0][pred].item()
    return label, confidence
