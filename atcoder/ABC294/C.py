def resolve():
    INF = 10 ** 9 + 1

    N, M = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()] + [INF]
    B = [int(e) for e in input().split()] + [INF]

    ans_a, ans_b = [], []
    ia = ib = 0
    while A[ia] < INF or B[ib] < INF:
        if A[ia] < B[ib]:
            ans_a.append(ia + ib + 1)
            ia += 1
        else:
            ans_b.append(ia + ib + 1)
            ib += 1
    print(*ans_a)
    print(*ans_b)

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
        input = """4 3
3 14 15 92
6 53 58"""
        output = """1 3 4 7
2 5 6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 4
1 2 3 4
100 200 300 400"""
        output = """1 2 3 4
5 6 7 8"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8 12
3 4 10 15 17 18 22 30
5 7 11 13 14 16 19 21 23 24 27 28"""
        output = """1 2 5 9 11 12 15 20
3 4 6 7 8 10 13 14 16 17 18 19"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
