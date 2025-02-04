class Minheap:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)
    
    def __str__(self):
        return str(self.heap)
    
    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap)- 1)
    
    def peek_min(self):
        if not self.heap:
            raise IndexError('Empty Heap')
        else:
            return self.heap[0]

    def extrack_min(self):
        if not self.heap:
            raise IndexError('Empty Heap')
        
        min_element = self.heap[0]
        last_element = self.heap.pop()

        if self.heap:
            self.heap[0] = last_element
            self.sift_down(0)
        return min_element

    def heapify(self, elements:list[int]):
        self.heap = list(elements)

        for i in reversed(range(self._parent(len(self.heap) - 1) + 1)):
            self.sift_down(i)

    def _parent(self, index):
        return (index - 1) // 2 if index != 0 else None

    def _left(self, index):
        left = (2 * index) + 1
        return left if left < len(self.heap) else None
    
    def _right(self, index):
        right = (2 * index) + 2
        return right if right < len(self.heap) else None

    def sift_up(self, index):
        parent_index = self._parent(index)

        while parent_index is not None and self.heap[index] < self.heap[parent_index]:
            self.heap[index] , self.heap[parent_index] = self.heap[parent_index] , self.heap[index]
            index = parent_index
            parent_index = self._parent(index)

    def sift_down(self, index):
        while True:
            smallest = index

            left = self._left(index)
            right = self._right(index)

            if left is not None and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right is not None and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == index:
                break
            
            self.heap[index] , self.heap[smallest] = self.heap[smallest] ,self.heap[index]
            index = smallest


if __name__ == '__main__':
    min_heap = Minheap()
    min_heap.heapify([10, 8, 7, 6, 5, 3, 14, 13])
    print(min_heap)

    min_heap.insert(0cw)
    print(min_heap)