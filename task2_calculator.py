num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
print("choose an operation:")
print("+ for addition")
print("- for subtraction")
print("* for multipication")
print("/ for division")
operation=input("enter your operation:")
if operation== "+":
    result=num1+num2
    print("result =", result)
elif operation== "-":
    result=num1-num2
    print("result =", result)
elif operation== "*":
    result=num1*num2
    print("result =", result)
elif operation== "/":
    result=num1/num2
    print("result =", result)
else:
    print("Invalid Operation")





