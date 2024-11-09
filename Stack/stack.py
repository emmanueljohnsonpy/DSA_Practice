

# Sample Stack 


stack=[]
def push():
    if len(stack)==n:
        print('List is full!')
    else:
        element=int(input('Enter the element : '))
        stack.append(element)
        print(stack)

def pop_element():
    if not stack:
        print('Stack is empty!')
    else:
        e=stack.pop()
        print('Removed element :', e)
        print(stack)    

n=int(input('Enter the limit of stack :- '))
while True:
    choice=int(input('Enter 1 for push, 2 for pop, 3 for quit :- '))
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    else:
        print('Enter Correct Number') 

# Implement stack using collections and queue module


import collections
stack = collections.deque()
print(stack)
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)
stack.rotate(2)
print(stack)
stack.pop()
stack.pop()
print(stack)
stack.appendleft(50)
stack.appendleft(60)
print(stack)
stack.popleft()
stack.popleft()
print(stack)

import queue 
stack=queue.LifoQueue()
print(stack)
stack.put(10)
stack.put(20)
stack.put(30, timeout=1)
print(stack.get())
print(stack.get())
print(stack.get())
print(stack.get(timeout=1)) 


# NeetCode



def isValid(s):
    stack=[]
    closeToOpen={')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in closeToOpen:
            if stack and stack[-1]==closeToOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return False if stack else True

s="({[]})"
print(isValid(s))  
        



class Stack:
    def __init__(self):
        self.stack=[]
    def push(self, item):
        self.stack.append(item)
        print(item, 'is added to the stack')
    def peek(self):
        if not self.is_empty():
            element=self.stack[-1]
            print(element, 'is at top of the stack')
        else:
            print('Stack is empty')
    def pop(self):
        if len(self.stack)==0:
            print('Stack is empty!')
        else:
            item=self.stack.pop()
            print(item, 'is removed from stack')
            return item
    def display(self):
        if len(self.stack)==0:
            print('Stack is empty!')
        else:
            print('Stack elements from top to bottom:')
            for item in reversed(self.stack):
                print(item)
    def is_empty(self):
        return len(self.stack)==0
                
s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.pop()
s.display()