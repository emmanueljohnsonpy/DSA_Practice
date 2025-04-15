
# Stack and Queue

## 🥞 Stack (LIFO - Last In, First Out)

Think of a **stack** like a pile of plates. You can:

- **Push**: Add a plate on top.
- **Pop**: Remove the plate from the top.

> 🧠 Last item added is the first one to be removed.

**Common operations (Python):**
```python
stack = []

# Push
stack.append(10)
stack.append(20)

# Pop
top = stack.pop()  # Removes 20
```

---

## 🚶 Queue (FIFO - First In, First Out)

Think of a **queue** like a line at a ticket counter. You can:

- **Enqueue**: Add a person to the end of the line.
- **Dequeue**: Remove the person from the front of the line.

> 🧠 First item added is the first one to be removed.

**Common operations (Python):**
```python
from collections import deque

queue = deque()

# Enqueue
queue.append(10)
queue.append(20)

# Dequeue
front = queue.popleft()  # Removes 10
```