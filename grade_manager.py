# Each dictionary in this list stores one student's name and mark.
students = []


def get_grade(mark):
    """Return the grade for a mark from 0 to 100."""
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


def get_valid_mark():
    """Ask for a mark until the user enters a whole number from 0 to 100."""
    while True:
        mark_text = input("Enter mark (0-100): ").strip()

        if mark_text == "":
            print("Mark cannot be empty. Please try again.")
            continue

        try:
            mark = int(mark_text)
        except ValueError:
            print("Invalid mark. Please enter a whole number, such as 85.")
            continue

        if mark < 0 or mark > 100:
            print("Mark must be between 0 and 100. Please try again.")
            continue

        return mark


def add_student():
    """Get a student's details and save them in the students list."""
    name = input("Enter student name: ").strip()

    if name == "":
        print("Student name cannot be empty. Student was not added.")
        return

    mark = get_valid_mark()

    student = {
        "name": name,
        "mark": mark
    }
    students.append(student)

    print(f"Student '{name}' added successfully.")


def show_results():
    """Display all students and the class statistics."""
    if len(students) == 0:
        print("No student records found. Please add a student first.")
        return

    # Find a suitable column width so names line up neatly.
    name_width = max(12, max(len(student["name"]) for student in students))

    print("\nSTUDENT RESULTS")
    print("-" * (name_width + 19))
    print(f"{'Name':<{name_width}} {'Mark':>6} {'Grade':>6}")
    print("-" * (name_width + 19))

    for student in students:
        name = student["name"]
        mark = student["mark"]
        grade = get_grade(mark)
        print(f"{name:<{name_width}} {mark:>6} {grade:>6}")

    print("-" * (name_width + 19))

    marks = [student["mark"] for student in students]
    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print(f"Average: {average:.1f}    Highest: {highest}    Lowest: {lowest}")
    print()


def main():
    """Show the menu and keep running until the user chooses Quit."""
    while True:
        print("\n===== STUDENT GRADE MANAGER =====")
        print("1. Add student")
        print("2. Show results")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            show_results()
        elif choice == "3":
            print("Thank you for using Student Grade Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nProgram closed safely.")
