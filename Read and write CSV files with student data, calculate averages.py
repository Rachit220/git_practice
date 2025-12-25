import csv

input_file = "students.csv"
output_file = "student_averages.csv"

students_result = []

# Read CSV file
with open(input_file, "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        maths = int(row["maths"])
        science = int(row["science"])
        english = int(row["english"])

        average = (maths + science + english) / 3

        students_result.append({
            "roll_no": row["roll_no"],
            "name": row["name"],
            "average": round(average, 2)
        })

# Write result to new CSV file
with open(output_file, "w", newline="") as file:
    fieldnames = ["roll_no", "name", "average"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for student in students_result:
        writer.writerow(student)

print("Student averages calculated and saved successfully!")
