class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance_amount = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance_amount += amount
            print(f"Deposited ₹{amount}. New Balance: ₹{self.balance_amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance_amount:
            print("Insufficient balance.")
        else:
            self.balance_amount -= amount
            print(f"Withdrawn ₹{amount}. New Balance: ₹{self.balance_amount}")

    def balance(self):
        print(f"Current Balance: ₹{self.balance_amount}")


# Using the class
account = BankAccount("Rachit", 1000)

account.balance()
account.deposit(7000)
account.withdraw(3050)
account.withdraw(1700)
account.balance()
