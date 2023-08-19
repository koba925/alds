# 2_C.py Priority Queue
# my library 1.85s 29132KB
# heqpq 0.62s 29012KB

from sys import stdin

from heapq import heappush, heappop
def heaptop(h): return h[0]
def heapempty(h): return len(h) == 0

n, _ = [int(e) for e in stdin.readline().split()]
queues = [[] for _ in range(n)]

for query in stdin.readlines():
    q = [int(e) for e in query.split()]
    if q[0] == 0:
        heappush(queues[q[1]], -q[2])
    elif q[0] == 1 and not heapempty(queues[q[1]]):
        print(-heaptop(queues[q[1]]))
    elif q[0] == 2 and not heapempty(queues[q[1]]):
        heappop(queues[q[1]])
