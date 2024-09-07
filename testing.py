# Define a function for addition
def addition():
    number1 = input("What is your first number? ")
    number2 = input("What is your second number? ")
    
    # Convert inputs to integers and perform addition
    result = int(number1) + int(number2)
    print("The result of the addition is:", result)

# Define a function for subtraction
def subtraction():
    number1 = input("What is your first number? ")
    number2 = input("What is your second number? ")
    
    # Convert inputs to integers and perform subtraction
    result = int(number1) - int(number2)
    print("The result of the subtraction is:", result)

# Define a function for multiplication
def multiplication():
    number1 = input("What is your first number? ")
    number2 = input("What is your second number? ")
    
    # Convert inputs to integers and perform multiplication
    result = int(number1) * int(number2)
    print("The result of the multiplication is:", result)

# Define a function for division
def division():
    number1 = input("What is your first number? ")
    number2 = input("What is your second number? ")
    
    result = int(number1) / int(number2)
    print("The result of the division is:", result)

# Call the functions to perform the operations
addition()
subtraction()
multiplication()
division()
