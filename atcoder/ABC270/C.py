# C - Simple path

from sys import stdin
from sys import setrecursionlimit
from collections import defaultdict, deque

setrecursionlimit(1000000)


# segmentation fault in Python
def solve_dfs_recursive(X, Y, adj):
    def dfs(v):
        if v == Y:
            return [v]
        visited.add(v)
        for a in adj[v]:
            if not a in visited:
                ans = dfs(a)
                if ans is not None:
                    return ans + [v]
        return None

    visited = set([])
    return reversed(dfs(X))

# AC
def solve_dfs_stack(X, Y, adj):
    parents = {X: None}
    to_visit = [X]
    while len(to_visit) > 0:
        v = to_visit.pop()
        if v == Y:
            break
        for a in adj[v]:
            if not a in parents:
                to_visit.append(a)
                parents[a] = v
    path = [v]
    while parents[v] is not None:
        v = parents[v]
        path.append(v)
    return reversed(path)

# editorial
def solve_editorial(X, Y, adj):
    def dfs(v):
        nonlocal stop

        if not stop:
            deq.append(v)
        if v == Y:
            stop = True
        visited.add(v)
        for a in adj[v]:
            if not a in visited:
                dfs(a)
        if not stop:
            deq.pop()

    deq = deque()
    visited = set()
    stop = False
    dfs(X)
    return list(deq)

# don't go back
def solve(X, Y, adj):
    def dfs(current, prev, path):
        if current == Y:
            return path + [current]
        for nxt in adj[current]:
            if nxt == prev: continue
            ret = dfs(nxt, current, path + [current])
            if ret: return ret
        
    return dfs(X, None, [])

    
N, X, Y = [int(e) for e in stdin.readline().split()]

adj = defaultdict(list)
for line in stdin.readlines():
    Ui, Vi = [int(e) for e in line.split()]
    adj[Ui].append(Vi)
    adj[Vi].append(Ui)

print(*solve(X, Y, adj))
