from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "SmartLead AI calisiyor!"

if __name__ == "__main__":
    app.run(debug=True)
    
    
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