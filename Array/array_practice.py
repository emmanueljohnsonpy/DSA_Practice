myarray=[85,47,63,55,68,71]
def myfunc(myarray):
    min=myarray[0]
    max=myarray[0]
    for i in myarray:
        if i>max:
            max=i
        if i<min:
            min=i
    return print('maximum :',max,'\n''minimum :',min)
myfunc(myarray)



arr=[85,47,63,55,68,71]
left=0
right=len(arr)-1
while left<right:
    arr[left], arr[right]=arr[right], arr[left]
    left+=1
    right-=1
print(arr)



arr=[85,47,63,55,68,71]
def sum_of_elements(arr):
    total=0
    for i in arr:
        total+=i
    return total
res=sum_of_elements(arr)
print(res)



arr = [1, 1, 2, 2, 3, 4, 4, 5]
def remove_dup(arr):
    index=0
    for i in range(1, len(arr)):
        if arr[index]!=arr[i]:
            index+=1
            arr[index]=arr[i]
    return index + 1
result=remove_dup(arr)
print('length:', result)
print('new array:', arr[:result])



arr=[1, 2, 3, 4, 5]
k=2
k=k%len(arr)
arr.reverse()
arr[:k]=reversed(arr[:k])
arr[k:]=reversed(arr[k:])
print(arr)
