# ==============================================================================
# Task 7: Prints each item and its corresponding type from the following list
# Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
# ==============================================================================

print("\n--- Task 7: Print Each Item and its Type ---")
datalist = [1452, 11.23, 1 + 2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]
for item in datalist:
    print(f"Item: {str(item)} | Type: {type(item)}")