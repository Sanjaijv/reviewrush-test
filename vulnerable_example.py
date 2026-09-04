import os

# Hardcoded credential (gitleaks should flag this as a generic secret)
API_KEY = "gK9dP2xQmR7vT4nL8wY1cE6jH3sA0zV5bF9uI2oC7yN4kM8xR1nQ8"

def run_query(user_input):
    query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    os.system(query)
