

# Deletion{Except Root Node With 1 child}

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
    def delete(self, data):
        if self.key is None:
            print('Tree is empty!')
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data)
            else:
                print('Given Node is Not present in the tree!')
        elif data > self.key:
            if self.rchild:
                self.rchild=self.rchild.delete(data)
            else:
                print('Given Node is Not present in the tree!')
        else:
            if self.lchild is None:
                temp=self.rchild
                self=None
                return temp
            if self.rchild is None:
                temp=self.lchild
                self=None
                return temp
            node=self.rchild
            while node.lchild:
                node=node.lchild
            self.key=node.key
            self.rchild=self.rchild.delete(node.key)
        return self 



root=BST(10)
list1=[6, 3, 1, 6, 98, 3, 7]
for i in list1:
    root.insert(i)
root.delete(10)
print("Preorder :")
root.preorder()
print("\nInorder :")
root.inorder()
print("\nPostorder :")
root.postorder()