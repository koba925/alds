import sys

def chocolate(N, D, X, A):
    total = X
    for a in A:
        for day in range(1, D + 1, a):
            total += 1
    return total

def chocolate_editorial(N, D, X, A):
    return X + sum(1 + (D - 1) // a for a in A)

def resolve():
    N = int(sys.stdin.readline())
    D, X = [int(e) for e in sys.stdin.readline().split()]
    A = [int(sys.stdin.readline()) for _ in range(N)]
    print(chocolate_editorial(N, D, X, A))

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
7 1
2
5
10"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
8 20
1
10"""
        output = """29"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
30 44
26
18
81
18
6"""
        output = """56"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
