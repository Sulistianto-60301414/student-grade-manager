# Student Grade Manager
# Description: A simple Python console program to manage student grades.

def display_menu():
    print("\n=== Student Grade Manager ===")
    print("1. Add Student")
    print("2. View Students")
    print("3. Calculate Average Grade")
    print("4. Save and Exit")

def add_student(students):
    name = input("Enter student name: ").strip()
    try:
        grade = float(input("Enter grade (0-100): "))
        if 0 <= grade <= 100:
            students[name] = grade
            print(f" Added {name} with grade {grade}")
        else:
            print(" Grade must be between 0 and 100.")
    except ValueError:
        print(" Invalid input! Please enter a number for the grade.")

def view_students(students):
    if not students:
        print("No students added yet.")
        return
    print("\n--- Student List ---")
    for name, grade in students.items():
        print(f"{name}: {grade}")

def calculate_average(students):
    if not students:
        print("No data to calculate average.")
        return
    avg = sum(students.values()) / len(students)
    print(f"\n Class Average: {avg:.2f}")

def save_data(students, filename="grades.txt"):
    with open(filename, "w") as f:
        for name, grade in students.items():
            f.write(f"{name},{grade}\n")
    print(" Data saved successfully!")

def load_data(filename="grades.txt"):
    students = {}
    try:
        with open(filename, "r") as f:
            for line in f:
                name, grade = line.strip().split(",")
                students[name] = float(grade)
    except FileNotFoundError:
        pass
    return students

def main():
    students = load_data()
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            calculate_average(students)
        elif choice == "4":
            save_data(students)
            break
        else:
            print("Invalid choice, try again.")

main()
