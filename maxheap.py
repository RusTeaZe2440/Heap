class MaxHeap:

    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def __str__(self):
        return str(self.heap)

    def insert(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def peek_max(self):
        if not self.heap:
            raise IndexError('Empty Heap')
        else:
            return self.heap[0]

    def extract_max(self):
        if not self.heap:
            raise IndexError('Empty Heap')

        max_element = self.heap[0]
        last_element = self.heap.pop()

        if self.heap:
            self.heap[0] = last_element
            self._sift_down(0)
        return max_element

    def _parent(self, index):
        return (index - 1) // 2 if index != 0 else None

    def _left(self, index):
        left = (2 * index) + 1
        return left if left > len(self.heap) else None

    def _right(self, index):
        right = (2 * index) + 2
        return right if right > len(self.heap) else None

    def heapify(self, elements: list[int]) -> list[int]:
        self.heap = list(elements)

        for i in reversed(range(self._parent(len(self.heap) - 1) + 1)):
            self._sift_down(i)
            
    def _sift_up(self, index):
        parent_index = self._parent(index)

        while parent_index is not None and self.heap[index] > self.heap[parent_index]:
            self.heap[index] , self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = self._parent(index)

    def _sift_down(self, index):
        while True:
            largest = index

            left = self._left(index)
            right = self._right(index)

            if left is not None and self.heap[left] > self.heap[largest]:
                largest = left
            if right is not None and self.heap[right] > self.heap[largest]:
                largest = right

            if largest == index:
                break

            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest


if __name__ == '__main__':
    max_heap = MaxHeap()
    max_heap.heapify([10, 8, 7, 6, 5, 3, 2, 1])
    print(max_heap)

    max_heap.insert(12)
    print(max_heap)