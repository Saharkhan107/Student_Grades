#Course: CIS 103
#Instructor: Md Ali
#Student: Sahar Iqbal
#Date: 10/03/2024

def grade_category(grade):
    """Returns the grade category based on the grade value."""
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'

def main():
    # Dictionary to hold student names and their grades
    student_grades = {}

    # Input number of students
    try:
        num_students = int(input("Enter the number of students: "))
        # Check if the number is positive
        if num_students <= 0:
            print("Please enter a positive number of students.")
            return
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    # Loop to input each student's name and grade
    for _ in range(num_students):
        name = input("Enter student name: ")
        # Validate that the name is not empty
        if name.strip() == "":
            print("Name cannot be empty. Please enter a valid name.")
            continue
        
        try:
            # Prompt for the student's grade
            grade_input = input(f"Enter grade for {name}: ")
            # Check if the grade input is empty
            if grade_input.strip() == "":
                print(f"No grade entered for {name}. Skipping...")
                continue
            # Convert the input grade to a float
            grade = float(grade_input)
            # Store the name and grade in the dictionary
            student_grades[name] = grade
        except ValueError:
            # Handle the case where the input is not a valid number
            print("Invalid input. Please enter a numeric grade.")
            continue

    # Check if any grades were entered
    if student_grades:
        # Calculate average, highest, and lowest grades
        grades = list(student_grades.values())  # Get all grades
        average = sum(grades) / len(grades)     # Calculate average
        highest = max(grades)                   # Find highest grade
        lowest = min(grades)                     # Find lowest grade

        # Display results
        print("\nStudent Grades:")
        for name, grade in student_grades.items():
            category = grade_category(grade)  # Get the grade category
            print(f"{name}: {grade} ({category})")  # Print name, grade, and category

        # Print summary statistics
        print(f"\nClass Average: {average:.2f}")
        print(f"Highest Grade: {highest}")
        print(f"Lowest Grade: {lowest}")

        # Save the results to a file
        with open("student_grades.txt", "w") as file:
            for name, grade in student_grades.items():
                file.write(f"{name}: {grade} ({grade_category(grade)})\n")
        print("Grades saved to student_grades.txt")
    else:
        print("No grades entered.")

if __name__ == "__main__":
    main()

