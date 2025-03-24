STRENGTH
""""
Hanldes large input list
my_list = list(reversed(range(200000)))
print(insertion_sort_shifts(my_list))
// 19999900000


WEAKNESS
"""""""
It fails to hanlde duplicate cases.
arr = [1, 1, 1, 2, 2]
print(insertion_sort_shifts(arr))  # Output: 4 // wrong