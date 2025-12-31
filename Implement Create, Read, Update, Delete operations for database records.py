import mysql.connector
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Rachit@2025",
        database="crud_db"
    )
def create_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)",
        (name, age, course)
    )
    conn.commit()
    conn.close()
    print("Student Added")
def read_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    print("STUDENT RECORDS")
    for r in records:
        print(f"ID:{r[0]} Name:{r[1]} Age:{r[2]} Course:{r[3]}")

    conn.close()
def update_student():
    sid = int(input("Enter ID to update: "))
    name = input("New Name: ")
    age = int(input("New Age: "))
    course = input("New Course: ")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE students SET name=%s, age=%s, course=%s WHERE id=%s",
        (name, age, course, sid)
    )
    conn.commit()
    conn.close()
    print("Student Updated")
def delete_student():
    sid = int(input("Enter ID to delete: "))

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=%s", (sid,))
    conn.commit()
    conn.close()
    print("Student Deleted")
while True:
    print("\n STUDENT MANAGEMENT SYSTEM")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        create_student()
    elif choice == "2":
        read_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting Program")
        break
    else:
        print("Invalid Choice")
