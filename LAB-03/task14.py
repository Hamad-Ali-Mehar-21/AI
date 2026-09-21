print("\n--- Task 14: Check Password Validity ---")

password = input(f"Input your password : ")

if 6 <= len(password) <= 16:
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    special_characters = "$@#"

    for c in password:
        if c.islower():
            has_lower = True
        elif c.isupper():
            has_upper = True
        elif c.isdigit():
            has_digit = True
        elif c in special_characters:
            has_special = True

    if has_lower and has_upper and has_digit and has_special:
        print("Valid Password")
    else:
        print("Invalid Password")
else:
    print("Invalid Password: Length must be between 6 and 16 characters.")
