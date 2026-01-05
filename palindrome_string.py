# Palindrome String Checker

text = input("Enter a string: ")

if text == text[::-1]:
    print("The string is a Palindrome")
else:
    print("The string is Not a Palindrome")
