def resolve():
    N = int(input())
    S = [input() for _ in range(N)]
    R = zip(*S)
    rc = [row.count("o") for row in S]
    cc = [col.count("o") for col in R]

    ans = 0
    for i, row in enumerate(S):
        for j, s in enumerate(row):
            if s == "o":
                ans += (cc[j] - 1) * (rc[i] - 1)
    print(ans)

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
ooo
oxx
xxo"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
oxxx
xoxx
xxox
xxxo"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """15
xooxxooooxxxoox
oxxoxoxxxoxoxxo
oxxoxoxxxoxoxxx
ooooxooooxxoxxx
oxxoxoxxxoxoxxx
oxxoxoxxxoxoxxo
oxxoxooooxxxoox
xxxxxxxxxxxxxxx
xooxxxooxxxooox
oxxoxoxxoxoxxxo
xxxoxxxxoxoxxoo
xooxxxooxxoxoxo
xxxoxxxxoxooxxo
oxxoxoxxoxoxxxo
xooxxxooxxxooox"""
        output = """2960"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
