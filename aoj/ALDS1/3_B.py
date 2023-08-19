# 3_B.py

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

n, q = [int(e) for e in input().split()]

processes = Queue(100000)
for i in range(n):
    name, time = input().split()
    time = int(time)
    processes.enqueue({"name": name, "time": time})

t = 0
while not processes.is_empty() > 0:
    p = processes.dequeue()
    if p["time"] > q:
        t += q
        p["time"] -= q
        processes.enqueue(p)
    else:
        t += p["time"]
        print(p["name"], t)
