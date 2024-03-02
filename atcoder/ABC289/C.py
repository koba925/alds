def resolve():
    def solve(N, M, A):
        all = set(range(1, N + 1))
        ret = 0
        for i in range(1 << M):
            s = set()
            for j in range(M):
                if i & 1 == 1: s = s.union(A[j])
                i >>= 1
            if s == all: ret += 1
        return ret
    
    N, M = [int(e) for e in input().split()]
    A = []
    for _ in range(M):
        c = int(input())
        A.append(set(int(e) for e in input().split()))

    print(solve(N, M, A))

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
        input = """3 3
2
1 2
2
1 3
1
2"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 2
2
1 2
2
1 3"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6 6
3
2 3 6
3
2 4 6
2
3 6
3
1 5 6
3
1 3 6
2
1 4"""
        output = """18"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
