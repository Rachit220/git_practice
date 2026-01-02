def load_students(filename):
    students = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                name, marks = line.strip().split(",")
                students[name] = int(marks)
    except FileNotFoundError:
        print("Error: students file not found")
        return {}
    return students
def calculate_average(students):
    if not students:
        return 0
    total = sum(students.values())
    return total / len(students)

def find_topper(students):
    if not students:
        return None, 0

    topper = max(students, key=students.get)
    return topper, students[topper]

def save_report(avg, topper, marks):
    with open("report.txt", "w") as f:
        f.write(f"Average Marks: {avg:.2f}\n")

        if topper:
            f.write(f"Topper: {topper} ({marks})\n")
        else:
            f.write("No student data available\n")
def main():
    students = load_students("students.txt")
    avg = calculate_average(students)
    topper, marks = find_topper(students)
    save_report(avg, topper, marks)
    print("Report Generated Successfully")
if __name__ == "__main__":
    main()
