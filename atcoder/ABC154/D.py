import itertools as it


def resolve():
    N, K = [int(e) for e in input().split()]
    P = [int(e) for e in input().split()]
    E = [p * (p + 1) // 2 / p for p in P]
    EE = list(it.accumulate(E, initial=0))
    S = [EE[i + K] - EE[i] for i in range(N - K + 1)]
    print(max(S))


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
        input = """5 3
1 2 2 4 5"""
        output = """7.000000000000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 1
6 6 6 6"""
        output = """3.500000000000"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 4
17 13 13 12 15 20 10 13 17 11"""
        output = """32.000000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
