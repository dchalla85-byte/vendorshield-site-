from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from utils.parser import extract_text_from_file
from utils.analyzer import analyze_invoice
from utils.exporter import save_to_excel
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # update this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/scan")
async def scan_invoice(file: UploadFile = File(...)):
    contents = await file.read()
    filename = file.filename
    file_path = os.path.join("uploads", filename)

    with open(file_path, "wb") as f:
        f.write(contents)

    text = extract_text_from_file(file_path)
    result = analyze_invoice(text)
    save_to_excel(filename, result)

    return result
