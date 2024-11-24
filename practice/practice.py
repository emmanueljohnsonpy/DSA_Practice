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
                else:
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
    def closest_value(self, target):
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
bst.insert(30)

print("Contains 10 :", bst.contains(10))
print("Contains 40 :", bst.contains(40))

bst.delete(10)

inorder_result=[]
bst.inorder(bst.root, inorder_result)
print("Inorder Traversal :", inorder_result)

preorder_result=[]
bst.preorder(bst.root, preorder_result)
print("Preorder Traversal :", preorder_result)

postorder_result=[]
bst.postorder(bst.root, postorder_result)
print("Postorder Traversal :", postorder_result)

target=17
closest=bst.closest_value(target)
print(f"Closest Value to {target} is {closest}")

print("This is a BST :", bst.is_bst())














































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
            raise IndexError("Heap is empty")
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
        if index!=smallest:
            self.heap[index], self.heap[smallest]=self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)
    def ascending_order(self):
        sorted_list=[]
        while self.heap:
            sorted_list.append(self.remove())
        return sorted_list
minheap=MinHeap()
minheap.build_heap([3, 4, 2, 5, 7, 1, 8, 9])
print("MinHeap :", minheap.heap)
minheap.insert(100)
print("After Inserting :", minheap.heap)
temp=minheap.remove()
print("Removed Value :", temp)
print("After Removing :", minheap.heap)
print("Min heap Ascending Order :", minheap.ascending_order())















































class MaxHeap:
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
        while index>0 and self.heap[index]>self.heap[parent]:
            self.heap[index], self.heap[parent]=self.heap[parent], self.heap[index]
            index=parent
            parent=(index-1)//2
    def _heapify_down(self, index):
        largest=index
        left=2*index+1
        right=2*index+2
        if left<len(self.heap) and self.heap[left]>self.heap[largest]:
            largest=left
        if right<len(self.heap) and self.heap[right]>self.heap[largest]:
            largest=right
        if largest!=index:
            self.heap[index], self.heap[largest]=self.heap[largest], self.heap[index]
            self._heapify_down(largest)
    def descending_order(self):
        sorted_list=[]
        while self.heap:
            sorted_list.append(self.remove())
        return sorted_list


maxheap=MaxHeap()
maxheap.build_heap([3, 4, 2, 6, 1, 7, 8, 2, 1, 0])
print("Max Heap :", maxheap.heap)
maxheap.insert(100)
print("After inserting :", maxheap.heap)
print("Removed element :", maxheap.remove())
print("After Removal :", maxheap.heap)
print("Descending Order :", maxheap.descending_order())









































class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end_of_word=False

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self, word):
        node=self.root
        for char in word:
            if char not in node.children:
                node.children[char]=TrieNode()
            node=node.children[char]
        node.is_end_of_word=True
    def search(self, word):
        node=self.root
        for char in word:
            if char not in node.children:
                return False
            node=node.children[char]
        return node.is_end_of_word
    def starts_with(self, prefix):
        node=self.root
        for char in prefix:
            if char not in node.children:
                return False
            node=node.children[char]
        return True


trie=Trie()
trie.insert('cat')
print(trie.search('cat'))
print(trie.search('yo'))

print(trie.starts_with('c'))
print(trie.starts_with('yo'))