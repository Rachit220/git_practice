class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.grades = []   # list to store grades

    # Add a grade
    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
            print(f"Grade {grade} added.")
        else:
            print("Invalid grade. Must be between 0 and 100.")

    # Calculate average grade
    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    # Get highest grade
    def highest_grade(self):
        if not self.grades:
            return None
        return max(self.grades)

    # Get lowest grade
    def lowest_grade(self):
        if not self.grades:
            return None
        return min(self.grades)

    # Display student report
    def display_report(self):
        print("\n--- Student Report ---")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Grades:", self.grades)
        print("Average:", self.calculate_average())
        print("Highest Grade:", self.highest_grade())
        print("Lowest Grade:", self.lowest_grade())


# Using the Student class
student1 = Student("Rachit", 100)

student1.add_grade(87)
student1.add_grade(88)
student1.add_grade(78)

student1.display_report()
