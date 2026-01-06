# Program to find factorial of a number using loop

num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial is:", factorial)