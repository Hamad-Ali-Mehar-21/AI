# Task 3: Guess a number between 1 to 9

# ==============================================================================

import random
print("\n--- Task 3: Number Guessing Game (1 to 9) ---")
target = random.randint(1, 9)
while True:
    try:
        guess = int(input("Guess a number between 1 to 9: "))
        if guess == target:
            print("Well guessed!")
            break
        else:
            print("Wrong guess! Try again.")
    except ValueError:
        print("Please enter a valid integer between 1 and 9.")
