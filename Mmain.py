# List to store student data
students = []

# Function to calculate the total score and grade
def calculate_grade(scores):
    total = sum(scores)
    average = total / len(scores)
    
    # Assigning grade based on the average score
    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    return total, grade

# Function to add a new student
def add_student():
    name = input("Enter student's name: ")
    student_id = input("Enter student's ID: ")
    
    # Get scores for 3 subjects
    scores = []
    for i in range(3):
        score = int(input(f"Enter score for subject {i+1}: "))
        scores.append(score)
    
    # Calculate total score and grade
    total, grade = calculate_grade(scores)
    
    # Store student data in the list
    student_data = {
        'name': name,
        'id': student_id,
        'scores': scores,
        'total': total,
        'grade': grade
    }
    students.append(student_data)

# Function to display all students
def display_students():
    if not students:
        print("No students found.")
        return

    for student in students:
        print(f"Name: {student['name']}, ID: {student['id']}, Total Score: {student['total']}, Grade: {student['grade']}")

# Main menu function
def main_menu():
    while True:
        print("\n1. Add a student")
        print("2. Display all students")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid option, please try again.")

# Run the program
if __name__ == "__main__":
    main_menu()
