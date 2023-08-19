# 12_A.py Minimum Spanning Tree

# Prototype: #6 0.13s
# Use INF: #6 0.09s
# Remove Node class: #6 0.08s
# 0-based: #6 0.08s
# Remove init: #6 0.08s
# Change visited to local: #6 0.06s
# Prim's algorithm: 0.02s

from math import inf

class Graph:

    def __init__(self, n, weights) -> None:
        self.n = n
        self.weights = weights
        self.parent = [-1] * n

    def minimum_spanning_tree(self):

        visited = [False] * n
        weight_from_visited = [inf] * n

        def nearest_neighbor():
            nearest_id, min_weight = None, inf
            for id in range(self.n):
                if not visited[id] and weight_from_visited[id] < min_weight:
                    min_weight = weight_from_visited[id]
                    nearest_id = id
            return nearest_id

        def update_neighbors(nearest_id):
            for id in range(self.n):
                if (not visited[id] and
                            self.weights[nearest_id][id] < weight_from_visited[id]):
                    weight_from_visited[id] = self.weights[nearest_id][id]
                    self.parent[id] = nearest_id

        weight_from_visited[0] = 0
        while True:
            nearest_id = nearest_neighbor()
            if nearest_id is None:
                break
            visited[nearest_id] = True
            update_neighbors(nearest_id)

    def mst_weight_total(self):
        total = 0
        for id in range(self.n):
            if self.parent[id] != -1:
                total += self.weights[self.parent[id]][id]
        return total


n = int(input())
weights = [
    [inf if e == "-1" else int(e) for e in input().split()]
    for _ in range(n)
]
g = Graph(n, weights)
g.minimum_spanning_tree()
print(g.mst_weight_total())
