from datetime import datetime

class Transaction:
    def __init__(self, amount, category, t_type):
        self.amount = amount
        self.category = category
        self.type = t_type  
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "type": self.type,
            "date": self.date
        }
