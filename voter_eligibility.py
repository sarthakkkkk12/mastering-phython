# Voter Eligibility Checker

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
    print("You became eligible", age - 18, "years ago")
else:
    print("Not eligible to vote")
    print("You will be eligible in", 18 - age, "years")
