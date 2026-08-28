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


def search_student():
    name = input("Enter student name to search: ")

    found = False

    for student in students:
        if student["name"].lower() == name.lower():
            print("\nStudent found!")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Grade: {student['grade']}")
            found = True
            break

    if not found:
        print("Student not found.")


def main():
    while True:
        print("\n==============================")
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

        elif choice == "3":
            search_student()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
