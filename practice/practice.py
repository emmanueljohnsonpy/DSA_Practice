

# Create a Binary Search Tree with insertion, contains, delete, three traversals (postorder, preorder, in order).


class Node:
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self):
        self.root=None
    
    def insert(self, value):
        newnode=Node(value)
        if self.root is None:
            self.root=newnode
            return
        current=self.root
        while True:                                # Now this is for no duplicates in standard BST dup is not allowed (value==current.value)
            if value<current.value:                # dup to left use <= and don't use elif use else   
                if current.left is None:
                    current.left=newnode
                    return
                current=current.left
            elif value>current.value:              # dup to right use >= (else)
                if current.right is None:
                    current.right=newnode
                    return
                current=current.right
            else:
                return
    
    def contains(self, value):              # Iterative approach
        current=self.root
        while current:
            if value==current.value:
                return True
            elif value<current.value:
                current=current.left
            else:
                current=current.right
        return False

    def delete(self, value):
        def find_min(node):
            while node.left:
                node=node.left
            return node
        
        def delete_node(node, value):
            if not node:
                return None
            if value<node.value:
                node.left=delete_node(node.left, value)
            elif value>node.value:
                node.right=delete_node(node.right, value)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                
                temp=find_min(node.right)
                node.value=temp.value
                node.right=delete_node(node.right, temp.value)
            return node
        self.root=delete_node(self.root, value)

    def inorder(self, node, result):
        if node:
            self.inorder(node.left, result)
            result.append(node.value)
            self.inorder(node.right, result)
    
    def preorder(self, node, result):
        if node:
            result.append(node.value)
            self.preorder(node.left, result)
            self.preorder(node.right, result)
    
    def postorder(self, node, result):
        if node:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(node.value)

bst=BinarySearchTree()

bst.insert(10)
bst.insert(20)
bst.insert(30)
bst.insert(40)
bst.insert(50)

print("Contains 10 :", bst.contains(10))
print("Contains 60 :", bst.contains(60))

inorder_result = []
bst.inorder(bst.root, inorder_result)
print("Inorder Traversal:", inorder_result)

preorder_result = []
bst.preorder(bst.root, preorder_result)
print("Preorder Traversal:", preorder_result)

postorder_result = []
bst.postorder(bst.root, postorder_result)
print(postorder_result)

bst.delete(50)
