


""" class Node:
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
                    current.right =newnode
                    return
                current=current.right

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

inorder_result=[]
bst.inorder(bst.root, inorder_result)
print("Inorder Traversal :", inorder_result)

preorder_result=[]
bst.preorder(bst.root, preorder_result)
print("Preorder Traversal :", preorder_result)

postorder_result=[]
bst.postorder(bst.root, postorder_result)
print("Postorder Traversal :", postorder_result) """


class MinHeap:
    def __init__(self):
        self.heap=[]
    def build_heap(self, elements):
        self.heap=elements[:]
        for i in range(len(self.heap)//2-1, -1, -1):
            self._heapify_down(i)
    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap)-1)
    def remove(self):
        if len(self.heap)==0:
            raise IndexError("Heap is empty!")
        root=self.heap[0]
        if len(self.heap)>1:
            self.heap[0]=self.heap.pop()
            self._heapify_down(0)
        else:
            self.heap.pop()
        return root
    def _heapify_up(self, index):
        parent=(index-1)//2
        while index>0 and self.heap[index]<self.heap[parent]:
            self.heap[index], self.heap[parent]=self.heap[parent], self.heap[index]
            index=parent
            parent=(index-1)//2
    def _heapify_down(self, index):
        smallest=index
        left=2*index+1
        right=2*index+2
        if left<len(self.heap) and self.heap[left]<self.heap[smallest]:
            smallest=left
        if right<len(self.heap) and self.heap[right]<self.heap[smallest]:
            smallest=right
        if smallest!=index:
            self.heap[smallest], self.heap[index]=self.heap[index], self.heap[smallest]
            self._heapify_down(smallest)
    def ascending_order(self):
        result=[]
        while self.heap:
            result.append(self.remove())
        return result

arr=[4, 10, 3, 5, 1]

minheap=MinHeap()
minheap.build_heap(arr)
print(minheap.heap)
print(minheap.ascending_order())