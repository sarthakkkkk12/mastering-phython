# Email Username Extractor

email = input("Enter email id: ")

if "@" in email:
    username = email.split("@")[0]
    print("Username:", username)
else:
    print("Invalid email id")