def resolve():
    N = int(input())
    X, Y = zip(*[[int(e) for e in input().split()] for _ in range(N)])
    t, a = sum(X), sum(Y)
    print("Takahashi" if t > a else "Aoki" if t < a else "Draw")

def resolve():
    N = int(input())
    t = a = 0
    for _ in range(N):
        x, y = [int(e) for e in input().split()]
        t += x
        a += y
    print("Takahashi" if t > a else "Aoki" if t < a else "Draw")
    
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
        input = """4
10 2
10 1
10 2
3 2"""
        output = """Takahashi"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
5 4
4 5
2 4
1 6
7 1
3 2"""
        output = """Draw"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
0 0
10 10
50 50
0 100"""
        output = """Aoki"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
