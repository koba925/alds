import sys

sys.setrecursionlimit(2000000)


def resolve():
    N = int(sys.stdin.readline())
    bars = set()
    for _ in range(N):
        S = sys.stdin.readline().strip()
        R = S[::-1]
        if S not in bars and R not in bars:
            bars.add(S)
    print(len(bars))

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
a
abc
de
cba
de
abc"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
