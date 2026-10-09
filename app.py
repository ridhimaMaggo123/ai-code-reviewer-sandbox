import sqlite3


def get_user(db_path, user_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    # SQL injection: user_id is concatenated directly into the query
    cursor.execute("SELECT * FROM users WHERE id = " + user_id)
    return cursor.fetchone()


def divide(a, b):
    # No guard against b == 0 -> ZeroDivisionError on bad input
    return a / b


def load_config(path):
    try:
        with open(path) as f:
            return f.read()
    except:
        # bare except swallows everything, including KeyboardInterrupt
        pass


API_KEY = "sk-prod-12345-hardcoded-secret"
