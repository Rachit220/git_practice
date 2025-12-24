# Function definitions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


# Higher-order function (takes another function as parameter)
def calculate(operation, x, y):
    result = operation(x, y)
    print("Result:", result)


# Function calls
calculate(add, 10, 5)
calculate(subtract, 10, 5)
calculate(multiply, 10, 5)
