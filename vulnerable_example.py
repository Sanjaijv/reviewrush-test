import os

API_KEY = os.environ.get("API_KEY", "")

def run_query(user_input):
    query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    os.system(query)
