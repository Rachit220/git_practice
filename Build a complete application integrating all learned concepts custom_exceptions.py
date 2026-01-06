class FinanceError(Exception):
    pass

class InvalidAmountError(FinanceError):
    pass

class TransactionNotFoundError(FinanceError):
    pass
