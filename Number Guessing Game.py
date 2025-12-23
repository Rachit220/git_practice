import random

secret_number = random.randint(1, 100)
guess = None
attempts = 0

print(" Welcome to the Guessing Game!")
print("Guess a number between 1 and 100")

while guess != secret_number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess > secret_number:
        print(" Too high! Try a lower number.")
    elif guess < secret_number:
        print(" Too low! Try a higher number.")
    else:
        print(f" Congratulations! You guessed it in {attempts} attempts.")
