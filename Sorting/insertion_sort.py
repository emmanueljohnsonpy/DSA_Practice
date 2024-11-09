

# Ascending Order

def InsertionSort(my_list):
    for index in range(1, len(my_list)):
        current_element=my_list[index]
        pos=index
        while pos>0 and current_element>my_list[pos-1]:
            my_list[pos]=my_list[pos-1]
            pos-=1
        my_list[pos]=current_element

list1=[2, 4, 3, 5, 1]
InsertionSort(list1)
print(list1)


""" my_list=[4,3,6,8,2,1]
for i in range(1, len(my_list)):
    c=my_list[i]
    p=i
    while p>0 and c<my_list[p-1]:
        my_list[p]=my_list[p-1]
        p-=1
    my_list[p]=c

print(my_list)
 """


def InsertionSort(my_list):
    for index in range(1, len(my_list)):
        current_element = my_list[index]  
        pos = index
        
        while pos > 0 and len(current_element) < len(my_list[pos - 1]): 
            my_list[pos] = my_list[pos - 1]  
            pos -= 1
            
        my_list[pos] = current_element

list1 = ["apple", "banana", "pear", "kiwi", "grape"]
InsertionSort(list1)
print(list1) 


























































































































