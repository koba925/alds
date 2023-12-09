def resolve():
    import itertools as it

    N, T = [int(e) for e in input().split()]
    C = [int(e) for e in input().split()]
    R = [int(e) for e in input().split()]

    color = T if T in C else C[0]
    print(max((r, i) for c, r, i in zip(C, R, it.count(1)) if c == color)[1])

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
        input = """4 2
1 2 1 2
6 3 4 5"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 2
1 3 1 4
6 3 4 5"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 1000000000
1000000000 1
1 1000000000"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
