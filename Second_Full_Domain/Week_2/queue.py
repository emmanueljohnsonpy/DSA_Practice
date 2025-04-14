from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
        
    def enqueue(self, item):
            self.queue.append(item)
            print(f"{item} enqueued to Queue.")
            
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            item = self.queue.popleft()
            print(f"{item} is dequeued from Queue")
            return item
    
    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("From front to back")
            for i in self.queue:
                print(i)
    
    def peek(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print(f"The Front element is {self.queue[0]}")
            return self.queue[0]
        
    def is_empty(self):
        return len(self.queue) == 0
    

q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

q.dequeue()
q.dequeue()

q.display()

q.peek()