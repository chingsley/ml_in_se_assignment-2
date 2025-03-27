# def insertionSort(arr):
#     n = len(arr)
#     total_shifts = 0

#     for i in range(1, n):
#         key = arr[i]
#         j = i - 1
#         shifts_in_insertion = 0

#         # Move elements of arr[0..i-1], that are greater than key,
#         # to one position ahead of their current position
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
#             shifts_in_insertion += 1

#         total_shifts += shifts_in_insertion

#     return total_shifts


# # Example usage:
# arr = [4, 3, 2, 1]
# print(insertionSort(arr))  # Output: 4, wrong


def update_smallest_range(smallest: list, new_range: tuple):
    curr_length = smallest[1] - smallest[0]
    new_length = new_range[1] - new_range[0]
    if new_length < curr_length:
        smallest[0], smallest[1] = new_range[0], new_range[1]


def string_to_hash(s: str) -> dict:
    hash_map = {}
    for ch in s:
        hash_map[ch] = hash_map.get(ch, 0) + 1
    return hash_map


def expand_window(big_string, right_idx, window_counts, target_counts, k):
    while k < len(target_counts) and right_idx < len(big_string):
        ch = big_string[right_idx]
        if ch in target_counts:
            window_counts[ch] = window_counts.get(ch, 0) + 1
            if window_counts[ch] == target_counts[ch]:
                k += 1
        right_idx += 1
    return right_idx, k


def contract_window(
    big_string, left_idx, right_idx, window_counts, target_counts, k, smallest
):
    while k == len(target_counts) and left_idx <= right_idx:
        if big_string[left_idx] in window_counts:
            update_smallest_range(smallest, (left_idx, right_idx - 1))
            window_counts[big_string[left_idx]] -= 1
            if (
                window_counts[big_string[left_idx]]
                < target_counts[big_string[left_idx]]
            ):
                k -= 1
        left_idx += 1
    return left_idx, k


def smallest_substring_containing(big_string: str, small_string: str) -> str:
    target_counts, window_counts = string_to_hash(small_string), {}
    smallest, left_idx, right_idx, k = [-float("inf"), 0], 0, 0, 0

    while right_idx < len(big_string):
        right_idx, k = expand_window(
            big_string, right_idx, window_counts, target_counts, k
        )
        left_idx, k = contract_window(
            big_string, left_idx, right_idx, window_counts, target_counts, k, smallest
        )

    return big_string[smallest[0] : smallest[1] + 1] if smallest[0] >= 0 else ""


# Test cases (should match TypeScript behavior)
if __name__ == "__main__":
    # Original TypeScript test equivalents
    print(
        "Test 1:", smallest_substring_containing("abcd$ef$axb$c$", "$$abf")
    )  # "f$axb$"
    print("Test 2:", smallest_substring_containing("abcdef", "xyz"))  # ""
    print("Test 3:", smallest_substring_containing("abc", "abc"))  # "abc"
    print("Test 4:", smallest_substring_containing("ADOBECODEBANC", "ABC"))  # "BANC"
    print("Test 5:", smallest_substring_containing("a", "a"))  # "a"
