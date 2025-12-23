while True:
    print("\n==== MENU ====")
    print("1. Say Hello")
    print("2. Add Two Numbers")
    print("3. Skip this turn")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(" Hello! Welcome to the program.")

    elif choice == "2":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Sum =", a + b)

    elif choice == "3":
        print(" Skipping this option...")
        continue   # Go back to menu

    elif choice == "4":
        print("Exiting program. Goodbye!")
        break      # Exit loop

    else:
        print("Invalid choice. Try again.")
        continue
