# 2_B.py Queue
# deque: 0.50s 30144 KB
# ring: Queue Full or MLE

class QueueError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class Queue:
    def __init__(self, maxelem):
        self.maxlen = maxelem + 1
        self.queue = [None] * self.maxlen
        self.head = 0
        self.tail = 0
    
    def __repr__(self) -> str:
        return f"({self.head}, {self.tail}, {self.queue})"
    
    def is_empty(self):
        return self.head == self.tail
    
    def is_full(self):
        return self.head == (self.tail + 1) % self.maxlen

    def enqueue(self, val):
        if self.is_full():
            raise QueueError("Queue Full")
        self.queue[self.tail] = val
        self.tail = (self.tail + 1) % self.maxlen

    def front(self):
        if self.is_empty():
            raise QueueError("Queue Empty")
        return self.queue[self.head]

    def dequeue(self):
        if self.is_empty():
            raise QueueError("Queue Empty")
        val = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.maxlen
        return val

q = Queue(3)
q.enqueue(0)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.front())
print(q.dequeue())
print(q.front())
print(q.dequeue())
print(q.front())
print(q.dequeue())

exit()

from sys import stdin

n, _ = [int(e) for e in stdin.readline().split()]
queues = [Queue(10000) for _ in range(n)]

for query in stdin.readlines():
    q = [int(e) for e in query.split()]
    if q[0] == 0:
        queues[q[1]].enqueue(q[2])
    elif q[0] == 1 and not queues[q[1]].empty():
        print(queues[q[1]].front())
    elif q[0] == 2 and not queues[q[1]].empty():
        queues[q[1]].dequeue()
