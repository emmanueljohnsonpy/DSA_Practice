

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

bst=BinarySearchTree()

bst.insert(10)
bst.insert(20)
bst.insert(30)
bst.insert(40)
bst.insert(50)
