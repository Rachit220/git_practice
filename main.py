from services.finance_service import FinanceService
from exceptions.custom_exceptions import FinanceError
from config.settings import CURRENCY

def menu():
    print(" PERSONAL FINANCE MANAGER")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Summary")
    print("4. View Transactions")
    print("5. Exit")

def main():
    service = FinanceService()

    while True:
        menu()
        choice = input("Choose option: ")

        try:
            if choice == "1":
                amt = float(input("Amount: "))
                cat = input("Category: ")
                service.add_transaction(amt, cat, "income")

            elif choice == "2":
                amt = float(input("Amount: "))
                cat = input("Category: ")
                service.add_transaction(amt, cat, "expense")

            elif choice == "3":
                income, expense, balance = service.get_summary()
                print(f"Income: {CURRENCY}{income}")
                print(f"Expense: {CURRENCY}{expense}")
                print(f"Balance: {CURRENCY}{balance}")

            elif choice == "4":
                for t in service.list_transactions():
                    print(t)

            elif choice == "5":
                print("Goodbye")
                break

            else:
                print("Invalid choice")

        except FinanceError as e:
            print("Error:", e)
        except ValueError:
            print("Invalid input")

if __name__ == "__main__":
    main()
