def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [5, 10, 15, 20, 25]
target = 20
print(linear_search(arr, target))