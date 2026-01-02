def load_students(filename):
    file = open(filename, "r")
    students = {}
    for line in file:
        name, marks = line.split(",")
        students[name] = marks
    file.close()
    return students
def calculate_average(students):
    total = 0
    for marks in students.values():
        total += marks
    return total / len(students)
def find_topper(students):
    topper = ""
    highest = 0
    for name, marks in students.items():
        if marks > highest:
            highest = marks
            topper = name
    return topper, highest
def save_report(avg, topper, marks):
    f = open("report.txt", "w")
    f.write("Average: " + avg)
    f.write("\nTopper: " + topper + " (" + marks + ")")
    f.close()
def main():
    students = load_students("students.txt")
    avg = calculate_average(students)
    topper, marks = find_topper(students)
    save_report(avg, topper, marks)
    print("Report Generated")
    
main()
