def resolve():
    def divceil(a, x): return int((a + x - 1) // x)

    N = int(input())
    C, S, F = zip(*[[int(e) for e in input().split()] for _ in range(N - 1)])

    for i in range(N):
        t = 0
        for j in range(i, N - 1):
            if t < S[j]:
                t = S[j] + C[j]
            else:
                t = S[j] + F[j] * divceil(t - S[j], F[j]) + C[j]
        print(t)

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
6 5 1
1 10 1"""
        output = """12
11
0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
12 24 6
52 16 4
99 2 2"""
        output = """187
167
101
0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
12 13 1
44 17 17
66 4096 64"""
        output = """4162
4162
4162
0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
