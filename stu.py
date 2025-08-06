import csv
from tabulate import tabulate

# File to store report card records
CSV_FILE = 'report_cards.csv'

# Subject list (customizable)
SUBJECTS = ['Math', 'Science', 'English', 'History', 'Computer']

# Grade assignment logic
def calculate_grade(percentage):
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    elif percentage >= 50:
        return 'D'
    else:
        return 'F'

# Add a student record
def add_student():
    name = input("Enter student's name: ")
    roll_no = input("Enter roll number: ")
    
    print(f"Enter marks out of 100 for the following {len(SUBJECTS)} subjects:")
    marks = []
    for subject in SUBJECTS:
        while True:
            try:
                score = float(input(f'{subject}: '))
                if 0 <= score <= 100:
                    marks.append(score)
                    break
                else:
                    print("Please enter a score between 0 and 100.")
            except ValueError:
                print("Invalid input. Enter a numeric value.")

    total = sum(marks)
    percentage = total / len(SUBJECTS)
    grade = calculate_grade(percentage)

    # Save to CSV
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([roll_no, name] + marks + [total, round(percentage, 2), grade])
    
    print("\n✅ Student record added successfully.")

# Display all report cards
def display_report_cards():
    try:
        with open(CSV_FILE, mode='r') as file:
            reader = csv.reader(file)
            headers = ['Roll No', 'Name'] + SUBJECTS + ['Total', 'Percentage', 'Grade']
            records = list(reader)

            if not records:
                print("📭 No records found.")
                return

            print("\n📄 All Student Report Cards:")
            print(tabulate(records, headers=headers, tablefmt="grid"))
    except FileNotFoundError:
        print("🚫 No report card file found. Please add student records first.")

# Initialize CSV with header if not exists
def init_csv():
    try:
        with open(CSV_FILE, mode='r') as file:
            pass  # File already exists
    except FileNotFoundError:
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Roll No', 'Name'] + SUBJECTS + ['Total', 'Percentage', 'Grade'])

# Menu loop
def menu():
    init_csv()
    while True:
        print("\n===== Student Report Card Generator =====")
        print("1. Add Student Record")
        print("2. View All Report Cards")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_report_cards()
        elif choice == '3':
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❗ Invalid choice. Please enter 1, 2, or 3.")

if _name_ == '_main_':
    menu()