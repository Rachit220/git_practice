from app.models.calculator import Calculator
from app.exceptions.custom_exceptions import CalculationError

class CalculatorService:
    """Business logic layer"""

    def __init__(self):
        self.calculator = Calculator()

    def calculate(self, operation, a, b):
        try:
            if operation == "add":
                return self.calculator.add(a, b)
            elif operation == "subtract":
                return self.calculator.subtract(a, b)
            elif operation == "multiply":
                return self.calculator.multiply(a, b)
            elif operation == "divide":
                return self.calculator.divide(a, b)
            else:
                raise CalculationError("Invalid operation")
        except Exception as e:
            raise CalculationError(str(e))
