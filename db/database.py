import sqlite3
from datetime import datetime

DB_NAME = "invoice.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS invoices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_number TEXT,
    invoice_date TEXT,
    total_amount TEXT,
    source_file TEXT,
    status TEXT,
    created_at TEXT
    )
    """)
    conn.commit()
    conn.close()

def insert_invoice(data, filename, status):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        INSERT INTO invoices
        (invoice_number, invoice_date, total_amount, source_file, status, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        data.get("invoice_number"),
        data.get("invoice_date"),
        data.get("total_amount"),
        filename,
        status,
        datetime.now().isoformat()
    ))
    conn.commit()
    conn.close()