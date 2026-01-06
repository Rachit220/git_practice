import unittest
from services.finance_service import FinanceService

class TestFinanceService(unittest.TestCase):

    def test_add_income(self):
        service = FinanceService()
        service.add_transaction(1000, "Salary", "income")
        self.assertTrue(len(service.transactions) > 0)

if __name__ == "__main__":
    unittest.main()
