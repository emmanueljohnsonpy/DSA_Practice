# Construction of Singly linked list & Doubly linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def add_at_beginning(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def add_at_end(self, data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newnode
    
    def convert_array_to_linked_list(self, arr):
        for item in arr:
            self.add_at_end(item)

    def print_in_order(self):
        if not self.head:
            print("linked list is empty")
            return
        current = self.head
        while current:
            print(current.data, end = " -> ")
            current = current.next
        print("None")

    def print_in_reverse_order(self, node = None):
        if node is None:
            node = self.head
            if not self.head:
                print("linked list is empty")
                return
        if node.next:
            self.print_in_reverse_order(node.next)
        print(node.data, end = " -> ")

    def delete_node(self, value):
        if not self.head:
            print("Linked List is empty")
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next
        print("value not found")

    def insert_after(self, target, data):
        current = self.head
        while current:
            if current.data == target:
                newnode = Node(data)
                newnode.next = current.next
                current.next = newnode
                return
            current = current.next
    
    def insert_before(self, target, data):
        if not self.head:
            print("Linked List is empty")
            return
        if self.head.data == target:
            self.add_at_beginning(data)
            return
        current = self.head
        while current.next:
            if current.next.data == target:
                newnode = Node(data)
                newnode.next = current.next
                current.next = newnode
                return
            current = current.next

    def remove_duplicates(self):
        if not self.head:
            print("Linked List is empty")
            return
        current = self.head
        while current and current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
        


    
sll = SinglyLinkedList()
# sll.add_at_beginning(10)
# sll.add_at_beginning(5)
# sll.add_at_end(15)
arr = [1, 2, 3, 3, 4, 5, 5, 5]
sll.convert_array_to_linked_list(arr)
sll.delete_node(3)
sll.delete_node(4)
sll.insert_after(2, 20)
sll.insert_before(5, 25)
sll.remove_duplicates()
sll.print_in_order()
# sll.print_in_reverse_order()
print("None")