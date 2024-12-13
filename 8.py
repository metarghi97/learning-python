# Function to classify grades based on scores
def determine_grade(score):
    if score >= 70:
        return "Distinction"
    elif score >= 60:
        return "Merit"
    elif score >= 50:
        return "Pass"
    else:
        return "Fail"

# Paths for input and output files
input_file = "input.txt"
output_file = "output.txt"

# Dictionary to store cumulative scores for students
student_scores = {}

# Process the input file
with open(input_file, "r") as infile:
    for line in infile:
        name, subject, score, weightage = line.strip().split(", ")
        score = float(score)
        weightage = float(weightage)

        # Calculate weighted score and update the dictionary
        student_scores[name] = student_scores.get(name, 0) + score * (weightage / 100)

# Generate the output file
with open(output_file, "w") as outfile:
    for student, total_score in student_scores.items():
        result = determine_grade(total_score)
        outfile.write(f"{student},{total_score:.1f},{result}\n")

print("Processing complete! Check the output file.")
