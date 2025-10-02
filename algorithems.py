def bubble_sort(arr):
    arr_length = len(arr)
    for i in range(arr_length-1):       # loop for every element of the array
        for j in range(arr_length-i-1): # loop of the rest of the elements
            if arr[j] > arr[j+1]:       # swap element for a greater elements
                arr = swap(arr, j, j+1)
    return arr

def selection_sort(arr):
    arr_length = len(arr)
    for i in range(arr_length-1):
        min_idx = i                         # Assume the current position is the minimum
        for j in range(i+1, arr_length):    # look for the actual minimum in the rest of the array
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr = swap(arr, min_idx, i)         # swap the assumed minimum for the actual minimum
    return arr

def insertion_sort(arr):
    arr_length = len(arr)
    for i in range(1, arr_length):          # for every element in the array (exepct 0 where we assume it is sorted)
        j = i-1
        while j >= 0 and arr[i] < arr[j]:   # swap elements until the element arr[i] is in place in the sorted array
            arr = swap(arr, j+1, j)
            j -= 1
    return arr
       
def merge_sort(arr):
    arr_length = len(arr)
    if arr_length <= 1: return arr # return arr if can't split array

    mid_point = arr_length // 2

    # Split arr to left and right array
    left_arr = arr[0:mid_point]
    right_arr = arr[mid_point:arr_length]

    # Split the left and right array again
    arr1 = merge_sort(left_arr)
    arr2 = merge_sort(right_arr)

    return merge(arr1, arr2)

def merge(arr1, arr2):
    arr1_len = len(arr1)
    arr2_len = len(arr2)

    arr3 = []   # output array
    i=0         # index for arr1
    j=0         # index for arr2

    # merge arr1 to arr2 in order
    while i < arr1_len and j < arr2_len:
        if arr1[i] > arr2[j]:
            arr3.append(arr2[j])
            j += 1
        else:
            arr3.append(arr1[i])
            i += 1

    # if there are leftovers from arr1 merge to arr3
    while i < arr1_len:
        arr3.append(arr1[i])
        i += 1

    # if there are leftovers from arr2 merge to arr3
    while j < arr2_len:
        arr3.append(arr2[j])
        j += 1

    return arr3

def quick_sort(arr):
    return quick_sort_algo(arr, 0, len(arr)-1, 0)

def quick_sort_algo(arr, low, high, depth):
    len_arr = high - low
    if low >= high: return arr          # base case: subarray of size 0 or 1 is already sorted

    # --- choose pivot ---
    pivot_idx = low + len_arr // 2          # pick middle element as pivot
    arr = swap(arr, low+len_arr, pivot_idx) # move pivot to the end
    pivot_idx = high                        # pivot is now at the rightmost index

    # --- partition step ---
    i = low-1                               # Will track the boundary of elements smaller/equal to the pivot
    j = low                                 # Is the index we use to scan through the array
    while j < pivot_idx:                    # Partition step: move all elements <= pivot to the left side
        if arr[j] <= arr[pivot_idx]:        # If the current element is <= pivot, expand the "smaller zone"
            i += 1
            arr = swap(arr, i, j)           # Put arr[j] into the correct spot (swap with boundary)
        j += 1

    # place pivot in its final sorted position
    i += 1
    arr = swap(arr, i, pivot_idx)

   # --- recursive calls on left and right partitions ---
    arr = quick_sort_algo(arr, low, i-1, depth+1)
    arr = quick_sort_algo(arr, i+1, len_arr+low, depth+1)

    return arr

def swap(arr, idx1, idx2):

    temp = arr[idx1]
    arr[idx1] = arr[idx2]
    arr[idx2] = temp
    return arr
