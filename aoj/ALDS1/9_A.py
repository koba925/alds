# 9_A.py

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
       
def print_element(heap, i):
    print(f"node {i}: key = {heap.val(i)},", end="")

    p = heap.parent(i)
    if p != 0:
        print(f" parent key = {heap.val(p)},", end="")

    l = heap.left(i)
    if l != 0:
        print(f" left key = {heap.val(l)},", end="")

    r = heap.right(i)
    if r != 0:
        print(f" right key = {heap.val(r)}, ", end="")

    print()

n = int(input())
heap =  Heap([int(e) for e in input().split()])

for i in heap.range():
    print_element(heap, i)
