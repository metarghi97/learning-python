# Prompt user for input and convert to float
first_number = float(input("insert the first number: "))
second_number = float(input("insert the second number: "))

# Perform calculations and handle division by zero
total = first_number + second_number
difference = first_number - second_number
product = first_number * second_number
quotient = first_number / second_number if second_number != 0 else "Undefined (unable to divide by 0)"

# Output the results, converting numerical results to strings
print(f"Sum: {total}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Quotient: {quotient}")
