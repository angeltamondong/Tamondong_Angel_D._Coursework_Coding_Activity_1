# Generate a random secret number from 1 and 10
import random


secret_number = random.randint(1, 10)

# Initialize guess variable
guess = None

# Repeat until the guess is correct
while guess != secret_number:
    # Ask the user's guess
    guess_str = input("Guess a number between 1 and 10: ")
    guess = int(guess_str)
    
    # Review user's guess
    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Correct!")