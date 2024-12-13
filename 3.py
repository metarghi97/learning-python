# Function to assign grades based on the mark
def assign_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 40:
        return "D"
    elif score >= 30:
        return "E"
    elif score >= 20:
        return "F"
    else:
        return "Invalid input. Please enter a number between 20 and 100."

# Get the student's mark and convert it to a float
score = float(input("Please enter the student's mark: "))

# Display the grade
print(assign_grade(score))
