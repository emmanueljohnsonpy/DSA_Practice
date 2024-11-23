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
        if index!=largest:
            self.heap[index], self.heap[largest]=self.heap[largest], self.heap[index]
            self._heapify_down(largest)

maxheap=MaxHeap()
maxheap.build_heap([3, 4, 5, 2, 6, 4, 2, 7, 8])
print("Max Heap :", maxheap.heap)
maxheap.insert(100)
print("After Inserting :", maxheap.heap)
print("Removed Element :", maxheap.remove())
print("After Removal :", maxheap.heap)