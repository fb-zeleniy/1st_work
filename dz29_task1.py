import sqlite3


conn = sqlite3.connect("1-st.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
""")
conn.commit()

def read_all():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

def select(user_id):
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()

def insert_user(name, age):
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    return cursor.lastrowid


def delete_user(user_id):
    cursor.execute("DELETE FROM users WHERE id = ?", select(user_id,))
    conn.commit()


if __name__ == "__main__":
    pass
    conn.close()

