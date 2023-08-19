# 11_C.py

from collections import deque

class Graph:
    class Node:
        def __init__(self) -> None:
            self.adjs = None
            self.distance = -1

    def __init__(self, n) -> None:
        self.size = n
        self.nodes = [None] + [Graph.Node() for _ in range(n)] # 1-based
        
    @classmethod
    def read(cls, n):
        g = cls(n)
        for _ in range(n):
            id, _, *adjs = [int(e) for e in input().split()]
            g.nodes[id].adjs = adjs
        return g

    def node_range(self):
        return range(1, self.size + 1)
    
    def print_node_distances(self):
        for id in self.node_range():
            print(id, self.nodes[id].distance)

    def bfs(self):
        waiting = deque()
        waiting.appendleft(1)
        self.nodes[1].distance = 0
        while len(waiting) > 0:
            node_id = waiting.pop()
            for adj_id in self.nodes[node_id].adjs:
                if self.nodes[adj_id].distance == -1:
                    self.nodes[adj_id].distance = self.nodes[node_id].distance + 1
                    waiting.appendleft(adj_id)

n = int(input())
g = Graph.read(n)
g.bfs()
g.print_node_distances()
