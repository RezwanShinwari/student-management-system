Student Management System

A simple command-line Student Management System built with Python.

This project was created to practice Python programming, data structures, file handling, JSON data persistence, input validation, and basic application design.

Features

- Add new students
- View all students
- Search for a student by name
- Edit student information
- Delete students
- Calculate grade statistics
- Save student data using JSON
- Load saved data when the program starts
- Validate grades between 0 and 100
- Handle invalid grade input

Technologies

- Python 3
- JSON
- Command Line Interface (CLI)

Project Structure

student-management-system/
│
├── main.py
└── README.md

The program creates a "students.json" file locally to store student data.

How to Run

1. Make sure Python 3 is installed.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

python main.py

Example

The program provides an interactive menu:

==============================
   STUDENT MANAGEMENT SYSTEM
==============================
1. Add Student
2. View Students
3. Search Student
4. Edit Student
5. Delete Student
6. Grade Statistics
7. Exit
==============================
Choose an option:

Data Storage

Student records are stored locally in a JSON file named "students.json".

This allows the program to keep student information after the application is closed and opened again.

Learning Goals

This project helped me practice:

- Python functions
- Lists and dictionaries
- Loops and conditional statements
- Exception handling
- File handling
- JSON serialization and deserialization
- Input validation
- Basic CRUD operations
- Organizing a small Python application

Future Improvements

Possible future improvements include:

- Student IDs
- Sorting and filtering students
- More detailed statistics
- A graphical user interface
- Database integration
- Automated tests

Author

Rezwan Shinwari

GitHub: "@RezwanShinwari" (https://github.com/RezwanShinwari)
