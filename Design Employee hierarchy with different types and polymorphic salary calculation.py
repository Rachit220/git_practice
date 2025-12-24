# Base class
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def calculate_salary(self):
        raise NotImplementedError("Subclasses must implement this method")


# Full-time employee
class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


# Part-time employee
class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, hours_worked, hourly_rate):
        super().__init__(name, emp_id)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate


# Contract employee
class ContractEmployee(Employee):
    def __init__(self, name, emp_id, contract_amount):
        super().__init__(name, emp_id)
        self.contract_amount = contract_amount

    def calculate_salary(self):
        return self.contract_amount


# Using polymorphism
employees = [
    FullTimeEmployee("Rachit", 101, 50000),
    PartTimeEmployee("Aman", 102,  70, 500),
    ContractEmployee("Neha", 103, 30000)
]

for emp in employees:
    print(f"Employee: {emp.name}, Salary: ₹{emp.calculate_salary()}")
