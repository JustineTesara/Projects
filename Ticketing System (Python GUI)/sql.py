import sqlite3

con = sqlite3.connect("support.db")
cursor = con.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    issue TEXT,
    category TEXT,
    status TEXT
)               
               
""")

con.commit()
con.close()

