def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left_list=arr[:mid]
        right_list=arr[mid:]
        merge_sort(left_list)
        merge_sort(right_list)
        i=0
        j=0
        k=0
        while i<len(left_list) and j<len(right_list):
            if left_list[i]>right_list[j]:
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

arr=[6, 4, 9, 3, 0, 1, 2]
merge_sort(arr)
print(arr)