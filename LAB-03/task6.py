# ==============================================================================
# Task 6: Count the number of even and odd numbers from a series of numbers
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Expected Output :
# Number of even numbers : 4 (or 5 depending on sample)
# Number of odd numbers : 5
# ==============================================================================

print("\n--- Task 6: Count Even and Odd Numbers ---")
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Sample numbers : numbers = {numbers}")
print(f"Number of even numbers : {even_count}")
print(f"Number of odd numbers : {odd_count}")