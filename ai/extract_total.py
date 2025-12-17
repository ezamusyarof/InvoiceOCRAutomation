import re

patterns = [
    r"total\s*keseluruhan[:\s]*rp?\.?\s*([\d.,]+)",
    r"grand\s*total[:\s]*rp?\.?\s*([\d.,]+)"
]

def extract_total(text):
    for p in patterns:
        m = re.search(p, text)
        if m:
            return m.group(1)
    return None