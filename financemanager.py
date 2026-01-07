import sqlite3
import requests
from datetime import date
DB_NAME = "finance.db"
API_URL = "https://api.exchangerate-api.com/v4/latest/INR"

def get_connection():
    return sqlite3.connect(DB_NAME)
def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        type TEXT NOT NULL,
        date TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()
def add_transaction(amount, category, t_type):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO transactions (amount, category, type, date) VALUES (?, ?, ?, ?)",
        (amount, category, t_type, str(date.today()))
    )
    conn.commit()
    conn.close()
def get_summary():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='income'")
    income = cursor.fetchone()[0] or 0
    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='expense'")
    expense = cursor.fetchone()[0] or 0
    conn.close()
    return income, expense, income - expense
def get_exchange_rate(currency):
    try:
        response = requests.get(API_URL, timeout=5)
        data = response.json()
        return data["rates"].get(currency)
    except Exception:
        return None
def main():
    create_tables()

    while True:
        print("Personal Finance Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Currency Rate")
        print("5. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            try:
                amt = float(input("Amount: "))
                cat = input("Category: ")
                add_transaction(amt, cat, "income")
                print("Income added")
            except ValueError:
                print("Invalid amount")
        elif choice == "2":
            try:
                amt = float(input("Amount: "))
                cat = input("Category: ")
                add_transaction(amt, cat, "expense")
                print("Expense added")
            except ValueError:
                print("Invalid amount")
        elif choice == "3":
            income, expense, balance = get_summary()
            print(f"Income: ₹{income}")
            print(f"Expense: ₹{expense}")
            print(f"Balance: ₹{balance}")
        elif choice == "4":
            cur = input("Currency (USD, EUR): ").upper()
            rate = get_exchange_rate(cur)
            if rate:
                print(f"1 INR = {rate} {cur}")
            else:
                print("Currency not found or API error")
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid choice, try again.")
if __name__ == "__main__":
    main()
