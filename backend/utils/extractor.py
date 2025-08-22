from pdf2image import convert_from_path
import pytesseract
import os
from PyPDF2 import PdfReader

def extract_text_from_pdf(file_path):
    # First try to extract text directly
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    
    # If no text found, use OCR as fallback
    if not text.strip():
        print("No direct text found. Running OCR...")
        text = extract_text_with_ocr(file_path)
    
    return text

def extract_text_with_ocr(file_path):
    # Convert PDF to images (one per page)
    images = convert_from_path(file_path)
    
    text = ""
    for i, image in enumerate(images):
        text += pytesseract.image_to_string(image)
    
    return text
