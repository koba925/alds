import sys

sys.setrecursionlimit(2000000)

def resolve():
    N = int(sys.stdin.readline())
    A = [int(e) for e in sys.stdin.readline().split()]

    highrank = 0
    colors = set()
    for a in A:
        if a >= 3200:
            highrank += 1
        else:
            colors.add(a // 400)
    lower = max(1, len(colors))
    higher = len(colors) + highrank

    print(lower, higher)

# resolve()

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
2100 2500 2700 2700"""
        output = """2 2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
1100 1900 2800 3200 3200"""
        output = """3 5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """20
800 810 820 830 840 850 860 870 880 890 900 910 920 930 940 950 960 970 980 990"""
        output = """1 1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
