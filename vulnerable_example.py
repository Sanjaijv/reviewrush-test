import os
import sqlite3

API_KEY = os.environ.get("API_KEY", "")

def run_query(*args, **kwargs) -> list:
    if len(args) == 1 and isinstance(args[0], str):
        user_input = args[0]
        connection = kwargs.get("connection")
        if connection is None:
            raise TypeError("Missing required argument: connection")
    elif len(args) == 2 and isinstance(args[0], sqlite3.Connection) and isinstance(args[1], str):
        connection, user_input = args
    else:
        raise TypeError("run_query() signature mismatch")
    cursor = connection.execute("SELECT * FROM users WHERE name = ?", (user_input,))
    return cursor.fetchall()
    return cursor.fetchall()


def find_user_by_email(connection, email):
    # looks up a single user record by email address
    query = "SELECT * FROM users WHERE email = '" + email + "'"
    cursor = connection.execute(query)
    return cursor.fetchone()
