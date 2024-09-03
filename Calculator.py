#Simple Calculator:

# Write a program that performs basic arithmetic operations like addition, 
# subtraction, multiplication, 
# and division based on user input.

def additions(a,b):
    return a + b

def subtractions(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def division(a,b):
    return a/b

# Get user input for two numbers and an operator

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operator = input("Enter the operator (+, -, *, /): ")

# Perform the operation based on the user input
if operator == "+":
    print(num1, "+", num2, "=", additions(num1, num2))
    
elif operator == "-":
    print(num1, "-", num2, "=", subtractions(num1, num2))
    
elif operator == "*":
    print(num1, "*", num2, "=", multiplication(num1, num2))
    
elif operator == "/":
    print(num1, "/", num2, "=", division(num1, num2))