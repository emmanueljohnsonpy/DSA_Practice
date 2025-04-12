# Sorting Algorithms

## 1. Bubble Sort
**How it works:** Repeatedly swaps adjacent elements if they are in the wrong order.

**Time Complexity:**
- Best: O(n) (when already sorted)
- Average/Worst: O(n²)

**Stable:** Yes  
**In-place:** Yes  

**Example Logic:**
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
```

---

## 2. Insertion Sort
**How it works:** Builds the final sorted array one item at a time by inserting each element into its correct position.

**Time Complexity:**
- Best: O(n)
- Average/Worst: O(n²)

**Stable:** Yes  
**In-place:** Yes  

**Example Logic:**
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
```

---

## 3. Selection Sort
**How it works:** Selects the smallest (or largest) element from the unsorted portion and swaps it with the first unsorted element.

**Time Complexity:** O(n²) for all cases  
**Stable:** No  
**In-place:** Yes  

**Example Logic:**
```python
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < min_idx:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
```

---

## 4. Quick Sort
**How it works:** Uses a divide-and-conquer strategy. Picks a pivot, partitions the array into two halves, and recursively sorts them.

**Time Complexity:**
- Best/Average: O(n log n)
- Worst: O(n²) (if poor pivot choice)

**Stable:** No  
**In-place:** Yes  

**Example Logic:**
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```

---

## 5. Merge Sort
**How it works:** Also a divide-and-conquer algorithm. Divides the array into halves, recursively sorts them, and merges the sorted halves.

**Time Complexity:** O(n log n) in all cases  
**Stable:** Yes  
**In-place:** No (uses extra memory for merging)  

**Example Logic:**
```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
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
```
