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

    def build_heap(self, elements):
        self.heap = elements[:]
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def remove(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        root = self.heap[0]
        if len(self.heap) > 1:
            self.heap[0] = self.heap.pop()
            self._heapify_down(0)
        else:
            self.heap.pop()
        return root

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)


# Min Heap
min_heap = MinHeap()
min_heap.build_heap([5, 3, 8, 4, 1, 9])
print("Min Heap:", min_heap.heap)  # Min Heap: [1, 3, 8, 4, 5, 9]
min_heap.insert(2)
print("After Insert:", min_heap.heap)  # After Insert: [1, 3, 2, 4, 5, 9, 8]
print("Removed Element:", min_heap.remove())  # Removed Element: 1
print("After Remove:", min_heap.heap)  # After Remove: [2, 3, 8, 4, 5, 9]
















class MaxHeap:
    def __init__(self):
        self.heap = []

    def build_heap(self, elements):
        """Build a max heap from a list of elements."""
        self.heap = elements[:]
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def insert(self, val):
        """Insert an element into the heap."""
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def remove(self):
        """Remove and return the largest element (root)."""
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        root = self.heap[0]
        if len(self.heap) > 1:
            self.heap[0] = self.heap.pop()
            self._heapify_down(0)
        else:
            self.heap.pop()
        return root

    def _heapify_up(self, index):
        """Ensure the heap property by moving an element up."""
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index):
        """Ensure the heap property by moving an element down."""
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)


# Max Heap
max_heap = MaxHeap()
max_heap.build_heap([5, 3, 8, 4, 1, 9])
print("Max Heap:", max_heap.heap)  # Max Heap: [9, 5, 8, 4, 1, 3]
max_heap.insert(10)
print("After Insert:", max_heap.heap)  # After Insert: [10, 5, 9, 4, 1, 3, 8]
print("Removed Element:", max_heap.remove())  # Removed Element: 10
print("After Remove:", max_heap.heap)  # After Remove: [9, 5, 8, 4, 1, 3]













def heapify(arr, n, i):
    """
    Heapify a subtree rooted at index i.
    n is the size of the heap
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # Compare with left child
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Compare with right child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)

def heap_sort(arr):
    """
    Sort array in ascending order using heap sort
    """
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root to end
        arr[0], arr[i] = arr[i], arr[0]
        # Call heapify on reduced heap
        heapify(arr, i, 0)
    
    return arr

# Example usage
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = heap_sort(arr.copy())  # Create a copy to preserve original array
print(f"Original array: {arr}")
print(f"Sorted array: {sorted_arr}")

























def heapify(arr, n, i):
    """
    Heapify a subtree rooted at index i.
    n is the size of the heap
    Creating a min heap - smallest element at root
    """
    smallest = i  # Initialize smallest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # Compare with left child
    if left < n and arr[left] < arr[smallest]:
        smallest = left

    # Compare with right child
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    # If smallest is not root
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)

def heap_sort_descending(arr):
    """
    Sort array in descending order using min heap
    """
    n = len(arr)

    # Build min heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root (smallest) to end
        arr[0], arr[i] = arr[i], arr[0]
        # Call heapify on reduced heap
        heapify(arr, i, 0)
    
    return arr

# Example usage
arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)
sorted_arr = heap_sort_descending(arr.copy())
print("Sorted array (descending):", sorted_arr)

# Another example
test_arr = [64, 34, 25, 12, 22, 11, 90]
print("\nOriginal array:", test_arr)
sorted_arr = heap_sort_descending(test_arr.copy())
print("Sorted array (descending):", sorted_arr)




































class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Example usage:
trie = Trie()
trie.insert("cat")
trie.insert("can")
trie.insert("car")
trie.insert("dog")
trie.insert("dot")

print(trie.search("cat"))  # Output: True
print(trie.starts_with("ca"))  # Output: True
print(trie.search("bat"))  # Output: False
