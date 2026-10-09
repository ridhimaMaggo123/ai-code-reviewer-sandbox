import sqlite3


def get_user(db_path, user_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = " + user_id)
    return cursor.fetchone()


def divide(a, b):
    return a / b
