def resolve():
    N, M = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]
    B = [int(e) - 1 for e in input().split()]

    print(sum(A[b] for b in B))

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
        input = """3 2
10 20 30
1 3"""
        output = """40"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 1
1 1 1 100
4"""
        output = """100"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8 4
22 75 26 45 72 81 47 29
4 6 7 8"""
        output = """202"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
