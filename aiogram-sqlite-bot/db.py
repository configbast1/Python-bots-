import sqlite3

DB_NAME = "bot.db"

async def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            name TEXT
        )
    """)
 
    cur.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            content TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS poll_answers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            poll_id TEXT,
            answer TEXT
        )
    """)

    conn.commit()
    conn.close()
