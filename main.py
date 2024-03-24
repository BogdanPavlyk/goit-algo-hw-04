import timeit
import random

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >=0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Testing the algorithms on different array sizes
array_sizes = [100, 1000, 5000]

for size in array_sizes:
    arr = [random.randint(1, 10000) for _ in range(size)]
    
    merge_time = timeit.timeit('merge_sort(arr.copy())', globals=globals(), number=10)
    print(f'Merge Sort {size} elements: {merge_time:.4f} seconds')

    insertion_time = timeit.timeit('insertion_sort(arr.copy())', globals=globals(), number=10)
    print(f'Insertion Sort {size} elements: {insertion_time:.4f} seconds')

    timsort_time = timeit.timeit('sorted(arr.copy())', globals=globals(), number=10)
    print(f'Timsort {size} elements: {timsort_time:.4f} seconds')
