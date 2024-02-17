def resolve():
    from heapq import heapify, heappush, heappop

    def solve(A):
            
        B = [(-n, a) for a, n in enumerate(A, 1)]
        heapify(B)

        while B:
            n1, a1 = heappop(B)
            if B:
                n2, a2 = heappop(B)
            else:
                return -n1 - 1
            if n1 < -1: heappush(B, (n1 + 1, a1))
            if n2 < -1: heappush(B, (n2 + 1, a2))

        return 0
    
    K, T = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]

    print(solve(A))

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
        input = """7 3
3 2 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 3
1 4 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100 1
100"""
        output = """99"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
