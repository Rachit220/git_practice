score = int(input("Enter your numerical grade: "))
if score >= 90 and score <= 100:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "c"
elif score >= 60:
    grade = "D"
elif score >= 0:
    grade ="F"
else:
    grade = "Invalid score"
print("Your letter grade is:", grade)
