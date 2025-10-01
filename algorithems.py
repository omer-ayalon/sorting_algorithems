def bubble_sort(arr, draw=None):
    arr_length = len(arr)
    for i in range(arr_length-1):
        for j in range(arr_length-i-1):
            if arr[j] > arr[j+1]:
                arr = swap(arr, j, j+1)
            if draw:
                draw(arr, j)
    return arr

def swap(arr, idx1, idx2):
    temp = arr[idx1]
    arr[idx1] = arr[idx2]
    arr[idx2] = temp
    return arr

