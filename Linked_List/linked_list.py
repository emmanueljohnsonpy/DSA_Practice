

# Singly linked list


class Node:
    def __init__(self, data):
        self.data=data
        self.ref=None
class LinkedList:
    def __init__(self):
        self.head=None
    def print_LL(self):
        if self.head is None:
            print('linked list is empty')
        else:
            n=self.head
            while n is not None:
                print(n.data, '--->', end="  ")
                n=n.ref
    def add_at_begin(self, data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    def add_at_end(self, data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
    def add_after(self, data, x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n=n.ref
        if n is None:
            print('Node is not present in LL')
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
    def add_before(self, data, x):
        if self.head is None:
            print('linked list is empty')
            return
        if self.head.data==x:
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref
        if n.ref is None:
            print('Node not found!')
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
    def insert_empty(self, data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print('ll is not empty')
    def delete_begin(self):
        if self.head is None:
            print('Linked list is empty')
        else:
            self.head=self.head.ref
    def delete_end(self):
        if self.head is None:
            print('linked list is empty')
        elif self.head.ref == None:
            self.head=None
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None
    def delete_by_value(self, x):
        if self.head==None:
            print('linked list is empty')
            return
        if x==self.head.data:
            self.head=self.head.ref
            return
        n=self.head
        while n.ref is not None:
            if x==n.ref.data:
                break
            n=n.ref
        if n.ref is None:
            print('item not in this linked list')
        else:
            n.ref=n.ref.ref
    def array_to_ll(self, arr):
        for i in arr:
            LL1.add_at_end(i)
    def remove_duplicates(self):
        n = self.head
        while n.ref is not None:
            if n.data == n.ref.data:
                n.ref = n.ref.ref
            else:
                n = n.ref


LL1=LinkedList()
arr=[5, 8, 8, 9, 9, 9]
LL1.array_to_ll(arr)
LL1.remove_duplicates()
LL1.print_LL() 

# Doubly linked list


class Node:
    def __init__(self, data):
        self.data=data
        self.nref=None
        self.pref=None

class doublyLL:
    def __init__(self):
        self.head=None
    def print_LL(self):
        if self.head==None:
            print('linked list is empty')
        else:
            n=self.head
            while n is not None:
                print(n.data, '-->', end=" ")
                n=n.nref 
    def print_LL_reverse(self):
        print()
        if self.head == None:
            print('linked list is empty')
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data, '--->', end=" ")
                n=n.pref
    def insert_empty(self, data):
        if self.head==None:
            new_node=Node(data)
            self.head=new_node
        else:
            print('linked list is empty')
    def add_begin(self, data):
        newnode=Node(data)
        if self.head == None:
            self.head=newnode
        else:
            newnode.nref=self.head
            self.head.pref=newnode
            self.head=newnode
    def add_end(self, data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.nref=new_node
            new_node.pref=n
    def add_after(self, data, x):
        if self.head==None:
            print('linked list is empty')
        else:
            n=self.head
            while n is not None:
                if x==n.data:
                    break
                n=n.nref
            if n==None:
                print('entered element not found')
            else:
                new_node=Node(data)
                new_node.nref=n.nref
                new_node.pref=n
                if n.nref is not None:
                    n.nref.pref=new_node
                n.nref=new_node
    def add_before(self, data, x):
        if self.head==None:
            print('linked list is empty')
        else:
            n=self.head
            while n is not None:
                if x==n.data:
                    break
                n=n.nref
            if n==None:
                print('entered element not found')
            else:
                new_node=Node(data)
                new_node.nref=n
                new_node.pref=n.pref
                if n.pref is not None:
                    n.pref.nref=new_node
                else:
                    self.head=new_node
                n.pref=new_node
    def delete_begin(self):
        if self.head == None:
            print('linked list is empty')
            return
        if self.head.nref==None:
            self.head=None
        else:
            self.head=self.head.nref
            self.head.pref=None
    def delete_end(self):
        if self.head == None:
            print('linked list is empty')
            return
        if self.head.nref==None:
            self.head=None
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.pref.nref=None
    def delete_by_value(self, x):
        if self.head==None:
            print('linked list is empty')
            return
        if self.head.nref == None:
            if x==self.head.data:
                self.head=None
            else:
                print('element not found')
                return
        if self.head.data==x:
            self.head=self.head.nref
            self.head.pref=None
            return
        n=self.head
        while n.nref is not None:
            if x==n.data:
                break
            n=n.nref
        if n.nref is not None:
            n.nref.pref=n.pref
            n.pref.nref=n.nref
        else:
            if n.data==x:
                n.pref.nref=None
            else:
                print('element not found')
    def array_to_dll(self, arr):
        for i in arr:
            dd1.add_end(i)

dd1=doublyLL()
arr=[6,7,8,4,2,21]
dd1.array_to_dll(arr)
dd1.print_LL() 