# Heap, Priority Queue

# 普通は heapq を使う
# 生のlistを使い、最初の要素が最小
# 最大値を取り出すときは-1をかける
# タプルも使える

from heapq import heappush, heappop
def heaptop(hq): return hq[0]
def heapempty(hq): return len(hq) == 0

hq = []
heappush(hq, 1)
if not heapempty(hq):
    print(heaptop(hq))
top = heappop(hq)

# 自分で書くと

class Heap:
    def __init__(self, elements = []):
        self.heap = [None] + elements # 1-based
        self.size = len(elements)

    def range(self):
        return range(1, self.size + 1)
    
    def is_empty(self):
        return len(self.heap) <= 1
    
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

    def peek(self):
        return self.heap[1]
    
    def extract_max(self):
        m = self.heap[1]
        n = self.heap.pop()
        self.size -= 1
        if self.size > 0:
            self.heap[1] = n
            self.max_heapify(1)        
        return m
