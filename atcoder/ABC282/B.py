import sys
from io import StringIO
import unittest

def resolve():
    N, M = [int(e) for e in input().split()]
    S = [input() for _ in range(N)]
    ans = 0
    for a in range(N - 1):
        for b in range(a + 1, N):
            for j in range(M):
                if S[a][j] == "x" and S[b][j] == "x":
                    break
            else:
                ans += 1
    print(ans)

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """5 5
ooooo
oooxx
xxooo
oxoxo
xxxxx"""
        expected = """5"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """3 2
ox
xo
xx"""
        expected = """1"""
        self.assertIO(input, expected)

    def test_sample3(self):
        input = """2 4
xxxx
oxox"""
        expected = """0"""
        self.assertIO(input, expected)

    def assertIO(self, input, expected):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        actual = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
