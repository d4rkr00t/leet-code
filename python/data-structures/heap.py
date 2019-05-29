class MinHeap:
    def __init__(self):
        self.heap = []

    def add(self, item):
        self.heap.append(item)
        self.__heapifyUp()

    def pop(self):
        if not len(self.heap):
            return None

        head = self.heap[0]
        last = self.heap.pop()

        if (len(self.heap)):
            self.heap[0] = last
            self.__heapifyDown()

        return head

    def head(self):
        return self.heap[0]

    def __parent(self, index):
        return -1 if index == 0 else (index - 1) // 2 if index % 2 == 1 else (index - 2) // 2

    def __heapifyUp(self):
        idx = len(self.heap) - 1

        while (idx > 0):
            parent = self.__parent(idx)
            if (self.compare(self.heap[idx], self.heap[parent]) == 1):
                self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
                idx = parent
            else:
                break

    def __heapifyDown(self):
        idx = 0

        while (idx * 2 + 1 < len(self.heap) - 1):
            left_idx = idx * 2 + 1
            right_idx = idx * 2 + 2

            child = left_idx

            if (right_idx < len(self.heap) and self.compare(
                    self.heap[left_idx], self.heap[right_idx]) == -1):
                child = right_idx

            if self.compare(self.heap[idx], self.heap[child]) == -1:
                self.heap[child], self.heap[idx] = self.heap[idx], self.heap[child]
                idx = child
            else:
                break

    def compare(self, a, b):
        return 0 if a == b else -1 if a > b else 1

    def __str__(self):
        return str(self.heap)


class MaxHeap(MinHeap):
    def compare(self, a, b):
        return 0 if a == b else 1 if a > b else -1


print()
print("Min heap:")
min_heap = MinHeap()
min_heap.add(7)
min_heap.add(10)
min_heap.add(4)
min_heap.add(3)
min_heap.add(20)
min_heap.add(15)
print(str(min_heap))
print(min_heap.pop())
print(min_heap.pop())
print(min_heap.pop())
print(min_heap.pop())
print(min_heap.pop())
print(min_heap.pop())

print()

print("Max heap:")
max_heap = MaxHeap()
max_heap.add(7)
max_heap.add(10)
max_heap.add(4)
max_heap.add(3)
max_heap.add(20)
max_heap.add(15)
print(str(max_heap))
print(max_heap.pop())
print(max_heap.pop())
print(max_heap.pop())
print(max_heap.pop())
print(max_heap.pop())
print(max_heap.pop())
