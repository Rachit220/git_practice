from models.transaction import Transaction
from utils.file_handler import read_json, write_json
from config.settings import DATA_FILE
from exceptions.custom_exceptions import InvalidAmountError
from utils.logger import log_info

class FinanceService:
    def __init__(self):
        self.transactions = read_json(DATA_FILE)

    def add_transaction(self, amount, category, t_type):
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")

        txn = Transaction(amount, category, t_type)
        self.transactions.append(txn.to_dict())
        write_json(DATA_FILE, self.transactions)
        log_info(f"{t_type.capitalize()} added: {amount}")

    def get_summary(self):
        income = sum(t["amount"] for t in self.transactions if t["type"] == "income")
        expense = sum(t["amount"] for t in self.transactions if t["type"] == "expense")
        return income, expense, income - expense

    def list_transactions(self):
        return self.transactions
