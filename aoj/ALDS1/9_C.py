# 9_C.py

# TLE but algorythm is correct #3 0.03s #4 TLE

class Heap:
    def __init__(self, elements = []):
        self.heap = [None] + elements
        self.size = len(elements)
    
    # def val(self, i):
    #     return self.heap[i]
    
    # def add(self, val):
    #     self.heap.append(val)
    #     self.size += 1
    #     return self.size

    # def parent(self, i):
    #     return i // 2

    # def left(self, i):
    #     return 2 * i

    # def right(self, i):
    #     return 2 * i + 1

    def range(self):
        return range(1, self.size + 1)
    
    def max_heapify(self, i):
        largest = i
        l = 2 * i
        r = 2 * i + 1
        if l <= self.size and self.heap[l] > self.heap[largest]:
            largest = l
        if r <= self.size and self.heap[r] > self.heap[largest]:
            largest = r
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest)
    
    def buid_max_heap(self):
        for i in reversed(range(1, self.size() // 2 + 1)):
            self.max_heapify(i)

    def insert(self, val):
        self.heap.append(None)
        self.size += 1

        i = self.size
        p = i // 2
        while p != 0:
            if val > self.heap[p]:
                self.heap[i] = self.heap[p]
            else:
                break
            i = p
            p = i // 2
        self.heap[i] = val

    def extract_max(self):
        m = self.heap[1]
        n = self.heap.pop()
        self.size -= 1
        if self.size > 0:
            self.heap[1] = n
            self.max_heapify(1)        
        return m

from sys import stdin

def solve():
    heap = Heap()
    for l in stdin.readlines():
        command, *param = l.split()
        if command == "insert":
            heap.insert(int(param[0]))
        elif command == "extract":
            print(heap.extract_max())
        else:
            break

solve()
