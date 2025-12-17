import re

patterns = [
    r"(\d{2}/\d{2}/\d{4})",
    r"(\d{4}-\d{2}-\d{2})"
]

def extract_date(text):
    for p in patterns:
        m = re.search(p, text)
        if m:
            return m.group(1)
    return None
