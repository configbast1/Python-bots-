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

async def add_user(user_id: int, name: str):
    
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(
        "INSERT OR IGNORE INTO users (user_id, name) VALUES (?, ?)",
        (user_id, name)
    )
    conn.commit()
    conn.close() 
async def add_note(user_id: int, content: str):
   
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO notes (user_id, content) VALUES (?, ?)",
        (user_id, content)
    )
    conn.commit()
    conn.close()
async def get_notes(user_id: int):
   
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(
        "SELECT content FROM notes WHERE user_id = ?",
        (user_id,)
    )
    rows = cur.fetchall()
    conn.close()
    return [row[0] for row in rows]
    
