import sys
import time
import random
import matplotlib.pyplot as plt

# Increase recursion limit for recursive selection sort
sys.setrecursionlimit(20000)

# Iterative Selection Sort
def selection_sort_iterative(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Recursive Selection Sort
def selection_sort_recursive(arr, start=0):
    n = len(arr)
    if start >= n - 1:
        return
    min_idx = start
    for i in range(start + 1, n):
        if arr[i] < arr[min_idx]:
            min_idx = i
    arr[start], arr[min_idx] = arr[min_idx], arr[start]
    selection_sort_recursive(arr, start + 1)


# Input sizes
sizes_iter = list(range(1, 10001, 500))   # 1, 501, 1001, ..., 10001
sizes_rec = list(range(1, 3001, 300))     # 1, 301, 601, ..., 3001

time_iterative = []
time_recursive = []

# Measure Iterative
for n in sizes_iter:
    arr = [random.randint(0, 10000) for _ in range(n)]
    start = time.time()
    selection_sort_iterative(arr)
    end = time.time()
    time_iterative.append(end - start)

# Measure Recursive
for n in sizes_rec:
    arr = [random.randint(0, 10000) for _ in range(n)]
    start = time.time()
    selection_sort_recursive(arr)
    end = time.time()
    time_recursive.append(end - start)


# Graph
plt.figure()
plt.plot(sizes_iter, time_iterative, label="Iterative Selection Sort")
plt.plot(sizes_rec, time_recursive, label="Recursive Selection Sort")
plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Runtime Comparison: Iterative vs Recursive Selection Sort")
plt.legend()
plt.grid(True)
plt.show()
