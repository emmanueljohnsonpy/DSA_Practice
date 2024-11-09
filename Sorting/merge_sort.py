

# Ascending order

""" def mergesort(list1):
    if len(list1)>1:
        mid=len(list1)//2
        left_list=list1[:mid]
        right_list=list1[mid:]
        mergesort(left_list)
        mergesort(right_list)
        i=0
        j=0
        k=0
        while i<len(left_list) and j<len(right_list):
            if left_list[i]<right_list[j]:
                list1[k]=left_list[i]
                i+=1
                k+=1
            else:
                list1[k]=right_list[j]
                j+=1
                k+=1
        while i<len(left_list):
            list1[k]=left_list[i]
            i+=1
            k+=1
        while j<len(right_list):
            list1[k]=right_list[j]
            j+=1
            k+=1

list1=[7, 5, 9, 3, 3, 0, 2, 1, 9, 5]
mergesort(list1)
print(list1)     """



def merge_sort(arr):
    if len(arr)>1:
        middle=len(arr)//2
        left_list=arr[:middle]
        right_list=arr[middle:]
        merge_sort(left_list)
        merge_sort(right_list)
        i=0
        j=0
        k=0
        while i<len(left_list) and j<len(right_list):
            if left_list[i]<right_list[j]:
                arr[k]=left_list[i]
                i+=1
                k+=1
            else:
                arr[k]=right_list[j]
                j+=1
                k+=1
        while i<len(left_list):
            arr[k]=left_list[i]
            i+=1
            k+=1
        while j<len(right_list):
            arr[k]=right_list[j]
            j+=1
            k+=1
    return arr
    

arr=[4,6,3,8,9,1,0]
merge_sort(arr)
print(arr)




def merge_sort(arr):
    if len(arr)>1:
        middle=len(arr)//2
        left_list=arr[:middle]
        right_list=arr[middle:]
        merge_sort(left_list)
        merge_sort(right_list)
        i=0
        j=0
        k=0
        while i<len(left_list) and j<len(right_list):
            if len(left_list[i])<len(right_list[j]):
                arr[k]=left_list[i]
                i+=1
                k+=1
            else:
                arr[k]=right_list[j]
                j+=1
                k+=1
        while i<len(left_list):
            arr[k]=left_list[i]
            i+=1
            k+=1
        while j<len(right_list):
            arr[k]=right_list[j]
            j+=1
            k+=1
    return arr

arr = ["apple", "banana", "kiwi", "fig", "grapefruit", "pear"]
merge_sort(arr)
print(arr)



































































































