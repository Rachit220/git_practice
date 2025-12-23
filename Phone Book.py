phone_book = {}

while True:
    print("\n PHONE BOOK MENU")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        phone_book[name] = number
        print("Contact added successfully")

    elif choice == "2":
        name = input("Enter name to search: ")
        if name in phone_book:
            print(f"{name}'s number is {phone_book[name]}")
        else:
            print("Contact not found")

    elif choice == "3":
        name = input("Enter name to update: ")
        if name in phone_book:
            phone_book[name] = input("Enter new phone number: ")
            print("Contact updated successfully")
        else:
            print("Contact not found")

    elif choice == "4":
        name = input("Enter name to delete: ")
        if name in phone_book:
            del phone_book[name]
            print("Contact deleted successfully")
        else:
            print("Contact not found")

    elif choice == "5":
        if phone_book:
            print("\n All Contacts:")
            for name, number in phone_book.items():
                print(f"{name}: {number}")
        else:
            print("Phone book is empty")

    elif choice == "6":
        print("Exiting Phone Book")
        break

    else:
        print("Invalid choice, try again")
