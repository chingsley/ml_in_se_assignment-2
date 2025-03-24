STRENGTH 
"""""""
Generates a quick solution that can handle small input list



WEAKNESS
""""
Generates a non-optimized algorithm with complexity O(n^2) time,
that fails to handle very large list
my_list = list(reversed(range(200000)))
print(insertion_sort_shifts(my_list))
// Fails with ta timeout