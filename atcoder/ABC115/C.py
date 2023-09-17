import sys


def resolve():
    N, K = [int(e) for e in sys.stdin.readline().split()]
    H = [int(sys.stdin.readline()) for _ in range(N)]
    H.sort()
    print(min([H[i + K - 1] - H[i] for i in range(N - K + 1)]))


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
10
15
11
14
12"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 3
5
7
5
7
7"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
