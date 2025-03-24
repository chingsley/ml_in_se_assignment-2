# def insertion_sort_shifts(arr):
#     shifts = 0  # Initialize the shift counter
#     for i in range(1, len(arr)):
#         key = arr[i]  # Current element to be inserted
#         j = i - 1
#         # Move elements of arr[0..i-1] that are greater than key to one position ahead
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             shifts += 1
#             j -= 1
#         arr[j + 1] = key
#     return shifts

import bisect


def insertion_sort_shifts(arr):
    shifts = 0
    sorted_list = []

    for num in arr:
        pos = bisect.bisect_left(sorted_list, num)
        shifts += len(sorted_list) - pos
        bisect.insort(sorted_list, num)

    return shifts


# Example usage:
arr = [1, 1, 1, 2, 2]
print(insertion_sort_shifts(arr))  # Output: 4, wrong
