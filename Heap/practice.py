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
            raise IndexError('Heap is empty!')
        root=self.heap[0]
        if len(self.heap)>1:
            self.heap[0]=self.heap.pop()
            self._heapify_down(0)
        else:
            self.heap.pop()
        return root


    