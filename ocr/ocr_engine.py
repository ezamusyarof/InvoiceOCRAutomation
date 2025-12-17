from ocr.pdf_reader import read_pdf_text
from ocr.image_reader import ocr_image
from pdf2image import convert_from_path
import os

def ocr_document(path):
    if path.lower().endswith('.pdf'):
        text = read_pdf_text(path)
        if text.strip():
            return text
        images = convert_from_path(path)
        return ''.join([ocr_image(img) for img in images])
    else:
        return ocr_image(path)