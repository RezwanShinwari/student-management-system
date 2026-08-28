students = []


def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = float(input("Enter student grade: "))

    student = {
        "name": name,
        "age": age,
        "grade": grade
    }

    students.append(student)

    print("Student added successfully!")


def view_students():
    if not students:
        print("No students found.")
        return

    print("\n===== Students =====")

    for i, student in enumerate(students, start=1):
        print(f"{i}. Name: {student['name']}")
        print(f"   Age: {student['age']}")
        print(f"   Grade: {student['grade']}")
        print("--------------------")


def main():
    print("==============================")
    print("   STUDENT MANAGEMENT SYSTEM")
    print("==============================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()


if __name__ == "__main__":
    main()
