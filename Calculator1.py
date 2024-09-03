import math

# Basic arithmetic functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Advanced functions for engineering calculator
def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error! Cannot take the square root of a negative number."
    return math.sqrt(x)

def logarithm(x, base=10):
    if x <= 0:
        return "Error! Logarithm of non-positive numbers is undefined."
    return math.log(x, base)

def natural_log(x):
    return logarithm(x, math.e)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def factorial(x):
    if x < 0:
        return "Error! Factorial of negative number is undefined."
    return math.factorial(int(x))

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power (x^y)")
    print("6. Square Root")
    print("7. Logarithm (base 10)")
    print("8. Natural Logarithm (ln)")
    print("9. Sine")
    print("10. Cosine")
    print("11. Tangent")
    print("12. Factorial")

    choice = input("Enter choice (1/2/3/4/5/6/7/8/9/10/11/12): ")

    if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']:
        if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter first number: "))
            if choice != '6':
                num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"The result of {num1} + {num2} is {add(num1, num2)}")

        elif choice == '2':
            print(f"The result of {num1} - {num2} is {subtract(num1, num2)}")

        elif choice == '3':
            print(f"The result of {num1} * {num2} is {multiply(num1, num2)}")

        elif choice == '4':
            result = divide(num1, num2)
            print(f"The result of {num1} / {num2} is {result}")

        elif choice == '5':
            print(f"The result of {num1} ^ {num2} is {power(num1, num2)}")

        elif choice == '6':
            num1 = float(input("Enter the number: "))
            print(f"The square root of {num1} is {square_root(num1)}")

        elif choice == '7':
            num1 = float(input("Enter the number: "))
            print(f"The logarithm base 10 of {num1} is {logarithm(num1)}")

        elif choice == '8':
            num1 = float(input("Enter the number: "))
            print(f"The natural logarithm (ln) of {num1} is {natural_log(num1)}")

        elif choice == '9':
            num1 = float(input("Enter the angle in degrees: "))
            print(f"The sine of {num1} degrees is {sine(num1)}")

        elif choice == '10':
            num1 = float(input("Enter the angle in degrees: "))
            print(f"The cosine of {num1} degrees is {cosine(num1)}")

        elif choice == '11':
            num1 = float(input("Enter the angle in degrees: "))
            print(f"The tangent of {num1} degrees is {tangent(num1)}")

        elif choice == '12':
            num1 = float(input("Enter the number: "))
            print(f"The factorial of {num1} is {factorial(num1)}")

    else:
        print("Invalid input. Please enter a number between 1 and 12.")

if __name__ == "__main__":
    calculator()
