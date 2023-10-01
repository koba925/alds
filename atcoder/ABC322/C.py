def resolve():
    N, M = [int(e) for e in input().split()]
    A = [0] + [int(e) for e in input().split()]
    for i in range(M):
        for j in reversed(range(A[i + 1] - A[i])):
            print(j)


def resolve():
    N, M = [int(e) for e in input().split()]
    A = set([int(e) for e in input().split()])
    ans, days = [0] * N, 0

    for d in reversed(range(N)):
        days = 0 if d + 1 in A else days + 1
        ans[d] = days

    print(*ans, sep="\n")


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
2 3"""
        output = """1
0
0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8 5
1 3 4 7 8"""
        output = """0
1
0
0
2
1
0
0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
