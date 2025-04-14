class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"{item} is pushed to stack.")

    def pop(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            item = self.stack.pop()
            print(f"{item} is popped from stack.")
            return item
        
    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack from top to bottom")
            for i in reversed(self.stack):
                print(i)
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            print(f"Top element is {self.stack[-1]}")
            return self.stack[-1]
    
s = Stack()

s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

s.display()

s.pop()

s.display()

s.peek()




# Stack using Linked List



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None
        
    def push(self, data):
        newnode = Node(data)
        newnode.next = self.top
        self.top = newnode
        print(f"{data} is pushed to stack")
        
        
    def pop(self):
        if self.top is None:
            print("Stack is empty")
        else:
            item = self.top.data
            self.top = self.top.next
            print(f"{item} popped from stack")
    
    def display(self):
        if self.top is None:
            print("Stack is empty")
        else:
            current = self.top
            while current:
                print(current.data, end = " ")
                current = current.next
            print()
            
        
s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()

s.pop()
s.pop()
s.pop()
s.pop()

s.display()