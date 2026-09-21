# ==============================================================================
# Task 5: Accepts a word from the user and reverse it
# ==============================================================================

print("\n--- Task 5: Reverse a Word ---")
word = input("Input a word to reverse :").strip()

# Reversing character by character using loop
reversed_word = ""
for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]
print(f"Reversed word: {reversed_word}")