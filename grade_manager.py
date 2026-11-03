
# Student Grade Manager
# Week 1 - Day 2 Assignment

# Store all student records in a list of dictionaries.
# This allows two students to have the same name.

students = []


# Function to calculate grade
def get_grade(mark):

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


# Function to add a student
def add_student():

    name = input("Enter student name: ").strip()

    if name == "":
        print("Name cannot be empty!")
        return

    # Get and validate student mark
    while True:
        try:
            mark = int(input("Enter student mark (0-100): "))

            if mark < 0 or mark > 100:
                print("Mark must be between 0 and 100!")
                continue

            break

        except ValueError:
            print("Invalid input! Please enter a number.")

    # Store student details
    student = {
        "name": name,
        "mark": mark
    }

    students.append(student)

    print("Student added successfully!")


# Function to display all student results
def show_results():

    if len(students) == 0:
        print("No student records available!")
        return

    print("\n========== STUDENT RESULTS ==========")

    print(f"{'Name':<15} {'Mark':>8} {'Grade':>8}")
    print("-" * 35)

    marks = []

    for student in students:

        name = student["name"]
        mark = student["mark"]
        grade = get_grade(mark)

        marks.append(mark)

        print(f"{name:<15} {mark:>8} {grade:>8}")

    # Calculate class statistics
    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print("-" * 35)

    print(f"Average : {average:.1f}")
    print(f"Highest : {highest}")
    print(f"Lowest  : {lowest}")

    print("=" * 35)


# Main menu function
def main():

    while True:

        print("\n===== STUDENT GRADE MANAGER =====")
        print("1. Add Student")
        print("2. Show Results")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":

            add_student()

        elif choice == "2":

            show_results()

        elif choice == "3":

            print("Thank you! Program closed.")
            break

        else:

            print("Invalid choice! Please select 1, 2 or 3.")


# Program execution
if __name__ == "__main__":

    try:
        main()

    except (EOFError, KeyboardInterrupt):
        print("\nProgram closed safely.")
