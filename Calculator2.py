def addition(a,b):
    return a + b
def substractions (a,b):
    return a -b 
def multiplications(a,b):
    return a * b
def division(a,b):
    return a / b

num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

Operator = input("Select the Oprator (+,-,*./) :")

if Operator == "+":
    print(num1 ,"+" ,num2 ,"=" , addition(num1,num2))

elif Operator == "-":
    print(num1,"-", num2, "=",substractions(num1,num2))
    
elif Operator == "*":
    print(num1,"*",num2,"=",multiplications(num1,num2))
    
elif Operator ==  "/":
    print(num1,"/",num2,"=",division(num1,num2))
    
    
    




