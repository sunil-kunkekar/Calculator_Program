# Recursive approach to calculate factorial
def factorial_calculations(num):
    if num ==0 or num==1:
        return 1
    else:
        return num * factorial_calculations(num-1)
    
    
# Iterative approach to calculate factorial
def  factorial_iterative(num):
    factorial = 1
    for i in range(num,num+1):
        num *= i
    return factorial

obj = int(input("Enter a number to calculate its factorial:"))

# Calculate factorial using recursive approach
factorial_records = factorial_calculations(obj)
print(f"Factorial of {obj} (recursive approach): {factorial_records}")


# Calculate factorial using iterative approach
factorial_Ite = factorial_iterative(obj)
print(f"Factorial of {obj} (iterative approach): {factorial_Ite}")
        
        
    
