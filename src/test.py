def insertionSort(arr):
    n = len(arr)
    total_shifts = 0

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        shifts_in_insertion = 0

        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            shifts_in_insertion += 1

        total_shifts += shifts_in_insertion

    return total_shifts


# Example usage:
arr = [4, 3, 2, 1]
print(insertionSort(arr))  # Output: 4, wrong
