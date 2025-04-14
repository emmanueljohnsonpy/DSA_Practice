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