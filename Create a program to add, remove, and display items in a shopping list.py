shopping_list = []

while True:
    print("\n--- Shopping List Menu ---")
    print("1. Add item")
    print("2. Remove item")
    print("3. Display shopping list")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(f"{item} added to the shopping list.")

    elif choice == "2":
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed from the shopping list.")
        else:
            print("Item not found in the shopping list.")

    elif choice == "3":
        if shopping_list:
            print("\nYour Shopping List:")
            for i, item in enumerate(shopping_list, start=1):
                print(f"{i}. {item}")
        else:
            print("Your shopping list is empty.")

    elif choice == "4":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1-4.")
