# Function to perform the mathematical operation
def perform_operation(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        # Check for division by zero
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation."

# Main program
def main():
    # Get user input for the first number
    num1 = float(input("Enter the first number: "))
    
    # Get user input for the second number
    num2 = float(input("Enter the second number: "))
    
    # Get user input for the operation
    operation = input("Enter the operation (+, -, *, /): ")
    
    # Perform the operation and get the result
    result = perform_operation(num1, num2, operation)
    
    # Display the result
    if isinstance(result, str):
        print(result)
    else:
        print(f"{num1} {operation} {num2} = {result}")

# Run the main program
if __name__ == "__main__":
    main()