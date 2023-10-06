def resolve_naive():
    N, M = [int(e) for e in input().split()]

    B = [[1] * (M + 2) for _ in range(N + 2)]

    neighbors = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    for r in range(1, N + 1):
        for c in range(1, M + 1):
            for dr, dc in neighbors:
                B[r + dr][c + dc] = 1 - B[r + dr][c + dc]

    print(sum(sum(row[1 : M + 1]) for row in B[1 : N + 1]))


def resolve():
    N, M = [int(e) for e in input().split()]
    if N == 1 and M == 1:
        print(1)
    elif N == 1:
        print(M - 2)
    elif M == 1:
        print(N - 2)
    elif N == 2 or M == 2:
        print(0)
    else:
        print((N - 2) * (M - 2))


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
        input = """2 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 7"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """314 1592"""
        output = """496080"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

"""
1 1
0 0 0
0 1 0
0 0 0

1 2
0 1 1 0
0 0 0 0
0 1 1 0

1 3
0 1 0 1 0
0 0 1 0 0
0 1 0 1 0

1 4
0 1 0 0 1 0
0 0 1 1 0 0
0 1 0 0 1 0

2 2
0 1 1 0
1 0 0 1
1 0 0 1
0 1 1 0

2 3
0 1 0 1 0
1 0 0 0 1
1 0 0 0 1
0 1 0 1 0

2 4
0 1 0 0 1 0
1 0 0 0 0 1
1 0 0 0 0 1
0 1 0 0 1 0

3 3
0 1 0 1 0
1 0 0 0 1
0 0 1 0 0
1 0 0 0 1
0 1 0 1 0

3 5
0 1 0 0 0 1 0
1 0 0 0 0 0 1
0 0 1 1 1 0 0
1 0 0 0 0 0 1
0 1 0 0 0 1 0

4 4
0 1 0 0 1 0
1 0 0 0 0 1
0 0 1 1 0 0
0 0 1 1 0 0
1 0 0 0 0 1
0 1 0 0 1 0

5 5
0 1 0 0 0 1 0
1 0 0 0 0 0 1
0 0 1 1 1 0 0
0 0 1 1 1 0 0
0 0 1 1 1 0 0
1 0 0 0 0 0 1
0 1 0 0 0 1 0
"""
