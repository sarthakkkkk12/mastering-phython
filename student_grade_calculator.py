# Student Grade Calculator

total_marks = 0

for i in range(1, 6):
    marks = float(input(f"Enter marks of subject {i}: "))
    total_marks += marks

percentage = total_marks / 5

print("Percentage:", percentage)

if percentage >= 90:
    print("Grade: A+")
elif percentage >= 80:
    print("Grade: A")
elif percentage >= 70:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
else:
    print("Grade: Fail")