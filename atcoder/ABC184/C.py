import sys


def resolve():
    r1, c1 = [int(e) for e in sys.stdin.readline().split()]
    r2, c2 = [int(e) for e in sys.stdin.readline().split()]
    rd, cd = r2 - r1, c2 - c1

    if rd == cd == 0:
        ans = 0
    elif abs(rd) + abs(cd) <= 3:
        ans = 1
    elif abs(rd) == abs(cd):
        ans = 1
    elif abs(rd) + abs(cd) <= 6:
        ans = 2
    elif abs(rd + cd) <= 3 or abs(rd - cd) <= 3:
        ans = 2
    elif (r1 + c1) % 2 == (r2 + c2) % 2:
        ans = 2
    else:
        ans = 3

    print(ans)


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
        input = """1 1
5 6"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 1
1 200001"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 3
998244353 998244853"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1 1
1 1"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
