import random
import time
import matplotlib.pyplot as plt

# ITERATIVE INVERSION COUNT
# Time Complexity: O(n^2)
def count_inversions_iterative(arr):
    n = len(arr)
    inversions = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inversions += 1
    return inversions

# RECURSIVE INVERSION COUNT
# Divide and Conquer Approach
# Time Complexity: O(n log n)
def count_inversions_recursive(arr):
    _, inv_count = merge_sort_and_count(arr)
    return inv_count
def merge_sort_and_count(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, left_inv = merge_sort_and_count(arr[:mid])
    right, right_inv = merge_sort_and_count(arr[mid:])
    merged, split_inv = merge_and_count(left, right)
    return merged, left_inv + right_inv + split_inv
def merge_and_count(left, right):
    i = j = inv_count = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv_count += len(left) - i
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inv_count


# PERFORMANCE TESTING
input_sizes = [1, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
iter_times = []
rec_times = []

for n in input_sizes:
    arr = [random.randint(1, n) for _ in range(n)]
    # Iterative timing
    start = time.perf_counter()
    count_inversions_iterative(arr.copy())
    end = time.perf_counter()
    iter_times.append(end - start)
    # Recursive timing
    start = time.perf_counter()
    count_inversions_recursive(arr.copy())
    end = time.perf_counter()
    rec_times.append(end - start)
    print(f"n={n} | Iterative: {iter_times[-1]:.6f}s | Recursive: {rec_times[-1]:.6f}s")


# GRAPH PLOTTING
plt.plot(input_sizes, iter_times, label="Iterative Algorithm")
plt.plot(input_sizes, rec_times, label="Recursive Algorithm")
plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Iterative vs Recursive Inversion Count Performance")
plt.legend()
plt.grid(True)
plt.show()
