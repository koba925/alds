import sys


def find_it_mine(N, A):
    def path(start):
        p = [start]
        node = parent[start]
        while node != start:
            p.append(node)
            node = parent[node]
        return reversed(p)

    parent = [None] + [-1] * N
    visited = [None] + [False] * N

    node = 1
    while not visited[node]:
        visited[node] = True
        nxt = A[node]
        parent[nxt] = node
        node = nxt
    return list(path(node))


def find_it_editorial(N, A):
    path = []
    visited = [None] + [False] * N
    node = 1
    while not visited[node]:
        visited[node] = True
        path += [node]
        node = A[node]
    start = path.index(node)
    return path[start:]


def resolve():
    N = int(sys.stdin.readline())
    A = [None] + [int(e) for e in sys.stdin.readline().split()]
    ans = find_it_mine(N, A)
    # ans = find_it_editorial(N, A)
    print(len(ans))
    print(*ans)


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
        input = """7
6 7 2 1 3 4 5"""
        output = """4
7 5 3 2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
2 1"""
        output = """2
1 2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8
3 7 4 7 3 3 8 2"""
        output = """3
2 7 8"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
