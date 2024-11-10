
# Reviewer : Emil IS


# create linked list , add, traverse, remove duplicates mine is for sorted but he asked for unsorted

class Node:
    def __init__(self, data):
        self.data=data
        self.ref=None

class LinkedList:
    def __init__(self):
        self.head=None
    def print_LL(self):
        if self.head==None:
            print('linked list is empty')
        else:
            n=self.head
            while n is not None:
                print(n.data, '--->', end=" ")
                n=n.ref
    def add_begin(self, data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    def remove_duplicates(self):
        n=self.head
        while n.ref is not None:
            if n.data==n.ref.data:
                n.ref=n.ref.ref
            else:
                n=n.ref
    
LL=LinkedList()
LL.add_begin(10)
LL.add_begin(20)
LL.add_begin(20)
LL.add_begin(30)
LL.add_begin(20)
LL.remove_duplicates()
LL.print_LL()

# Do fibanocci in any way 

def fibanocci(n):
    res=[0, 1]
    for i in range(2, n+1):
        end=res[-1]+res[-2]
        res.append(end)
    return res

print(fibanocci(6)) 

# Mine is wrong, The output must be in list of fibanoocci series

def fibanocci(n):

    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibanocci(n-1) + fibanocci(n-2)

n=6
res=fibanocci(n)
print(res) 

# Return the longest substring that not contains vowels

s="orange"

def find_largest_substring(s):
    c=""
    vowels=['a', 'e', 'i', 'o', 'u']
    for i in range(len(s)):
        if s[i] not in vowels:
            c+=s[i]
        else:
            c+=" "
    res=c.split()
    # print(res)
    m=res[0]
    for i in res:
        if len(i)>len(m):
            m=i
    return m

print(find_largest_substring(s))
