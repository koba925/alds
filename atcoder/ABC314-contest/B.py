import sys  # https://docs.python.org/ja/3/library/sys.html


def roulette(N, A, X):
    atatta = [(i, a) for i, a in enumerate(A, 1) if X in a]
    if not atatta:
        return []
    minl = min(len(a) for i, a in atatta if X in a)
    result = [i for i, a in atatta if len(a) == minl]
    return result


def resolve():
    N = int(sys.stdin.readline())
    A = []
    for i in range(N):
        c = int(sys.stdin.readline())
        a = [int(e) for e in sys.stdin.readline().split()]
        A.append(set(a))
    X = int(sys.stdin.readline())
    result = roulette(N, A, X)
    print(len(result))
    if result:
        print(*result)


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
        input = """4
3
7 19 20
4
4 19 24 0
2
26 10
3
19 31 24
19"""
        output = """2
1 4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
1
1
1
2
1
3
0"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
