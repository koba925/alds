def resolve():
    N = int(input())
    for _ in range(N):
        A = [int(e) for e in input().split()]
        B = []
        for j in range(N):
            if A[j] == 1: B.append(j + 1)
        print(*B)

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
0 1 1 0
1 0 0 1
1 0 0 0
0 1 0 0"""
        output = """2 3
1 4
1
2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
0 0
0 0"""
        output = """"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
0 1 0 1 1
1 0 0 1 0
0 0 0 0 1
1 1 0 0 1
1 0 1 1 0"""
        output = """2 4 5
1 4
5
1 2 5
1 3 4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
