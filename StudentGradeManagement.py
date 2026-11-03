"""Simple Student Grade Manager - beginner Python assignment.

Concepts used: variables, input/output, data types, operators, if/elif/else,
loops, lists, dictionaries, functions, classes/objects, and try/except.
"""


class Student:
    """Store one student's details and calculate their grade."""

    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks  # Dictionary: subject name -> mark

    def calculate_total(self):
        return sum(self.marks.values())

    def calculate_average(self):
        return self.calculate_total() / len(self.marks)

    def calculate_grade(self):
        average = self.calculate_average()

        if average >= 90:
            return "A+"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        else:
            return "F"

    def display_details(self):
        print("\nStudent ID :", self.student_id)
        print("Name       :", self.name)
        for subject, mark in self.marks.items():
            print(f"{subject:<10}: {mark:g}")
        print("Total      :", self.calculate_total())
        print(f"Average    : {self.calculate_average():.2f}")
        print("Grade      :", self.calculate_grade())
        print("-" * 30)


# A list stores all Student objects created by the program.
students = []

# A tuple stores the subject names.
subjects = ("Tamil", "English", "Maths", "Science", "Social Science")


def add_student():
    """Read student details and add a Student object to the list."""
    student_id = input("Enter student ID: ").strip()

    if student_id == "":
        print("Student ID cannot be empty.")
        return

    # Check whether the ID is already used.
    for student in students:
        if student.student_id == student_id:
            print("This student ID already exists.")
            return

    name = input("Enter student name: ").strip()
    if name == "":
        print("Student name cannot be empty.")
        return

    marks = {}
    for subject in subjects:
        while True:
            try:
                mark = float(input(f"Enter {subject} mark (0-100): "))
                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break
                else:
                    print("Mark must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    new_student = Student(student_id, name, marks)
    students.append(new_student)
    print("Student added successfully!")


def display_all_students():
    """Display every student in the list."""
    if len(students) == 0:
        print("No student records found.")
    else:
        for student in students:
            student.display_details()


def search_student():
    """Find and display a student using their ID."""
    search_id = input("Enter student ID to search: ").strip()

    for student in students:
        if student.student_id == search_id:
            student.display_details()
            return

    print("Student not found.")


def main():
    """Show the menu until the user chooses Exit."""
    while True:
        print("\n===== STUDENT GRADE MANAGER =====")
        print("1. Add student")
        print("2. Display all students")
        print("3. Search student")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            display_all_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Thank you for using Student Grade Manager!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


# Start the program only when this file is run directly.
if __name__ == "__main__":
    main()
