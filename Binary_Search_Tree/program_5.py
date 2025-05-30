

# In-Order And Post-Order Algorithm

class BST:
    def __init__(self, key):
        self.key=key 
        self.lchild=None
        self.rchild=None
    def insert(self, data):
        if self.key is None:
            self.key=data
            return
        if self.key==data:  # no duplicates
            return
        if self.key>data:   # dup in left side >=, right side >
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
        if data==self.key:
            print('Node is found!')
            return
        if data<self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node not Found!")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node not Found!")

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
list1=[6, 3, 1, 6, 98, 3, 7]
for i in list1:
    root.insert(i)
print("Preorder :")
root.preorder()
print("\nInorder :")
root.inorder()
print("\nPostorder :")
root.postorder()