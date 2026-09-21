print("\n--- Task 12: Comma Separated Binary Numbers Divisible by 5 ---")

user_input = input("Enter Comma Separated Binary Numbers ")
binary_items = user_input.split(",")

divisible_by_5 = []
for b in binary_items:
    try:
        val = int(b, 2)
        if val % 5 == 0:
            divisible_by_5.append(b)
    except ValueError:
        print(f"Skipping invalid binary number: {b}")
print("Result:", ",".join(divisible_by_5))