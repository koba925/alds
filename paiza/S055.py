import sys

sys.setrecursionlimit(2000000)


def topological_sort(animals, G):
    def rec(a):
        visited[a] = True
        for next_a in G[a]:
            if visited[next_a]:
                continue
            rec(next_a)
        order.append(a)

    visited = {a: False for a in animals}

    order = []
    for a in animals:
        if visited[a]:
            continue
        rec(a)

    return list(reversed(order))


def S055(H, W, A, N, animals, G):
    moves = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    porder = topological_sort(animals, G)

    for predetor in porder:
        for row in range(H):
            for col in range(W):
                if A[row][col] != predetor:
                    continue
                for drow, dcol in moves:
                    nrow, ncol = row + drow, col + dcol
                    if 0 <= nrow < H and 0 <= ncol < W:
                        if A[nrow][ncol] in G[predetor]:
                            A[nrow][ncol] = "-"


def print_animals(A):
    for row in A:
        print(*row)


def resolve():
    H, W = [int(e) for e in sys.stdin.readline().split()]
    A = [list(sys.stdin.readline().split()) for _ in range(H)]
    animals = set(sum(A, []))
    N = int(sys.stdin.readline())
    G = {a: [] for a in animals}
    for _ in range(N):
        p, v = sys.stdin.readline().split()
        G[p].append(v)

    S055(H, W, A, N, animals, G)
    print_animals(A)


resolve()
