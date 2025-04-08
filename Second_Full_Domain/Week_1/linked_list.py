class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_begin(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode
        
    def insert_at_end(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newnode
    
    def display(self):
        if self.head is None:
            print("Linked List is empty")
            return
        current = self.head
        while current:
            print(current.data, "-->", end = " ")
            current = current.next
        print("None")
    
    def array_to_linked_list(self, arr):
        for i in arr:
            self.insert_at_end(i)
    
    def delete_by_value(self, value):
        if self.head is None:
            print("Linked List is empty")
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != value:
            current = current.next
        if current.next is None:
            print("Value Not Found")
            return
        current.next = current.next.next
        
    def insert_after_value(self, x, data):
        if self.head is None:
            print("Linked list is empty")
            return
        current = self.head
        while current:
            if current.data == x:
                newnode = Node(data)
                newnode.next = current.next
                current.next = newnode
                return
            current = current.next
        print("Value is not Found")
        
    def insert_before_value(self, x, data):
        if self.head is None:
            print("Linked List is empty")
            return
        if self.head.data == x:
            self.insert_at_begin(data)
            return
        current = self.head
        while current.next and current.next.data != x:
            current = current.next
        if current.next is None:
            print("Value Not Found")
            return
        newnode = Node(data)
        newnode.next = current.next
        current.next = newnode
        
    def display_reverse(self):
        def _reverse(node):
            if node is None:
                return
            _reverse(node.next)
            print(f"{node.data} -->", end = " ")
            
        if self.head is None:
            print("Linked List is empty")
            return
        _reverse(self.head)
        print("None")
        
    def display_reverse_iterative(self):
        stack = []
        current = self.head
        while current:
            stack.append(current.data)
            current = current.next
        while stack:
            print(stack.pop(), end = " --> ")
        print("None")
    
    def remove_duplicates_sorted(self):
        if self.head is None:
            print("Linked LIst is empty")
            return
        current = self.head
        while current and current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
            
    
ssl = SinglyLinkedList()
ssl.insert_at_end(10)
ssl.insert_at_end(20)
ssl.insert_at_end(20)
ssl.insert_at_end(20)
ssl.insert_at_end(30)
ssl.display()

ssl.remove_duplicates_sorted()
ssl.display()

















