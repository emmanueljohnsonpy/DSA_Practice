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
        while True:
            if value<current.value:
                if current.left is None:
                    current.left=newnode
                    return
                current=current.left
            elif value>current.value:
                if current.right is None:
                    current.right=newnode
                    return
                current=current.right
    def contains(self, value):
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
    def find_closest_value(self, target):
        closest=float('inf')
        def helper(node, target, closest):
            if node is None:
                return closest
            if abs(target-node.value)<abs(target-closest):
                closest=node.value
            if target<node.value:
                return helper(node.left, target, closest)
            elif target>node.value:
                return helper(node.right, target, closest)
            else:
                return node.value
        return helper(self.root, target, closest)
    def is_bst(self, node=None, lower=float('-inf'), upper=float('inf')):
        if node is None:
            return True
        if node.value<=lower or node.value>=upper:
            return False
        return (self.is_bst(node.left, lower, node.value) and self.is_bst(node.right, node.value, upper))
bst=BinarySearchTree()

bst.insert(10)
bst.insert(20)
bst.insert(35)
bst.insert(25)
bst.insert(75)
bst.insert(95)

print('Contains 10 :', bst.contains(10))
print('Contains 5 :', bst.contains(5))

bst.delete(10)

inorder_result=[]
bst.inorder(bst.root, inorder_result)
print('Inorder Traversal :', inorder_result)

preorder_result=[]
bst.preorder(bst.root, preorder_result)
print('Preorder Traversal :', preorder_result)

postorder_result=[]
bst.postorder(bst.root, postorder_result)
print('Postorder Traversal :', postorder_result)

target=20
closest=bst.find_closest_value(target)
print(f"{closest} is closest to {target}")

print("Is this BST or Not?", bst.is_bst(bst.root))