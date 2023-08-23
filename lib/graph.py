import sys


def dfs_rec(N, G, start):
    def _dfs(v):
        visited[v] = True
        for nv in G[v]:
            if not visited[nv]:
                parent[nv] = v
                _dfs(nv)

    visited = [None] + [False] * N
    parent = [None] + [None] * N
    _dfs(start)

    # def farthest_bfs_noweight(start, adjs):             # longest distance / farthest node
    # def shortest_bfs_noweight(start, goal, adjs):       # find shortest path / judge if connected
    def path(node):
        p = []
        while node != -1:
            p.append(node)
            node = parent[node]
        return reversed(p)

    def farthest_node():
        return (max(enumerate(distances), key=lambda x: x[1]))[0]

    l = len(adjs)
    q = deque()
    parent = [-1] * l
    distances = [-1] * l
    distances[start] = 0
    q.append(start)
    while q:
        node = q.popleft()
        # if node == goal:                            # find shortest path / judge if connected
        # return path(node)                       # find shortest path
        # return True                             # judge if connected
        for adj in adjs[node]:
            if distances[adj] == -1:
                distances[adj] = distances[node] + 1
                parent[adj] = node
                q.append(adj)
    # return []                                       # find shortest path
    # return False                                    # judge if connected
    # return max(distances)                           # longest distance
    # return farthest_node()                          # farthest node


def resolve():
    # Read edges into a graph (1-based, no weight)
    N, M = [int(e) for e in sys.stdin.readline().split()]
    # remove "[None] + " if 0-based
    G = [None] + [[] for _ in range(N)]
    for _ in range(M):
        a, b = [int(e) for e in sys.stdin.readline().split()]
        G[a].append(b)
        G[b].append(a)
