def resolve():
    N, K = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]

    imin = A.index(min(A))
    if N <= K:
        print(1)
    else:
        print((N + K - 3) // (K - 1))

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
        input = """4 3
2 3 1 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 3
1 2 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8 3
7 3 1 8 4 6 2 5"""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
