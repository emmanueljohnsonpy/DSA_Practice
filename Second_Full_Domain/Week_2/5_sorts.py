def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(bubble_sort([2, 1, 3, 4, 7, 1, 9, 5, 0, 1, 4, 2, 8, 6, 5]))



def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
    
print(insertion_sort([3, 5, 4, 1]))



def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_ind = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]
    return arr
    
print(selection_sort([6, 5, 7, 4, 8, 3, 9, 2, 0, 1]))



def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort([6, 5, 7, 4, 8, 3, 9, 2, 0, 1]))



def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[ : mid]
        R = arr[mid : ]
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
            k += 1
            i += 1
        while j < len(R):
            arr[k] = R[j]
            k += 1
            j += 1
    return arr
            
print(merge_sort([6, 5, 7, 4, 8, 3, 9, 2, 0, 1]))




