# Function for addition
def addition():
    number1 = input("What is your first number? ")
    number2 = input("What is your second number? ")
    result = int(number1) + int(number2)
    print("The result of the addition is:", result)

# Function for subtraction
def subtraction():
    number1 = input("What is your first number? ")
    number2 = input("What is your second number? ")
    result = int(number1) - int(number2)
    print("The result of the subtraction is:", result)

# Function for multiplication
def multiplication():
    number1 = input("What is your first number? ")
    number2 = input("What is your second number? ")
    result = int(number1) * int(number2)
    print("The result of the multiplication is:", result)

# Function for division
def division():
    number1 = input("What is your first number? ")
    number2 = input("What is your second number? ")
    # Check for division by zero
    if int(number2) != 0:
        result = int(number1) / int(number2)
        print("The result of the division is:", result)
    else:
        print("Error: Division by zero is not allowed.")

# Call the functions
addition()
subtraction()
multiplication()
division()
