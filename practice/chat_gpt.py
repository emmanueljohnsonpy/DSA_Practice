class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def contains(self, value):
        current = self.root
        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def delete(self, value):
        def find_min(node):
            while node.left:
                node = node.left
            return node

        def delete_node(node, value):
            if not node:
                return None
            if value < node.value:
                node.left = delete_node(node.left, value)
            elif value > node.value:
                node.right = delete_node(node.right, value)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                temp = find_min(node.right)
                node.value = temp.value
                node.right = delete_node(node.right, temp.value)
            return node

        self.root = delete_node(self.root, value)

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

bst = BinarySearchTree()

bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(11)
bst.insert(13)

print("Contains 7:", bst.contains(7))
print("Contains 20:", bst.contains(20))  

bst.delete(15)

inorder_result = []
bst.inorder(bst.root, inorder_result)
print("Inorder Traversal:", inorder_result)

preorder_result = []
bst.preorder(bst.root, preorder_result)
print("Preorder Traversal:", preorder_result)

postorder_result = []
bst.postorder(bst.root, postorder_result)
print("Postorder Traversal:", postorder_result)

target=12
closest=bst.find_closest_value(target)
print(f"The closest value to {target} is {closest}")

print("Is the tree a valid BST?", bst.is_bst(bst.root))




















class MinHeap:
    def __init__(self):
        self.heap = []
    
    def build_heap(self, array):
        """Builds a min-heap from an unsorted array."""
        self.heap = array
        for i in range(len(array) // 2 - 1, -1, -1):
            self._heapify_down(i)
    
    def insert(self, val):
        """Inserts a value into the min-heap."""
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)
    
    def remove(self):
        """Removes and returns the smallest value in the heap."""
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move the last element to the root
        self._heapify_down(0)
        return root
    
    def _heapify_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        if smallest != index:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self._heapify_down(smallest)
    
    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)


class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def build_heap(self, array):
        """Builds a max-heap from an unsorted array."""
        self.heap = array
        for i in range(len(array) // 2 - 1, -1, -1):
            self._heapify_down(i)
    
    def insert(self, val):
        """Inserts a value into the max-heap."""
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)
    
    def remove(self):
        """Removes and returns the largest value in the heap."""
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move the last element to the root
        self._heapify_down(0)
        return root
    
    def _heapify_down(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2
        
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        
        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self._heapify_down(largest)
    
    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)


# Example Usage:

# Min Heap
min_heap = MinHeap()
min_heap.build_heap([10, 20, 15, 30, 40])
min_heap.insert(5)
print("Min Heap:", min_heap.heap)  # [5, 20, 10, 30, 40, 15]
print("Removed Min:", min_heap.remove())  # 5
print("After Removal:", min_heap.heap)  # [10, 20, 15, 30, 40]

# Max Heap
max_heap = MaxHeap()
max_heap.build_heap([10, 20, 15, 30, 40])
max_heap.insert(50)
print("Max Heap:", max_heap.heap)  # [50, 40, 15, 20, 10, 30]
print("Removed Max:", max_heap.remove())  # 50
print("After Removal:", max_heap.heap)  # [40, 30, 15, 20, 10]
