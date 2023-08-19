# 1_C.py List

# #9
# list 9.00s
# deque 1.26s
# DoublyLinkedList 2.11s AC
# double deques 1.19s AC

from collections import deque

class List:
    def __init__(self) -> None:
        self.before = deque()
        self.after = deque()

    def insert(self, x):
        self.after.appendleft(x)
    
    def move(self, d):
            if d > 0:
                for _ in range(d):
                    self.before.append(self.after.popleft())
            else:
                for _ in range(-d):
                    self.after.appendleft(self.before.pop())
    
    def erase(self):
        self.after.popleft()

    def list(self):
        return self.before + self.after
    
from sys import stdin

_ = int(stdin.readline())

l = List()
perform_query = [l.insert, l.move, l.erase]

for line in stdin.readlines():
    order, *args = [int(e) for e in line.split()]
    (perform_query[order])(*args)

print(*l.list(), sep="\n")
