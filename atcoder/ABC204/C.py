# C - Tour

from sys import setrecursionlimit
setrecursionlimit(3000)

def search(c, adj):
    def _search(c):
        visited[c] = True
        for a in adj[c]:
            if not visited[a]:
                _search(a)

    visited = [False] * N
    _search(c)
    return len([v for v in visited if v])
    

def solve(N, M, adj):
    return sum(search(c, adj) for c in range(N))

N, M = [int(e) for e in input().split()]
adj = [[] for _ in range(N)]
for _ in range(M):
    a, b = [int(e) for e in input().split()]
    adj[a - 1].append(b - 1)

print(solve(N, M, adj))
