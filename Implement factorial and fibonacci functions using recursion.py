def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# Factorial
print("Factorial of 5:", factorial(5))

# Fibonacci
print("Fibonacci Series:")
for i in range(7):
    print(fibonacci(i), end=" ")
