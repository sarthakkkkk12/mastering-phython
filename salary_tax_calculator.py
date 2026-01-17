# Salary Tax Calculator

monthly_salary = float(input("Enter monthly salary: "))

annual_salary = monthly_salary * 12
tax = 0

if annual_salary <= 250000:
    tax = 0
elif annual_salary <= 500000:
    tax = annual_salary * 0.05
elif annual_salary <= 1000000:
    tax = annual_salary * 0.10
else:
    tax = annual_salary * 0.15

net_salary = annual_salary - tax

print("Annual Salary:", annual_salary)
print("Tax Amount:", tax)
print("Net Annual Salary:", net_salary)