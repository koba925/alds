import sys  # https://docs.python.org/ja/3/library/sys.html

sys.setrecursionlimit(2000000)


def prerequisites_mine(N, books):
    def rec(i):
        for b in books[i]:
            if not b in read:
                read.add(b)
                rec(b)
        ans.append(i)

    read = set()
    ans = []
    rec(1)
    return ans


def topological_sort(G):
    def rec(v):
        visited[v] = True
        for next_v in G[v]:
            if visited[next_v]:
                continue
            rec(next_v)
        order.append(v)

    N = len(G) - 1
    visited = [None] + [False] * N

    order = []
    for v in range(1, N + 1):
        if visited[v]:
            continue
        rec(v)

    return order


def prerequisites(N, books):
    def rec(i):
        for b in books[i]:
            if not required[b]:
                required[b] = True
                rec(b)

    required = [None] + [False] * N
    rec(1)

    T = topological_sort(books)
    ans = [t for t in T if required[t]]
    return ans


def resolve():
    N = int(sys.stdin.readline())
    books = [None]
    for i in range(1, N + 1):
        c, *p = [int(e) for e in sys.stdin.readline().split()]
        books.append(p)
    print(*prerequisites(N, books))


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

    def test_入力例_1(self):
        input = """6
3 2 3 4
2 3 5
0
1 5
0
0"""
        output = """5 3 4 2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
1 2
1 3
1 4
1 5
1 6
0"""
        output = """6 5 4 3 2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8
1 5
1 6
1 7
1 8
0
0
0
0"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
