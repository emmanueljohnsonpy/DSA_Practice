class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insertion
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    # Contains
    def contains(self, value):
        current = self.root
        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    # Delete
    def delete(self, value):
        def find_min(node):
            while node.left:
                node = node.left
            return node

        def delete_node(node, value):
            if not node:
                return None
            if value < node.value:
                node.left = delete_node(node.left, value)
            elif value > node.value:
                node.right = delete_node(node.right, value)
            else:
                # Node with only one child or no child
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                # Node with two children: Get the inorder successor
                temp = find_min(node.right)
                node.value = temp.value
                node.right = delete_node(node.right, temp.value)
            return node

        self.root = delete_node(self.root, value)

    # Inorder Traversal (Left → Node → Right)
    def inorder(self, node, result):
        if node:
            self.inorder(node.left, result)
            result.append(node.value)
            self.inorder(node.right, result)

    # Preorder Traversal (Node → Left → Right)
    def preorder(self, node, result):
        if node:
            result.append(node.value)
            self.preorder(node.left, result)
            self.preorder(node.right, result)

    # Postorder Traversal (Left → Right → Node)
    def postorder(self, node, result):
        if node:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(node.value)

# Example Usage
bst = BinarySearchTree()

# Insert values
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(12)
bst.insert(18)

# Check if a value exists
print("Contains 7:", bst.contains(7))  # True
print("Contains 20:", bst.contains(20))  # False

# Delete a value
bst.delete(15)

# Traversals
inorder_result = []
bst.inorder(bst.root, inorder_result)
print("Inorder Traversal:", inorder_result)

preorder_result = []
bst.preorder(bst.root, preorder_result)
print("Preorder Traversal:", preorder_result)

postorder_result = []
bst.postorder(bst.root, postorder_result)
print("Postorder Traversal:", postorder_result)
