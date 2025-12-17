from fastapi import FastAPI, UploadFile, File
import shutil, os, uuid
from ocr.ocr_engine import ocr_document
from ai.invoice_extractor import extract_invoice_fields
from db.database import insert_invoice, init_db

app = FastAPI(title="Invoice OCR API")
init_db()

UPLOAD_DIR = "data/api_uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/process-invoice")
def process_invoice(file: UploadFile = File(...)):
    filename = f"{uuid.uuid4()}_{file.filename}"
    filepath = os.path.join(UPLOAD_DIR, filename)

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        text = ocr_document(filepath)
        data = extract_invoice_fields(text)
        insert_invoice(data, filename, "success")
        return {**data, "status": "success"}

    except Exception as e:
        insert_invoice({}, filename, "failed")
        return {"status": "failed", "error": str(e)}