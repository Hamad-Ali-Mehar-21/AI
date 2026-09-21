# ==============================================================================
# Task 9: Get the Fibonacci series between 0 to 50
# Expected Output : 1 1 2 3 5 8 13 21 34
# ==============================================================================
print("\n--- Task 9: Fibonacci Series between 0 to 50 ---")
x, y = 0, 1
while y < 50:
    print(y, end=" ")
    x, y = y, x + y
print()



# ==============================================================================
# Task 9 (Bonus/FizzBuzz): Iterates integers 1 to 50
# Multiples of 3 -> "Fizz", multiples of 5 -> "Buzz", both -> "FizzBuzz"
# ==============================================================================

print("\n--- Task (FizzBuzz): Integers from 1 to 50 ---")
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)