# Construction of Singly linked list & Doubly linked list.


""" class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_beginning(self, data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head = newnode
    
    def insert_at_end(self, data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode
    
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end = " -> ")
            current = current.next
        print("None")

    def array_to_linkedlist(self, arr):
        for item in arr:
            self.insert_at_end(item)
        return self.head

sll = SinglyLinkedList()
arr = [1, 2, 3, 4, 5]
result = sll.array_to_linkedlist(arr)
sll.traverse()
print(result) """


