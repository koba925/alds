def resolve():
    import itertools as it
    
    N = int(input())
    A = [0] + [int(e) for e in input().split()] + [0]

    dist = lambda i, j: abs(A[i] - A[j])

    total = sum(dist(i, i + 1) for i in range(N + 1))
    for i in range(1, N + 1):
        print(total - dist(i - 1, i) - dist(i, i + 1) + dist(i - 1, i + 1))


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
        input = """3
3 5 -1"""
        output = """12
8
10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
1 1 1 2 0"""
        output = """4
4
4
2
4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
-679 -2409 -3258 3095 -3291 -4462"""
        output = """21630
21630
19932
8924
21630
19288"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
