# Number Classification Program

num = int(input("Enter a number: "))
num = abs(num)   # handle negative numbers

if num < 10:
    print("Single-digit number")
elif num < 100:
    print("Double-digit number")
else:
    print("More than two digits")