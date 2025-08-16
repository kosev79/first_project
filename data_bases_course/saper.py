import sqlite3 as sq

with sq.connect("saper.db") as con:
    cur = con.cursor()  # Cursor

# cur.execute("DROP TABLE IF EXISTS users")
cur.execute(
    """CREATE TABLE IF NOT EXISTS   games (
        user_id INTEGER,
        score INTEGER,
        time INTEGER
    )
"""
)
