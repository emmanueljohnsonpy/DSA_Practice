# 🧠 Hash Tables: Key Concepts

## 🔹 What is a Hash Table?

A **Hash Table** is a data structure that allows you to **store key-value pairs** and quickly retrieve values using their keys.

Think of it like a super-fast, super-organized locker system:
- You put your item (`value`) in a locker (`bucket`)
- The key to open that locker is generated using a formula (`hash function`)
- To get your item later, just use the same key!

---

## ⚙️ Core Concepts

### 1. **Hash Function**
- Converts your key into an **index**.
- Should be:
  - Fast
  - Consistent
  - Evenly distribute keys

### 2. **Buckets**
- The array where the values are stored.

### 3. **Collisions**
- When two keys hash to the **same index**.
- Solutions:
  - **Chaining**
  - **Open Addressing** (Linear/Quadratic Probing)

### 4. **Load Factor**
- `load_factor = number_of_items / number_of_buckets`
- If too high, the table **resizes**.

---

## 🧪 Common Operations

| Operation       | Average Time | Description                      |
|----------------|--------------|----------------------------------|
| Insert (Put)   | O(1)         | Add a key-value pair             |
| Search (Get)   | O(1)         | Find a value using a key         |
| Delete (Remove)| O(1)         | Remove a key-value pair          |

---

## 📦 Example in Python

```python
hash_table = {}

# Insert
hash_table["name"] = "Emmanuel"
hash_table["age"] = 25

# Retrieve
print(hash_table["name"])  # Emmanuel

# Delete
del hash_table["age"]
```

---

## 🔁 Linear Probing

### 🧠 Idea:
If a collision happens, **move one step at a time** to find an empty slot.

```text
new_index = (original_index + i) % table_size
```

### Pros:
- Simple

### Cons:
- **Primary Clustering** risk

---

## 🧮 Quadratic Probing

### 🧠 Idea:
Increase gap quadratically on collision.

```text
new_index = (original_index + i^2) % table_size
```

### Pros:
- Less clustering than linear

### Cons:
- **Secondary Clustering**

---

## 🧠 What is Clustering?

### 🔸 Clustering
Happens when keys are placed too close to each other in the hash table.

---

### 1️⃣ Primary Clustering (Linear Probing Problem)
- Long runs of filled slots
- Slows future insertions

### 2️⃣ Secondary Clustering (Quadratic Probing Problem)
- Keys with same initial index follow same probe sequence

---

## 🚀 How to Avoid Clustering?

- ✅ Quadratic Probing (partial fix)
- ✅ Double Hashing (best)
- ✅ Separate Chaining (linked lists)

---