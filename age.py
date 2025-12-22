age = int(input("Enter your age: "))

if age >= 0:
    if age <= 12:
        category = "Child"
    else:
        if age <= 19:
            category = "Teen"
        else:
            if age <= 59:
                category = "Adult"
            else:
                category = "Senior"
else:
    category = "Invalid age"

print("Age category:", category)
