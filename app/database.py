import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "smartlead.db"


def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS contact_requests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                message TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        
        
def save_contact_request(name, email, message):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute(
            """
            INSERT INTO contact_requests (name, email, message)
            VALUES (?, ?, ?)
            """,
            (name, email, message)
        )
        conn.commit()
        return cursor.lastrowid 
    

def get_contact_requests():
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            """
            SELECT id, name, email, message, created_at
            FROM contact_requests
            ORDER BY id DESC
            """
        ).fetchall()

        return [dict(row) for row in rows]