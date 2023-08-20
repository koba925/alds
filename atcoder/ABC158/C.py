# LL: 数が少なければ全探索も
# LL: パーセントの計算はかけてから100で割る

import sys  # https://docs.python.org/ja/3/library/sys.html
import math  # https://docs.python.org/ja/3/library/math.html


def resolve():
    A, B = [int(e) for e in sys.stdin.readline().split()]
    lower = math.ceil(max(A * 100 / 8, B * 100 / 10))
    upper = min((A + 1) * 100 / 8, (B + 1) * 100 / 10)
    print(lower if lower < upper else -1)


def resolve_editorial():
    A, B = [int(e) for e in sys.stdin.readline().split()]
    for x in range(10000):
        if x * 8 // 100 == A and x * 10 // 100 == B:
            print(x)
            break
    else:
        print(-1)


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
        input = """72 89"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_1(self):
        input = """2 2"""
        output = """25"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8 10"""
        output = """100"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """19 99"""
        output = """-1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
