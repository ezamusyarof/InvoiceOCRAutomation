from ai.preprocess import normalize_text
from ai.extract_invoice_no import extract_invoice_number
from ai.extract_date import extract_date
from ai.extract_total import extract_total

def extract_invoice_fields(raw_text):
    text = normalize_text(raw_text)
    return {
        "invoice_number": extract_invoice_number(text),
        "invoice_date": extract_date(text),
        "total_amount": extract_total(text)
    }