# Reviewer Hashif

# Stack

class Stack:
    def __init__(self):
        self.stack=[]
    def push(self, item):
        self.stack.append(item)
        print(item, 'is pushed to stack')
    def pop(self):
        if len(self.stack)==0:
            print('Stack is empty')
        else:
            e=self.stack.pop()
            print(e, 'removed from stack')
    def display(self):
        if len(self.stack)==0:
            print('Stack is empty!')
        else:
            for i in self.stack:
                print(i)

s=Stack()
s.push(10)
s.push(20)
s.push(30)

s.pop()

s.display()


# Insertion sort

arr=[64, 34, 25, 12, 22, 11, 90]
def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_element=arr[i]
        pos=i
        while pos>0 and current_element<arr[pos-1]:
            arr[pos]=arr[pos-1]
            pos-=1
        arr[pos]=current_element
    return arr

print(insertion_sort(arr)) 

# Merge Sort

arr=[64, 34, 25, 12, 22, 11, 90]
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

merge_sort(arr)
print(arr)