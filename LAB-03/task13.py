# Task 13: Accepts a string and calculate the number of digits and letters
# Sample Data : Python 3.2
# Expected Output :
# Letters 6
# Digits 2
# ==============================================================================

print("\n--- Task 13: Calculate Number of Digits and Letters ---")

text = input(f"Enter a string: ")

letters = 0
digits = 0
for char in text:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
print("Letters", letters)
print("Digits", digits)