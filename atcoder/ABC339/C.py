def resolve():
    import itertools as it

    N = int(input())
    A = [int(e) for e in input().split()]
    B = list(it.accumulate(A, initial=0))
    print(B[-1] - min(B))


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
3 -5 7 -4"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
0 0 0 0 0"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
-1 1000000000 1000000000 1000000000"""
        output = """3000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
