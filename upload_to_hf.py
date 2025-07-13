from huggingface_hub import create_repo, upload_folder
import os

HF_USERNAME = "yondikavl"
REPO_NAME = "artour-spam-filter"
MODEL_DIR = "./app/finetuned_model"
PRIVATE = True

if not os.path.exists(MODEL_DIR):
    raise FileNotFoundError(f"Folder {MODEL_DIR} tidak ditemukan!")

repo_id = f"{HF_USERNAME}/{REPO_NAME}"
print(f"📦 Membuat repo di HuggingFace: {repo_id} ...")
create_repo(repo_id, private=PRIVATE, exist_ok=True)

print(f"⬆️  Mengupload folder: {MODEL_DIR} ke {repo_id} ...")
upload_folder(
    folder_path=MODEL_DIR,
    repo_id=repo_id,
    repo_type="model"
)

print(f"✅ Sukses! Model tersedia di: https://huggingface.co/{repo_id}")
