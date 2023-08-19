# 9_B.py

class Heap:
    def __init__(self, elements = []):
        self.heap = [None] + elements
    
    def size(self):
        return len(self.heap) - 1
    
    def val(self, i):
        return self.heap[i]
    
    def parent(self, i):
        return i // 2

    def left(self, i):
        i = 2 * i
        return i if i <= self.size() else 0

    def right(self, i):
        i = 2 * i + 1
        return i if i <= self.size() else 0

    def range(self):
        return range(1, self.size() + 1)

    def add(self, val):
        self.heap.append(val)

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if l != 0 and self.heap[l] > self.heap[i]:
            largest = l
        else:
            largest = i
        if r != 0 and self.heap[r] > self.heap[largest]:
            largest = r
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest)
    
    def buid_max_heap(self):
        for i in reversed(range(1, self.size() // 2 + 1)):
            self.max_heapify(i)

n = int(input())
heap = Heap([int(e) for e in input().split()])
heap.buid_max_heap()
print(" ", end="")
print(*([heap.val(i) for i in heap.range()]))
