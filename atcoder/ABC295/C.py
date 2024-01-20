def resolve():
    import collections as cl

    N = int(input())
    A = [int(e) for e in input().split()]
    C = cl.Counter(A)
    print(sum(s // 2 for s in C.values()))

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
4 1 7 4 1 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1
158260522"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
295 2 29 295 29 2 29 295 2 29"""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
