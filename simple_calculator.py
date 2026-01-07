# Simple Calculator Program

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Choose operation (+, -, *, /): ")

if operator == "+":
    print("Result:", num1 + num2)

elif operator == "-":
    print("Result:", num1 - num2)

elif operator == "*":
    print("Result:", num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Division by zero not allowed")

else:
    print("Invalid operator")