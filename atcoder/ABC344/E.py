import itertools as it

N = int(input())
A = [int(e) for e in input().split()]

prv = {n: p for p, n in it.pairwise(A)}
prv[0], prv[A[0]] = A[-1], 0

nxt = {p: n for p, n in it.pairwise(A)}
nxt[0], nxt[A[-1]] = A[0], 0

for _ in range(int(input())):
    c, *p = [int(e) for e in input().split()]

    match c:
        case 1: 
            x, y = p
            nxt[y] = nxt[x]
            prv[y] = x
            prv[nxt[x]] = y
            nxt[x] = y
        case 2:
            x, = p
            nxt[prv[x]] = nxt[x]
            prv[nxt[x]] = prv[x]
            del nxt[x], prv[x]

ans, cur = [], nxt[0]
while cur != 0:
    ans.append(cur)
    cur = nxt[cur]

print(*ans)

"""
2
1 2
2
2 1
2 2

1
1
2
1 1 2
2 2
"""