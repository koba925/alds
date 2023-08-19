import sys  # https://docs.python.org/ja/3/library/sys.html


def resolve():
    N, M = [int(e) for e in sys.stdin.readline().split()]
    G = [None] + [[] for _ in range(N)]
    for _ in range(M):
        a, b = [int(e) for e in sys.stdin.readline().split()]
        G[a].append(b)
        G[b].append(a)

    print(*[len(g) for g in G[1:]], sep="\n")


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
        input = """4 3
1 2
2 3
1 4"""
        output = """2
2
1
1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 5
1 2
2 1
1 2
2 1
1 2"""
        output = """5
5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8 8
1 2
3 4
1 5
2 8
3 7
5 2
4 1
6 8"""
        output = """3
3
2
2
2
1
1
2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
