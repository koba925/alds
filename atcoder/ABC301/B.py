def resolve():
    import itertools as it
    
    N = int(input())
    A = [int(e) for e in input().split()]
    B = [A[0]]
    for a, b in it.pairwise(A):
        if abs(a - b) == 1:
            B.append(b)
        elif a < b:
            B += range(a + 1, b + 1)
        else:
            B += range(a - 1, b - 1, -1)
    print(*B)

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
2 5 1 2"""
        output = """2 3 4 5 4 3 2 1 2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
3 4 5 6 5 4"""
        output = """3 4 5 6 5 4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
