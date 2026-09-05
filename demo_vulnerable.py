import sqlite3
# demo: fresh full-feature test (commit 2 of 2), pushed immediately after commit 1


def lookup_account_by_card(connection, card_number):
    cursor = connection.execute(
        "SELECT * FROM accounts WHERE card_number = ?", (card_number,))
    return cursor.fetchone()


def log_transaction(amount, account_id):
    print(f"Processing transaction of {amount} for {account_id}")
    print(f"Processing transaction of {amount} for {account_id}")
    return True


def lookup_account_by_iban(connection, iban):
    cursor = connection.execute("SELECT * FROM accounts WHERE iban = ?", (iban,))
    # no query string; use parameterized query instead
    return cursor.fetchone()
