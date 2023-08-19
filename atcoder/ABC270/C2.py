# C - Simple path
# See https://note.com/kai1023/n/nf4021a868d49

from sys import stdin, setrecursionlimit

setrecursionlimit(2000000)

def search(start, goal, adj):
    def dfs(current, prev):
        if current == goal:
            print(*path)
            exit()
        for nxt in adj[current]:
            if nxt == prev:
                continue
            path.append(nxt)
            dfs(nxt, current)
            path.pop()

    path = [start]
    dfs(start, None)

def solve():
    N, X, Y = [int(e) for e in stdin.readline().split()]
    adj = [[] for _ in range(N + 1)]        # 1-based
    for line in stdin.readlines():
        u, v = [int(e) for e in line.split()]
        adj[u].append(v)
        adj[v].append(u)
    search(X, Y, adj)

solve()
