import sys  # https://docs.python.org/ja/3/library/sys.html
import math  # https://docs.python.org/ja/3/library/math.html


def resolve():
    K = int(sys.stdin.readline())
    s = 0
    for a in range(1, K + 1):
        for b in range(1, K + 1):
            abgcd = math.gcd(a, b)
            for c in range(1, K + 1):
                s += math.gcd(abgcd, c)
    print(s)


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
        input = """2"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """200"""
        output = """10813692"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
