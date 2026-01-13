# Email ID Validator Program

email = input("Enter email id: ")

if " " in email:
    print(" Invalid Email (contains space)")

elif "@" in email and "." in email and email.index("@") < email.index("."):
    print(" Valid Email")

else:
    print(" Invalid Email")