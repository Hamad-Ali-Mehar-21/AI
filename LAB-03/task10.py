# ==============================================================================
# Task 10: Takes two digits m (row) and n (column) as input and generates 2D array
# The element value in i-th row and j-th column should be i*j
# Test Data : Rows = 3, Columns = 4
# Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
# ==============================================================================

print("\n--- Task 10: Generate Two-Dimensional Array (i * j) ---")
row_input = int(input("Input number of rows: ").strip())
col_input = int(input("Input number of columns: ").strip())
m = row_input
n = col_input
multi_list = [[i * j for j in range(n)] for i in range(m)]
print(f"Generated ({m} rows, {n} columns) Array:")
print(multi_list)


