# ATM Withdrawal Simulator

balance = float(input("Enter your account balance: "))
withdraw = float(input("Enter withdrawal amount: "))

if withdraw > balance:
    print("❌ Insufficient Balance")

elif withdraw % 100 != 0:
    print("❌ Enter amount in multiples of 100")

else:
    balance -= withdraw
    print("✅ Withdrawal Successful")
    print("Remaining Balance:", balance)