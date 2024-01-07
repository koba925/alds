def resolve():
    N = int(input())
    A = [[int(e) for e in input().split()] for _ in range(N)]
    B = [[int(e) for e in input().split()] for _ in range(N)]

    for i in range(4):
        ok = True
        for i in range(N):
            for j in range(N):
                if A[i][j] == 1 and B[i][j] == 0:
                    ok = False
        if ok:
            print("Yes")
            break
        C = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                C[i][j] = A[N - 1 - j][i]
        A = C
    else:
        print("No")

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
0 1 1
1 0 0
0 1 0
1 1 0
0 0 1
1 1 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
0 0
0 0
1 1
1 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
0 0 1 1 0
1 0 0 1 0
0 0 1 0 1
0 1 0 1 0
0 1 0 0 1
1 1 0 0 1
0 1 1 1 0
0 0 1 1 1
1 0 1 0 1
1 1 0 1 0"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
