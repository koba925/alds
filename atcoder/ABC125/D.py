def resolve():
    def debug(*args, **kwargs): print(*args, **kwargs, file=sys.stderr)

    import sys
    sys.setrecursionlimit(2000000)

    N = int(input())
    A = [int(e) for e in input().split()]
    O = A[:]

    max_sum = float("-inf")

    last_plus = 0
    for i in range(N - 1):
        if A[i] < 0:
            A[i] *= -1
            A[i + 1] *= -1
        else:
            last_plus = i
    
    s = sum(abs(a) for a in A)
    if A[N - 1] < 0:
        s -= min(abs(a) for a in A[last_plus:]) * 2
    print(s)

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
-10 5 -4"""
        output = """19"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
10 -4 -8 -11 3"""
        output = """30"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """11
-1000000000 1000000000 -1000000000 1000000000 -1000000000 0 1000000000 -1000000000 1000000000 -1000000000 1000000000"""
        output = """10000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
