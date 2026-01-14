# Username Validator Program

username = input("Enter username: ")

if username.isalnum() and 5 <= len(username) <= 15:
    print(" Valid Username")
else:
    print("Invalid Username")