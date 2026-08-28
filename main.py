import json

students = []


def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)


def load_students():
    global students

    try:
        with open("students.json", "r") as file:
            students = json.load(file)

    except FileNotFoundError:
        students = []


def add_student():
    print("\n===== Add Student =====")

    name = input("Enter student name: ")
    age = input("Enter student age: ")

    while True:
        try:
            grade = float(input("Enter student grade: "))

            if 0 <= grade <= 100:
                break

            print("Grade must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

    student = {
        "name": name,
        "age": age,
        "grade": grade
    }

    students.append(student)
    save_students()

    print("Student added successfully!")


def view_students():
    if not students:
        print("\nNo students found.")
        return

    print("\n===== Students =====")

    for i, student in enumerate(students, start=1):
        print(f"\n{i}. Name: {student['name']}")
        print(f"   Age: {student['age']}")
        print(f"   Grade: {student['grade']}")
        print("--------------------")


def search_student():
    name = input("\nEnter student name to search: ")

    for student in students:
        if student["name"].lower() == name.lower():
            print("\n===== Student Found =====")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Grade: {student['grade']}")
            return

    print("Student not found.")


def edit_student():
    name = input("\nEnter student name to edit: ")

    for student in students:
        if student["name"].lower() == name.lower():

            print("\n===== Edit Student =====")
            print("Press Enter to keep the current value.")

            new_name = input(
                f"Enter new name ({student['name']}): "
            )

            new_age = input(
                f"Enter new age ({student['age']}): "
            )

            while True:
                new_grade = input(
                    f"Enter new grade ({student['grade']}): "
                )

                if new_grade == "":
                    break

                try:
                    new_grade = float(new_grade)

                    if 0 <= new_grade <= 100:
                        student["grade"] = new_grade
                        break

                    print("Grade must be between 0 and 100.")

                except ValueError:
                    print("Please enter a valid number.")

            if new_name:
                student["name"] = new_name

            if new_age:
                student["age"] = new_age

            save_students()

            print("Student updated successfully!")
            return

    print("Student not found.")


def delete_student():
    name = input("\nEnter student name to delete: ")

    for student in students:
        if student["name"].lower() == name.lower():

            print(f"\nStudent found: {student['name']}")

            confirmation = input(
                "Are you sure you want to delete this student? (y/n): "
            )

            if confirmation.lower() == "y":
                students.remove(student)
                save_students()
                print("Student deleted successfully!")
            else:
                print("Deletion cancelled.")

            return

    print("Student not found.")


def calculate_statistics():
    if not students:
        print("\nNo students found.")
        return

    grades = [student["grade"] for student in students]

    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)

    print("\n===== Grade Statistics =====")
    print(f"Number of students: {len(students)}")
    print(f"Average grade: {average:.2f}")
    print(f"Highest grade: {highest:.2f}")
    print(f"Lowest grade: {lowest:.2f}")


def main():
    load_students()

    while True:
        print("\n==============================")
        print("   STUDENT MANAGEMENT SYSTEM")
        print("==============================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Edit Student")
        print("5. Delete Student")
        print("6. Grade Statistics")
        print("7. Exit")
        print("==============================")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            edit_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            calculate_statistics()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
