class BankingError(Exception):
    """Base class for banking-related exceptions"""
    pass


class AccountNotFoundError(BankingError):
    def __init__(self, account_number):
        super().__init__(f"Account '{account_number}' not found.")


class InsufficientBalanceError(BankingError):
    def __init__(self, balance, amount):
        super().__init__(
            f"Insufficient balance. Available: ₹{balance}, Requested: ₹{amount}"
        )


class InvalidAmountError(BankingError):
    def __init__(self, amount):
        super().__init__(f"Invalid transaction amount: ₹{amount}")


class DailyLimitExceededError(BankingError):
    def __init__(self, limit):
        super().__init__(f"Daily withdrawal limit of ₹{limit} exceeded.")


class UnauthorizedAccessError(BankingError):
    def __init__(self):
        super().__init__("Unauthorized access detected. Incorrect PIN.")
class BankAccount:
    DAILY_WITHDRAW_LIMIT = 550000

    def __init__(self, account_number, holder_name, balance, pin):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
        self.pin = pin
        self.daily_withdrawn = 0

    def authenticate(self, pin):
        if self.pin != pin:
            raise UnauthorizedAccessError()

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError(amount)

        self.balance += amount
        print(f" ₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError(amount)

        if amount > self.balance:
            raise InsufficientBalanceError(self.balance, amount)

        if self.daily_withdrawn + amount > self.DAILY_WITHDRAW_LIMIT:
            raise DailyLimitExceededError(self.DAILY_WITHDRAW_LIMIT)

        self.balance -= amount
        self.daily_withdrawn += amount
        print(f" ₹{amount} withdrawn successfully.")

    def get_balance(self):
        return self.balance
class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def get_account(self, account_number):
        if account_number not in self.accounts:
            raise AccountNotFoundError(account_number)
        return self.accounts[account_number]
def main():
    bank = Bank()

    # Create Account
    account = BankAccount(
        account_number="101",
        holder_name="Rachit Prajapati",
        balance=10000,
        pin=1234
    )

    bank.add_account(account)

    try:
        # Fetch Account
        user_account = bank.get_account("101")

        # Authenticate User
        user_account.authenticate(1234)

        # Perform Transactions
        user_account.deposit(211000)
        user_account.withdraw(143000)
        user_account.withdraw(70000)  

    except BankingError as e:
        print(" Banking Error:", e)

    except Exception as e:
        print(" Unexpected Error:", e)

    finally:
        print("Current Balance: ₹", user_account.get_balance())
if __name__ == "__main__":
    main()
