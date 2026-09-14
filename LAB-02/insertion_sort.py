def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


nums=[12, -11, 67, 13, 5, 6,-78,-99,-2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = insertion_sort(nums)
print("Insertion Sort Result:", result)