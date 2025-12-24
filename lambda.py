# List of students with marks
students = [
    {"name": "Rachit", "marks": 85},
    {"name": "Aman", "marks": 72},
    {"name": "Falguni", "marks": 90},
    {"name": "Kiran", "marks": 60}
]

#filter(): Select students who passed (marks >= 70)
passed_students = list(filter(lambda s: s["marks"] >= 70, students))

#map(): Add 5 bonus marks to passed students
updated_students = list(
    map(lambda s: {**s, "marks": s["marks"] + 5}, passed_students)
)

#sorted(): Sort students by marks in descending order
final_result = sorted(
    updated_students,
    key=lambda s: s["marks"],
    reverse=True
)

# Display result
print("Final Student List:")
for student in final_result:
    print(student)
