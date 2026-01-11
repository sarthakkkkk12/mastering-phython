# Shopping Bill Generator

total = 0

for i in range(1, 4):
    price = float(input(f"Enter price of item {i}: "))
    total += price

print("Total Bill:", total)

if total > 2000:
    discount = total * 0.10
    total -= discount
    print("Discount Applied: 10%")

print("Final Amount to Pay:", total)