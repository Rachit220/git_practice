import random

choices = ["rock", "paper", "scissors"]

user_choice = input("Enter rock, paper, or scissors: ").lower()
computer_choice = random.choice(choices)

print("You chose:", user_choice)
print("Computer chose:", computer_choice)

if user_choice == computer_choice:
    print("Result: It's a TIE")

elif user_choice == "rock":
    if computer_choice == "scissors":
        print("Result: You WIN....!!")
    else:
        print("Result: You LOSE....!!")

elif user_choice == "paper":
    if computer_choice == "rock":
        print("Result: You WIN.....!!")
    else:
        print("Result: You LOSE...!!")

elif user_choice == "scissors":
    if computer_choice == "paper":
        print("Result: You WIN...!!")
    else:
        print("Result: You LOSE....!!")

else:
    print("Invalid choice")
