import numpy as np
import algorithems


array = np.random.randint(0, 100, 100).tolist()

# Bubble sort
bubble_sort = algorithems.bubble_sort(array)

# Selection sort
selection_sort = algorithems.selection_sort(array)

# Insertion sort
insertion_sort = algorithems.insertion_sort(array)

# Merge sort
merge_sort = algorithems.merge_sort(array)

# Quick sort
quick_sort = algorithems.quick_sort(array)