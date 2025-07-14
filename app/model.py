from transformers import AutoTokenizer, AutoModelForSequenceClassification

MODEL_NAME = "indobenchmark/indobert-base-p1"
MODEL_FINETUNED = "yondikavl/artour-spam-filter"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_FINETUNED) 
model.eval()
