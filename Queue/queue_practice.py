

# Queue implementation using list 


# append method and pop method for enqueue and dequeue operation
queue=[]
queue.append(10)
queue.append(20)
queue.append(30)
print(queue)
queue.pop(0)
print(queue)
queue.pop(0)
print(queue)
queue.pop(0)
print(queue) 

#another way
queue=[]
queue.insert(0, 10)
queue.insert(0, 20)
queue.insert(0, 30)
print(queue)
print(queue[0])
print(queue[-1])
queue.pop()
print(queue)
queue.pop()
print(queue)
queue.pop()
print(queue) 

# Enqueue and dequeue
queue=[]
def enqueue():
    e=int(input('Enter the element to add :- '))
    queue.append(e)
    print(e, 'is added to the queue')
def dequeue():
    if not queue:
        print('Queue is empty!')
    else:
        e=queue.pop(0)
        print(e, 'is removed from queue')
def display():
    print(queue)

while True:
    choice=int(input('Enter 1 for enqueue, 2 for dequeue, 3 for display, 4 for exit :- '))
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print('Enter valid number!') 


# Queue implementation using classes


import collections 
q=collections.deque()
print(q)
q.append(10)
q.append(20)
q.append(30)
print(q)
q.popleft()
print(q)

import collections
q=collections.deque()
print(q)
q.append(10)
q.append(20)
q.append(30)
print(q)
q.popleft()
print(q) 

import queue
q=queue.Queue()
q.put(10)
q.put(20)
q.put(30)
print(q)
print(q.get())
print(q.get())
print(q.get())
print(q.get(timeout=1)) 


# Priority Queue


# list, priority queue, heap queue module

# This is not best way to implement priority queue
q=[]
q.append(10)
q.append(5)
q.sort()
q.append(25)
q.sort()
q.pop(0)
q.pop(0)
q.pop(0)
print(q) 


# Priority queue
import queue
q=queue.PriorityQueue()
q.put(10)
q.put(40)
q.put(40)
q.put(65)
q.put(15)
q.put(50)
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get()) 


# Taking as tuple
q=[]
q.append((1, 'yoyo'))
q.append((2, 'yoyoyo'))
q.append((3, 'yo'))
q.sort(reverse=True)
print(q)
q.pop(0)
q.pop(0)
q.pop(0)
print(q) 





class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self, item):
        self.queue.append(item)
        print(item, 'enqueued to Queue')
    def dequeue(self):
        if len(self.queue)==0:
            print('Queue is empty!')
        else:
            item=self.queue.pop(0)
            print(item, 'is dequeued')
            return item
    def peek(self):
        if len(self.queue)==0:
            print('Queue is empty!')
        else:
            element=self.queue[0]
            print(element, 'is at the front')
    def display(self):
        if len(self.queue)==0:
            print('Queue is empty!')
        else:
            print('Queue from front to end:')
            for item in self.queue:
                print(item)
q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.peek()
q.display()























