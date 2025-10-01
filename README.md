---
title: Artour Filter Spam
emoji: 🐨
colorFrom: pink
colorTo: red
sdk: docker
pinned: false
---

# ArTour Spam Review Filter API

Proyek ini adalah **API berbasis FastAPI** yang digunakan untuk menyaring ulasan spam pada aplikasi **ArTour**.  
Model machine learning yang digunakan adalah hasil fine-tuning dari **IndoBERT** dan di-host di HuggingFace Hub.

## ✨ Fitur

- 🔎 API endpoint untuk memfilter ulasan
- ⚡ Model berbasis `transformers` (HuggingFace)
- 📦 Bisa dideploy di **HuggingFace Spaces** atau **VPS**
- ✅ Mengembalikan label **spam (1)** atau **non-spam (0)** dengan confidence score

---

## 📂 Struktur Proyek

├── app/
│ ├── filter_review.py # Fungsi untuk memproses teks dan memprediksi spam/non-spam
│ ├── model.py # Load model & tokenizer dari HuggingFace Hub
├── app.py # Entry point FastAPI (atau main.py jika belum diubah)
├── requirements.txt # Daftar dependency Python
├── Dockerfile # Konfigurasi container (opsional, untuk VPS)
└── README.md # Dokumentasi proyek

---

## 🚀 Cara Menjalankan

### 1. Lokally (di laptop/PC)

Pastikan sudah install Python 3.10+

```bash
git clone https://github.com/<username>/<repo-name>.git
cd <repo-name>
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 7860
```

API akan tersedia di:
👉 http://localhost:7860

Contoh request:

```bash
curl -X POST "http://localhost:7860/filter-review" \
     -H "Content-Type: application/json" \
     -d '{"text": "Promo murah! Klik link ini untuk hadiah gratis"}'
```

Response:

```bash
{
  "label": 1,
  "confidence": 0.945
}
```

### 2. Deploy ke HuggingFace Spaces

- Buat Space baru → pilih SDK: Docker / FastAPI
- Upload semua file (app/, app.py, requirements.txt, dll.)
- Pastikan requirements.txt sudah fix (lihat contoh di repo ini)
- Commit → Spaces akan auto-build → API bisa diakses di https://<username>-<space-name>.hf.space

---

Proyek ini untuk keperluan penelitian/akademik. Silakan disesuaikan bila digunakan secara komersial.
