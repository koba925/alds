# 12_B.py Single Source Shortest Path I 単一始点最短経路 ダイクストラ

from collections import namedtuple, deque
from math import inf

Adj = namedtuple("Adj", "id, wgt")


class Vert:
    def __init__(self, adjs):
        self.parent = None
        self.visited = False
        self.distance = inf
        self.adjs = adjs

    def __repr__(self):
        return f"Vert({self.parent}, {self.visited}, {self.distance}, {self.adjs})"


class Graph:
    def __init__(self, n, adjs) -> None:
        self.n = n
        self.verts = [Vert(adjs[id]) for id in range(n)]

    def dijkstra(self, start):
        self.verts[start].distance = 0

        while True:
            nearest_id, nearest_dist = -1, inf
            for id in range(self.n):
                v = self.verts[id]
                if not v.visited and v.distance < nearest_dist:
                    nearest_id, nearest_dist = id, v.distance

            if nearest_id == -1:
                break

            nearest = self.verts[nearest_id]
            nearest.visited = True

            for adj in nearest.adjs:
                nextv = self.verts[adj.id]
                if (not nextv.visited and
                        nearest.distance + adj.wgt < nextv.distance):
                    nextv.distance = nearest.distance + adj.wgt
                    nextv.parent = nearest_id

    def print_distances(self):
        for i in range(self.n):
            print(i, self.verts[i].distance)


n = int(input())
adjs = [None] * n
for _ in range(n):
    id, _, *tmp = [int(e) for e in input().split()]
    adjs[id] = [Adj(id, wgt) for id, wgt in zip(tmp[::2], tmp[1::2])]

g = Graph(n, adjs)
g.dijkstra(0)
g.print_distances()
