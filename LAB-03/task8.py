# ==============================================================================
# Task 8: Prints all numbers from 0 to 6 except 3 and 6 using 'continue'
# Expected Output : 0 1 2 4 5
# ==============================================================================

print("\n--- Task 8: Print Numbers 0 to 6 Except 3 and 6 (using continue) ---")
for num in range(7):
    if num == 3 or num == 6:
        continue
    print(num, end=" ")
print()