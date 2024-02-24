def resolve():
    import itertools as it

    def solve(N, A):
        A = sorted(A)
        AA = list(it.accumulate(A, initial=0))
        A.reverse()
        AA.reverse()

        for i, (big, smallsum) in enumerate(zip(A, it.islice(AA, 1, None)), 1):
            if big > 2 * smallsum: return i
        return N

    N = int(input())
    A = [int(e) for e in input().split()]
    print(solve(N, A))

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
3 1 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
1 1 1 1 1"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
40 1 30 2 7 20"""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
