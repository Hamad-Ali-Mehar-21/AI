# ==============================================================================
# Task 11: Accepts a sequence of lines (blank line to terminate) -> lower case
# ==============================================================================
print("\n--- Task 11: Accept Sequence of Lines and Print in Lowercase ---")
print("Enter lines of text (Press Enter on an empty line to terminate):")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line.lower())
print("\nOutput (all characters in lower case):")
for line in lines:
    print(line)

    