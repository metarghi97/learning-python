# Prompt the user to enter a non-negative integer
n = int(input("Please provide a non-negative integer: "))

# Ensure the input is non-negative
if n < 0:
    print("Invalid input! Please enter a non-negative integer.")
else:
    # Initialize the factorial to 1
    factorial = 1
    
    # Calculate the factorial for each number from 1 to n
    for i in range(1, n + 1):
        factorial *= i  # Multiply the current factorial by i
        print(f"{i}: {factorial}")  # Output the current number and its factorial

