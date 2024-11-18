

# Delete Root Node In Binary Search Tree

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
    def delete(self, data, curr):
        if self.key is None:
            print('Tree is empty!')
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data, curr)
            else:
                print('Given Node is Not present in the tree!')
        elif data > self.key:
            if self.rchild:
                self.rchild=self.rchild.delete(data, curr)
            else:
                print('Given Node is Not present in the tree!')
        else:
            if self.lchild is None:
                temp=self.rchild
                if data==curr:
                    self.key=temp.key
                    self.lchild=temp.lchild
                    self.rchild=temp.rchild
                    temp=None
                    return
                self=None
                return temp
            if self.rchild is None:
                temp=self.lchild
                if data==curr:
                    self.key=temp.key
                    self.lchild=temp.lchild
                    self.rchild=temp.rchild
                    temp=None
                    return
                self=None
                return temp
            node=self.rchild
            while node.lchild:
                node=node.lchild
            self.key=node.key
            self.rchild=self.rchild.delete(node.key, curr)
        return self 
    def min_node(self):
        current=self
        while current.lchild:
            current=current.lchild
        print("node with smallest key is : ", current.key)
    def max_node(self):
        current=self
        while current.rchild:
            current=current.rchild
        print("node with maximum key is : ", current.key)
def count(node):    
    if node is None:
        return 0
    return 1+count(node.lchild)+count(node.rchild)



root=BST(10)
list1=[1, 2, 9, 3, 6, 22    ]
for i in list1:
    root.insert(i)
print(count(root))
print("Preorder :")
root.preorder()
print()
if count(root)>1:
    root.delete(1, root.key)
else:
    print("Can't perform deletion operation!")
print()
root.preorder()
root.max_node()
root.min_node()

