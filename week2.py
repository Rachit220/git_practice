students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("\nEnter student name: ")
    marks = []

    subjects = int(input("Enter number of subjects: "))
    for j in range(subjects):
        mark = int(input(f"Enter marks for subject {j+1}: "))
        marks.append(mark)

    students[name] = marks

print("\n Student Grades Analysis\n")

for name, marks in students.items():
    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print(f"Student Name : {name}")
    print(f"Marks        : {marks}")
    print(f"Average      : {average:.2f}")
    print(f"Highest      : {highest}")
    print(f"Lowest       : {lowest}")
    print("-" * 30)
