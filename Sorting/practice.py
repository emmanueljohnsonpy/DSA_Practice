a=[4,6,3,8,9,1,0]
for j in range(len(a)-1):
    for i in range(len(a)-1-j):
        if a[i]>a[i+1]:
            a[i], a[i+1]=a[i+1], a[i]

a=[4,6,3,8,9,1,0]
for i in range(1, len(a)):
    current_element=a[i]
    pos=i
    while pos>0 and current_element<a[pos-1]:
        a[pos]=a[pos-1]
        pos-=1
    a[pos]=current_element

a=[4,6,3,8,9,1,0]
for i in range(len(a)-1):
    m=i
    for j in range(i+1, len(a)):
        if a[j]<a[m]:
            m=j
    if a[i]!=a[m]:
        a[i], a[m]=a[m], a[i]
    
a=[4,6,3,8,9,1,0]
def quick_sort(a):
    if len(a)<=1:
        return a
    pivot=a[len(a)//2]
    left=[i for i in a if i < pivot]
    middle=[i for i in a if i == pivot]
    right=[i for i in a if i > pivot]
    return quick_sort(left)+middle+quick_sort(right)

a=[4,6,3,8,9,1,0]
def merge_sort(a):
    if len(a)>1:
        middle=len(a)//2
        left_list=a[:middle]
        right_list=a[middle:]
        merge_sort(left_list)
        merge_sort(right_list)
        i=0
        j=0
        k=0
        while i<len(left_list) and j<len(right_list):
            if left_list[i]<right_list[j]:
                a[k]=left_list[i]
                i+=1
                k+=1
            else:
                a[k]=right_list[j]
                j+=1
                k+=1
        while i<len(left_list):
            a[k]=left_list[i]
            i+=1
            k+=1
        while j<len(right_list):
            a[k]=right_list[j]
            j+=1
            k+=1

merge_sort(a)
print(a)


