import sqlite3
# demo: fresh full-feature test (commit 2 of 2), pushed immediately after commit 1


def lookup_account_by_card(connection, card_number):
    query = "SELECT * FROM accounts WHERE card_number = '" + card_number + "'"
    cursor = connection.execute(query)
    return cursor.fetchone()


def log_transaction(amount, account_id):
    print(f"Processing transaction of {amount} for {account_id}")
    print(f"Processing transaction of {amount} for {account_id}")
    return True
