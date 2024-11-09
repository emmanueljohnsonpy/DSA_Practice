

# Sorting for non duplicate values using built in methods


arr=[5, 3, 12, 15, 17, 0]
for i in range(len(arr)):
    min_val=min(arr[i:])
    ind_min=arr.index(min_val)
    arr[i], arr[ind_min]=arr[ind_min], arr[i]

print(arr) 


# Sorting for duplicate values using built in methods


arr=[5, 0, 2, 2, 6, 0]
for i in range(len(arr)-1):
    min_val=min(arr[i:])
    ind_min=arr.index(min_val, i)
    if arr[i] != arr[ind_min]:
        arr[i], arr[ind_min]=arr[ind_min], arr[i]

print(arr)


# Sorting without built in methods


arr=[5, 0, 2, 2, 6, 0]
for i in range(len(arr)-1):
    m_ind=i
    for j in range(i+1, len(arr)):
        if arr[j]>arr[m_ind]:
            m_ind=j
    if arr[i]!=arr[m_ind]:
        arr[i], arr[m_ind]=arr[m_ind], arr[i]
print(arr) 



a=[5, 4, 3, 2, 7, 8, 6]
for i in range (len(a)-1):
    m=i
    for j in range(i+1, len(a)):
        if a[j]<a[m]:
            m=j
    if a[i]!=a[m]:
        a[i], a[m]=a[m], a[i]
print(a)




arr = ["apple", "banana", "pear", "kiwi", "grape"]
for i in range(len(arr)-1):
    m_ind=i
    for j in range(i+1, len(arr)):
        if len(arr[j])<len(arr[m_ind]):
            m_ind=j
    if arr[i]!=arr[m_ind]:
        arr[i], arr[m_ind]=arr[m_ind], arr[i]
print(arr)

