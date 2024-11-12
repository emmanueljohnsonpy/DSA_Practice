

# Search Operation

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

root=BST(10)
list1=[8, 9, 5, 4, 3, 2]
for i in list1:
    root.insert(i)
root.search(499)