

# Insertion

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
        if self.key>data:   # dup in left side >, right side <
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)
            

root=BST(10)
list1=[6, 8, 8, 4, 2, 10, 25]
for i in list1:
    root.insert(i)