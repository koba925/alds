def resolve():
    N, M, L = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]
    B = [int(e) for e in input().split()]
    L = set([tuple([int(e) for e in input().split()]) for _ in range(L)])

    BS = list(reversed(sorted((b, j) for j, b in enumerate(B, 1))))
    max_price = 0
    for i, a in enumerate(A, 1):
        for b, j in BS:
            if a + b < max_price: break
            if (i, j) not in L:
                max_price = max(max_price, a + b)

    print(max_price)

def resolve_TLE():
    import itertools as it
    
    N, M, L = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]
    B = [int(e) for e in input().split()]
    X = [[int(e) for e in input().split()] for _ in range(L)]

    max_item = int(L ** 0.5 + 1)
    A = sorted([(a, i) for i, a in enumerate(A, 1)], reverse = True)
    B = sorted([(b, j) for j, b in enumerate(B, 1)], reverse = True)
    X = set([tuple(x) for x in X])

    max_price = 0
    for a, i in A[:max_item]:
        for b, j in B:
            if (i, j) not in X:
                max_price = max(max_price, a + b)
    for a, i in A:
        for b, j in B[:max_item]:
            if (i, j) not in X:
                max_price = max(max_price, a + b)

    print(max_price)

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
        input = """2 3 3
2 1
10 30 20
1 2
2 1
2 3"""
        output = """31"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 1 0
1000000000 1
1000000000"""
        output = """2000000000"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 10 10
47718 21994 74148 76721 98917 73766 29598 59035 69293 29127
7017 46004 16086 62644 74928 57404 32168 45794 19493 71590
1 3
2 6
4 5
5 4
5 5
5 6
5 7
5 8
5 10
7 3"""
        output = """149076"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
