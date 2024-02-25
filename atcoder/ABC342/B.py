def resolve_contest():
    def solve(A, B):
        for i, p in enumerate(P, 1):
            if p == A or p == B:
                return p
    
    N = int(input())
    P = [int(e) for e in input().split()]
    Q = int(input())

    for _ in range(Q):
        A, B = [int(e) for e in input().split()]
        print(solve(A, B))

def resolve():
    N = int(input())
    P = [int(e) for e in input().split()]
    I = {int(p): i for i, p in enumerate(P)}
    Q = int(input())

    for _ in range(Q):
        A, B = [int(e) for e in input().split()]
        print(P[min(I[A], I[B])])

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
2 1 3
3
2 3
1 2
1 3"""
        output = """2
2
1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7
3 7 2 1 6 5 4
13
2 3
1 2
1 3
3 6
3 7
2 4
3 7
1 3
4 7
1 6
2 4
1 3
1 3"""
        output = """3
2
3
3
3
2
3
3
7
1
2
3
3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
