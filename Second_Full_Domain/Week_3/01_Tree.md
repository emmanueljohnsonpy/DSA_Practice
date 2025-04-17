
# Concepts of Tree

## 🌳 Tree - Basic Definition
A **tree** is a hierarchical data structure that consists of **nodes**, with a topmost node called the **root**. Each node can have **zero or more child nodes**, and each child node has **only one parent** (except the root, which has no parent).

---

## 🧱 Basic Terminology

| Term | Description |
|------|-------------|
| **Node** | A single element in the tree. |
| **Root** | The topmost node in a tree. |
| **Parent** | A node that has one or more children. |
| **Child** | A node that descends from another node (its parent). |
| **Leaf** | A node that has no children. |
| **Edge** | The connection between one node and another. |
| **Subtree** | Any node and its descendants form a subtree. |
| **Depth** | Number of edges from the root to the node. |
| **Height** | Number of edges from a node to its deepest leaf. |
| **Level** | Distance from the root (root is level 0). |
| **Degree** | The number of children a node has. |

---

## 🌲 Types of Trees

1. **Binary Tree**  
   - Each node has at most **2 children** (left and right).
   
2. **Binary Search Tree (BST)**  
   - Left child < Parent < Right child (used for efficient searching).

3. **Balanced Tree (like AVL, Red-Black Tree)**  
   - Keeps tree height balanced for optimal performance.

4. **N-ary Tree**  
   - A tree where nodes can have **N children**.

5. **Complete Binary Tree**  
   - All levels are fully filled except the last, and it's filled left to right.

6. **Full Binary Tree**  
   - Every node has **0 or 2 children**.

7. **Perfect Binary Tree**  
   - All internal nodes have 2 children and all leaves are at the same level.

8. **Trie (Prefix Tree)**  
   - Used for storing words efficiently (like in a dictionary).

9. **Heap Tree**  
   - A binary tree used in heap data structures (max-heap/min-heap).

---

## 🔁 Common Operations on Trees

- **Traversal**
  - **Inorder (Left → Root → Right)**  
  - **Preorder (Root → Left → Right)**  
  - **Postorder (Left → Right → Root)**  
  - **Level-order (BFS)**

- **Insertion/Deletion**
- **Searching**
- **Finding height, depth, number of nodes, leaves, etc.**

---

## 📌 Use Cases of Trees

- File systems
- HTML/XML parsers (DOM tree)
- AI (game trees, decision trees)
- Database indexes (B-Trees)
- Networking (routing trees)
- Compiler design (syntax trees)


## 🌳 Overview of Trees

A **tree** is a hierarchical data structure consisting of **nodes** connected by **edges**. It starts with a **root node** at the top, and the nodes below it are connected in a **parent-child relationship**. Each node can have **zero or more children**.

### Key Characteristics of a Tree

- **Root**: The topmost node, which has no parent.
- **Parent and Child**: Nodes are connected such that each node (except the root) has one parent and potentially multiple children.
- **Leaf**: A node with no children is called a leaf node.
- **Subtree**: Any node and all its descendants form a subtree.

### Types of Trees

1. **Binary Tree**: Each node has at most **2 children** (left and right).
2. **Binary Search Tree (BST)**: A binary tree where nodes follow the rule:  
    **Left child < Parent < Right child**, making searches efficient.
3. **Balanced Tree**: A tree where the height difference between left and right subtrees is minimal, ensuring fast operations.

### Applications of Trees

- **File Systems**: Directories are structured as trees.
- **Search Algorithms**: Binary search trees enable quick lookups.
- **Databases**: B-trees are used for indexing.
- **AI**: Decision trees assist in decision-making.

### Tree Metrics

- **Height**: The length of the longest path from the root to a leaf.
- **Depth**: The number of edges from the root to a specific node.
