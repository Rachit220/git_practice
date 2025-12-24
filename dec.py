import time
from functools import wraps

#Logging Decorator
def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Function '{func.__name__}' started")
        print(f"[LOG] Arguments: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] Function '{func.__name__}' finished")
        return result
    return wrapper


#Timing Decorator
def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"[TIME] Execution time of '{func.__name__}': {end_time - start_time:.4f} seconds")
        return result
    return wrapper


#Function using BOTH decorators
@timing_decorator
@log_decorator
def calculate_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total


#Function call
result = calculate_sum(1_000_000)
print("Result:", result)
