# GPA Calculator with User Input and Summary Function

grade_points = {
    'A+': 4.0, 'A': 4.0, 'A-': 3.6,
    'B+': 3.3, 'B': 3.0, 'B-': 2.67,
    'C+': 2.3, 'C': 2.0, 'C-': 1.7,
    'F': 0.0
}

# Function to calculate GPA
def calculate_gpa(grade_credit_list):
    total_points = 0
    total_credits = 0
    for grade, credit in grade_credit_list:
        point = grade_points.get(grade.upper(), 0.0)
        total_points += point * credit
        total_credits += credit
    if total_credits == 0:
        return 0.0
    return round(total_points / total_credits, 2)

# Function to print summary
def print_gpa_summary(student_name: str, gpa: float):
    print(f"\n📘 Student {student_name} has GPA: {round(gpa, 2)}")

# Get student name
student = input("Enter student name: ")

# Input grades and credit hours
print("\nEnter grades and credit hours (e.g., A 3). Type 'done' to finish.\n")

grade_credit_list = []
while True:
    entry = input("Enter grade and credit (or 'done' to finish): ")
    if entry.lower() == 'done':
        break
    try:
        grade, credit = entry.upper().split()
        credit = int(credit)
        if grade in grade_points:
            grade_credit_list.append((grade, credit))
        else:
            print("❌ Invalid grade. Please try again.")
    except:
        print("❌ Invalid input format. Use: A 3")

# Calculate and print result
gpa = calculate_gpa(grade_credit_list)
print_gpa_summary(student_name=student, gpa=gpa)
