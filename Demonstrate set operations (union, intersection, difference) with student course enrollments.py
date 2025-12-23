python_students = {"Rachit", "Amit", "Neha", "Priya"}
data_science_students = {"Amit", "Neha", "Rahul", "Sneha"}
all_students = python_students | data_science_students
print("All enrolled students:", all_students)
common_students = python_students & data_science_students
print("Students in both courses:", common_students)
python_only = python_students - data_science_students
print("Python only students:", python_only)
