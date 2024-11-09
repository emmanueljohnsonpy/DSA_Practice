

# Target searching in list


arr=[4, 6, 8, 10, 15]
target=15
def search_index(arr, target):
    l=0
    u=len(arr)-1
    while l<=u:
        mid=(l+u)//2
        if arr[mid]==target:
            return mid
        else:
            if arr[mid]<target:
                l=mid+1
            else:
                u=mid-1
    return -1
print(search_index(arr, target)) 


# Find First Occurrence of Target


arr = [1, 2, 2, 2, 4, 6]
x = 2
def first_occurence(arr, x):
    l=0
    u=len(arr)-1
    res=-1
    while l<=u:
        m=(u+l)//2
        if arr[m]==x:
            res=m
            u=m-1
        else:
            if arr[m]<x:
                l=m+1
            else:
                u=m-1
    return res
print(first_occurence(arr,x)) 


# Find First Occurrence of Target


arr = [1, 2, 2, 2, 4, 6]
x = 2
def last_occurence(arr, x):
    l=0
    u=len(arr)-1
    res=-1
    while l<=u:
        m=(l+u)//2
        if arr[m]==x:
            res=m
            l=m+1
        else:
            if arr[m]<x:
                l=m+1
            else:
                u=m-1   
    return res
print(last_occurence(arr,x))

