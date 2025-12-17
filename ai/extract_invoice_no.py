import re

patterns = [
    r"no : [:\s]*([a-z0-9-/]+)",
    r"no: [:\s]*([a-z0-9-/]+)",
    r"invoice\s*(no|number|#)[:\s]*([a-z0-9-/]+)"
]


def extract_invoice_number(text):
    for p in patterns:
        m = re.search(p, text)
        if m:
            return m.group(len(m.groups()))
    return None