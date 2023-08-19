# LL: 〇〇法が思いついても、シンプルなやり方がないか考えてみる
# DAG判定
# トポロジカルソート

import sys

sys.setrecursionlimit(200000)


# 1-based
def is_DAG(G):
    def has_cycle(v):
        if cache[v] is not None:
            return cache[v]

        if visited[v]:
            return True

        visited[v] = True

        result = False
        for next_v in G[v]:
            if has_cycle(next_v):
                result = True
                break

        cache[v] = result
        return result

    N = len(G) - 1
    visited = [None] + [False] * N
    cache = [None] + [None] * N

    for v in range(1, N + 1):
        if has_cycle(v):
            return False
    return True


# 1-based, return None if G is notDAG
def topological_sort(G):
    def rec(v):
        visited[v] = True
        for next_v in G[v]:
            if visited[next_v]:
                continue
            rec(next_v)
        order.append(v)

    if not is_DAG(G):
        return None

    N = len(G) - 1
    visited = [None] + [False] * N

    order = []
    for v in range(1, N + 1):
        if visited[v]:
            continue
        rec(v)

    return list(reversed(order))


def who_is_saikyo_mine(N, M, G):
    if len([g for g in G[1:] if len(g) == 0]) != 1:
        return -1

    t = topological_sort(G)
    if t is None:
        return -1
    return t[-1]


def who_is_saikyo_editorial(N, M, G):
    strongest = [None] + [1] * N

    for weaker in G[1:]:
        strongest[weaker] = 0

    if sum(strongest) != 1:
        return -1

    return strongest.index(1)


def resolve_mine():
    N, M = [int(e) for e in sys.stdin.readline().split()]
    G = [None] + [[] for _ in range(N)]
    for _ in range(M):
        a, b = [int(e) for e in sys.stdin.readline().split()]
        G[b].append(a)
    print(who_is_saikyo_mine(N, M, G))


def resolve():
    N, M = [int(e) for e in sys.stdin.readline().split()]
    strongest = [None] + [1] * N

    for _ in range(M):
        stronger, weaker = [int(e) for e in sys.stdin.readline().split()]
        strongest[weaker] = 0

    if sum(strongest[1:]) != 1:
        print(-1)
    else:
        print(strongest.index(1))


# resolve()
# exit()

import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_1(self):
        input = """3 3
1 2
2 3
3 1"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_1(self):
        input = """3 2
1 2
2 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 2
1 3
2 3"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6 6
1 6
6 5
6 2
2 3
4 3
4 2"""
        output = """-1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
