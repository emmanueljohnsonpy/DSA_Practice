# Binary Search Tree

class BST:
    def __init__(self, key):
        self.key=key
        self.lchild=None
        self.rchild=None

    def insert(self, data):
        if self.key is None:
            self.key=data
            return
        if self.key==data:
            return
        if self.key>data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)

    def search(self, data):
        if self.key==data:
            print("Node is found")
            return 
        if data<self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not Found")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not Found")
    
    def preorder(self):
        print(self.key, end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key, end=" ")
        if self.rchild:
            self.rchild.inorder()

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key, end=" ")

    
        


root=BST(10)
list1=[1,2,3,4,5,6]
for i in list1:
    root.insert(i)
root.search(33)
root.preorder()
print()
root.inorder()
print()
root.postorder()