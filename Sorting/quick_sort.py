

# Ascending and Descending order, First element as pivot


# to get the correct position of the pivot element
""" def pivot_place(list1, first, last):
    pivot=list1[first]
    left=first+1
    right=last
    while True:
        while left<=right and list1[left]<=pivot:
            left+=1
        while left<=right and list1[right]>=pivot:
            right-=1
        if right<left:
            break
        else:
            list1[left], list1[right]=list1[right], list1[left]
    list1[first], list1[right]=list1[right], list1[first]   
    return right

def quick_sort(list1, first, last):
    if first<last:
        p=pivot_place(list1, first, last)
        quick_sort(list1, first, p-1)
        quick_sort(list1, p+1, last)
    
#main
list1=[56, 26, 93, 17, 31, 44]
n=len(list1)
quick_sort(list1, 0, n-1)
print(list1)  """
# Ascending and Descending order, Last element as pivot


# to get the correct position of the pivot element
""" def pivot_place(list1, first, last):
    pivot=list1[last]
    left=first
    right=last-1
    while True:
        while left<=right and list1[left]<=pivot:
            left+=1
        while left<=right and list1[right]>=pivot:
            right-=1
        if right<left:
            break
        else:
            list1[left], list1[right]=list1[right], list1[left]
    list1[last], list1[left]=list1[left], list1[last]   
    return left

def quick_sort(list1, first, last):
    if first<last:
        p=pivot_place(list1, first, last)
        quick_sort(list1, first, p-1)
        quick_sort(list1, p+1, last)
    
#main
list1=[56, 26, 93, 17, 31, 44]
n=len(list1)      
quick_sort(list1, 0, n-1)
print(list1) """


# Ascending and Descending order, Random element as pivot


""" import random
# to get the correct position of the pivot element
def pivot_place(list1, first, last):
    rindex=random.randint(first, last)
    list1[rindex], list1[last]=list1[last], list1[rindex]
    pivot=list1[last]
    left=first
    right=last-1
    while True:
        while left<=right and list1[left]<=pivot:
            left+=1
        while left<=right and list1[right]>=pivot:
            right-=1
        if right<left:
            break
        else:
            list1[left], list1[right]=list1[right], list1[left]
    list1[last], list1[left]=list1[left], list1[last]   
    return left

def quick_sort(list1, first, last):
    if first<last:
        p=pivot_place(list1, first, last)
        quick_sort(list1, first, p-1)
        quick_sort(list1, p+1, last)
    
#main
list1=[56, 26, 93, 17, 31, 44]
n=len(list1)      
quick_sort(list1, 0, n-1)
print(list1) """


# Ascending and Descending order, Random element as pivot


""" import statistics
# to get the correct position of the pivot element
def pivot_place(list1, first, last):
    low=list1[first]
    high=list1[last]
    mid=(first+last)//2
    pivot_val=statistics.median([low, list1[mid], high])
    if pivot_val==low:
        pindex=first
    elif pivot_val==high:
        pindex=last 
    else:
        pindex=mid
    list1[last], list1[pindex]=list1[pindex], list1[last]
    pivot=list1[last]
    left=first
    right=last-1
    while True:
        while left<=right and list1[left]<=pivot:
            left+=1
        while left<=right and list1[right]>=pivot:
            right-=1
        if right<left:
            break
        else:
            list1[left], list1[right]=list1[right], list1[left]
    list1[last], list1[left]=list1[left], list1[last]   
    return left

def quick_sort(list1, first, last):
    if first<last:
        p=pivot_place(list1, first, last)
        quick_sort(list1, first, p-1)
        quick_sort(list1, p+1, last)
    
#main
list1=[56, 26, 93, 17, 31, 44]
n=len(list1)      
quick_sort(list1, 0, n-1)
print(list1) """




arr=[6, 4, 8, 3, 2]
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[len(arr)//2]
    left=[i for i in arr if i>pivot]
    middle=[i for i in arr if i==pivot]
    right=[i for i in arr if i<pivot]
    return quick_sort(left)+middle+quick_sort(right)

print(quick_sort(arr)) 




arr = ["apple", "banana", "kiwi", "fig", "grapefruit", "pear"]
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=len(arr[len(arr)//2])
    left=[i for i in arr if len(i)>pivot]
    middle=[i for i in arr if len(i)==pivot]
    right=[i for i in arr if len(i)<pivot]
    return quick_sort(left)+middle+quick_sort(right)

print(quick_sort(arr))