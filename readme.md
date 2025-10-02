# Sorting Algorithms in Python

This repository contains implementations of several classic sorting algorithms in Python.  
The goal is to demonstrate how these algorithms work step by step, with readable code and comments.  

## 📌 Implemented Algorithms

### 1. Bubble Sort
- Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

### 2. Selection Sort
- Divides the list into a sorted and an unsorted part. Repeatedly selects the minimum element from the unsorted part and moves it to the sorted part.

### 3. Insertion Sort
- Builds the final sorted array one item at a time by comparing each new element with those already sorted and inserting it in the correct position.

### 4. Merge Sort
- A **divide-and-conquer** algorithm. Splits the array into halves, recursively sorts them, and then merges the sorted halves.

### 5. Quick Sort
- Another **divide-and-conquer** algorithm.  
- Picks a pivot, partitions the array into elements less than or equal to the pivot and elements greater than it, then recursively sorts the partitions.

---

## 🔧 Helper Functions

- **`swap(arr, idx1, idx2)`**  
  Swaps two elements in the array.  
- **`merge(arr1, arr2)`**  
  Used in Merge Sort to merge two sorted arrays.  

---

## 🚀 Example Usage

```python
arr = [64, 34, 25, 12, 22, 11, 90]

print(bubble_sort(arr))
print(selection_sort(arr))
print(insertion_sort(arr))
print(merge_sort(arr))
print(quick_sort(arr))
