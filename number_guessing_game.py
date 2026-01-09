import random

# Generate random number between 1 and 50
secret_number = random.randint(1, 50)

attempts = 0

print("🎯 Welcome to Number Guessing Game!")
print("Guess a number between 1 and 50")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess > secret_number:
        print("Too High ❌")

    elif guess < secret_number:
        print("Too Low ❌")

    else:
        print("🎉 Correct! You guessed it in", attempts, "attempts.")
        break