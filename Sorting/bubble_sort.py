

# Sorting in ascending order


list1=[5, 4, 3, 7, 8, 9, 1, 2]
for j in range(len(list1)-1):
    for i in range(len(list1)-1-j):
        if list1[i]>list1[i+1]:
            list1[i], list1[i+1]=list1[i+1], list1[i]
print(list1)


def bubble_sort_by_length(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if len(arr[j]) > len(arr[j+1]):  
                arr[j], arr[j+1] = arr[j+1], arr[j]  
    

# Example usage
strings = ["apple", "banana", "pear", "kiwi", "grape"]
bubble_sort_by_length(strings)
print(strings) 

""" a=[5, 4, 3, 7, 8, 9, 1, 2]
for j in range(len(a)-1):
    for i in range(len(a)-1-j):
        if a[i]<a[i+1]:
            a[i], a[i+1]=a[i+1], a[i]
    
print(a) """





























































































































