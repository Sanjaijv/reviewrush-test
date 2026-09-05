import os
import sqlite3

API_KEY = os.environ.get("API_KEY", "")

def run_query(*args, **kwargs) -> list:
def run_query(connection: sqlite3.Connection, user_input: str) -> list:
    cursor = connection.execute("SELECT * FROM users WHERE name = ?", (user_input,))
    return cursor.fetchall()


def find_user_by_email(connection, email):
    # commit B, pushed immediately after commit A
    # looks up a single user record by email address
    cursor = connection.execute("SELECT * FROM users WHERE email = ?", (email,))
    return cursor.fetchone()


def find_user_by_username(connection, username):
    cursor = connection.execute("SELECT * FROM users WHERE username = ?", (username,))
    return cursor.fetchone()


def find_user_by_phone(connection, phone):
    query = "SELECT * FROM users WHERE phone = ?"
    cursor = connection.execute(query, (phone,))
    return cursor.fetchone()


def find_user_by_ssn(connection, ssn):
    query = "SELECT * FROM users WHERE ssn = '" + ssn + "'"
    cursor = connection.execute(query)
    return cursor.fetchone()
