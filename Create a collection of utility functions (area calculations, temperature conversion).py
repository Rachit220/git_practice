import math

while True:
    print("\n UTILITY FUNCTIONS MENU ")
    print("1. Area of Circle")
    print("2. Area of Rectangle")
    print("3. Area of Triangle")
    print("4. Celsius to Fahrenheit")
    print("5. Fahrenheit to Celsius")
    print("6. Celsius to Kelvin")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        r = float(input("Enter radius: "))
        print("Area of Circle =", math.pi * r * r)

    elif choice == "2":
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        print("Area of Rectangle =", l * w)

    elif choice == "3":
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        print("Area of Triangle =", 0.5 * b * h)

    elif choice == "4":
        c = float(input("Enter Celsius: "))
        print("Fahrenheit =", (c * 9/5) + 32)

    elif choice == "5":
        f = float(input("Enter Fahrenheit: "))
        print("Celsius =", (f - 32) * 5/9)

    elif choice == "6":
        c = float(input("Enter Celsius: "))
        print("Kelvin =", c + 273.15)

    elif choice == "7":
        print("Exiting program. Goodbye!")
        break

    else:
        print(" Invalid choice. Try again.")
