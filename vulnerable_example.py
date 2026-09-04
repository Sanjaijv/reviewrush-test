import os
import sqlite3

API_KEY = os.environ.get("API_KEY", "")


def run_query(connection: sqlite3.Connection, user_input: str) -> list:
    cursor = connection.execute("SELECT * FROM users WHERE name = ?", (user_input,))
    return cursor.fetchall()
