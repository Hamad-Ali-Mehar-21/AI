# ==============================================================================
# Task 2: Convert temperatures to and from Celsius, Fahrenheit
# Formula: c/5 = f-32/9 => c = (f-32)*5/9, f = (c*9/5) + 32
# Expected Output:
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius
# ==============================================================================
print("\n--- Task 2: Temperature Conversion ---")

# celsius = 60
# fahrenheit = int(round((celsius * 9 / 5) + 32))
# print(f"{celsius}°C is {fahrenheit} in Fahrenheit")
# fahrenheit_val = 45
# celsius_val = int(round((fahrenheit_val - 32) * 5 / 9))
# print(f"{fahrenheit_val}°F is {celsius_val} in Celsius")

user_val = input("\nEnter temperature to convert (e.g., 60C, 45F) [Press Enter to skip]: ")
if user_val:
    unit = user_val[-1].upper()
    val = float(user_val[:-1])
    if unit == "C":
        res = int(round((val * 9 / 5) + 32))
        print(f"{int(val) if val.is_integer() else val}°C is {res} in Fahrenheit")
    elif unit == "F":
        res = int(round((val - 32) * 5 / 9))
        print(f"{int(val) if val.is_integer() else val}°F is {res} in Celsius")
    else:
        print("Invalid unit! Please enter with 'C' or 'F' (e.g. 100C or 212F).")