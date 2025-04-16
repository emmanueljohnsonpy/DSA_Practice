# Applications of Stack, Queue, and Hashtable

---

## 📚 1. Stack (LIFO - Last In, First Out)

### 🔁 Applications:
- **Function Call Stack**  
  Tracks function calls. When a function is called, it’s pushed to the stack; when it returns, it’s popped off.

- **Undo/Redo Functionality**  
  Text editors (like VS Code or MS Word) use stacks to keep track of changes.

- **Expression Evaluation & Conversion**  
  Used in compilers to evaluate **postfix**, **prefix**, or **infix** expressions.

- **Backtracking Algorithms**  
  E.g., maze solvers, Sudoku solvers, etc.

- **Browser History**  
  Go back (pop) and forward (push).

---

## 📥 2. Queue (FIFO - First In, First Out)

### 🚦 Applications:
- **Task Scheduling / CPU Scheduling**  
  OS uses queues to manage processes/tasks.

- **Print Queue**  
  First document sent to printer is the first to print.

- **Customer Service / Call Centers**  
  Customers are served in the order they arrive.

- **Breadth-First Search (BFS) in Graphs**  
  BFS uses a queue to explore nodes level by level.

- **Messaging Systems**  
  Message queues are used in asynchronous systems (e.g., RabbitMQ, Kafka).

---

## 🔐 3. Hashtable (Key-Value Store)

### 🚀 Applications:
- **Database Indexing**  
  Fast lookup of data using keys (like primary keys in SQL).

- **Caching**  
  Store recently used data (e.g., browser cache, memcached).

- **Symbol Tables in Compilers**  
  Keeps track of variable names and scopes.

- **Counting Frequencies**  
  E.g., word frequency in a document.

- **Password Storage (with hashing + salt)**  
  Hash functions (not directly hashtable, but conceptually similar).

- **Dictionaries in Programming Languages**  
  Built-in data structures like `dict` in Python, `Map` in Java, etc.