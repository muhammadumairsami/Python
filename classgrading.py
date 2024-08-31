# Define the list of students
students = [["ALI", 1, 70, 80, 90],
            ["REHAN", 2, 11, 22, 33],
            ["UMER", 3, 22, 11, 441]]

try:
    # Prompt the user to enter a roll number and attempt to convert it to an integer
    rollno = int(input("Enter roll number: "))
    
    try:
        # Use a generator expression with next() to find the student with the matching roll number
        student = next(student for student in students if student[1] == rollno)
        # Print the student's details if found
        print(student)
    except StopIteration:
        # Handle the case where no student with the given roll number is found
        print("Roll number not found")

except ValueError:
    # Handle the case where the input is not an integer
    print("Roll number should be an integer only")
