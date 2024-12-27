import sqlite3


class Database:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
            CREATE TABLE IF NOT EXISTS complaints
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            contact_info TEXT,
            complaint VARCHAR(300),
            date DATE)
            """)
            conn.commit()

    def save_complaint(self, data: dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
            INSERT INTO complaints
            (name, contact_info, complaint,date)
            VALUES 
            (?,?,?,?)
            """,
                         (data['name'],
                          data['contact_info'],
                          data['complaint'],
                          data['complaint_date']))
