# Store student grades in a list
grades = []

# Take input from user
n = int(input("Enter number of students: "))

for i in range(n):
    score = float(input(f"Enter grade for student {i + 1}: "))
    grades.append(score)

# Calculate results
average = sum(grades) / len(grades)
highest = max(grades)
lowest = min(grades)

# Display results
print("\n--- Student Grade Report ---")
print("Grades:", grades)
print("Average Score:", average)
print("Highest Score:", highest)
print("Lowest Score:", lowest)
