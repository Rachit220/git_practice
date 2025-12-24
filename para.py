def student_details(course="Python", *marks, **info):
    print("Course:", course)

    if marks:
        total = sum(marks)
        average = total / len(marks)
        print("Marks:", marks)
        print("Average Marks:", average)
    else:
        print("No marks provided")

    print("Student Information:")
    for key, value in info.items():
        print(f"{key} : {value}")


# Function calls
student_details(
    "Data Science",
    85, 90, 88,
    name="Rachit",
    age=20,
    city="Ahmedabad"
)

student_details(
    name="Aman",
    age=21
)
