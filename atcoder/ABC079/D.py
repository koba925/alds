import sys

def wall(H, W, C, A):
    def floyd_warshall():
        INF = 10**3 + 1
        for k in range(10):
            for i in range(10):
                for j in range(10):
                    C[i][j] = min(C[i][j], C[i][k] + C[k][j])
    
    floyd_warshall()
    return sum(sum(C[n][1] for n in row if n != -1) for row in A)


def resolve():
    H, W = [int(e) for e in sys.stdin.readline().split()]
    C = [[int(e) for e in sys.stdin.readline().split()] for _ in range(10)]
    A = [[int(e) for e in sys.stdin.readline().split()] for _ in range(H)]
    print(wall(H, W, C, A))

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
        input = """2 4
0 9 9 9 9 9 9 9 9 9
9 0 9 9 9 9 9 9 9 9
9 9 0 9 9 9 9 9 9 9
9 9 9 0 9 9 9 9 9 9
9 9 9 9 0 9 9 9 9 2
9 9 9 9 9 0 9 9 9 9
9 9 9 9 9 9 0 9 9 9
9 9 9 9 9 9 9 0 9 9
9 9 9 9 2 9 9 9 0 9
9 2 9 9 9 9 9 9 9 0
-1 -1 -1 -1
8 1 1 8"""
        output = """12"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 5
0 999 999 999 999 999 999 999 999 999
999 0 999 999 999 999 999 999 999 999
999 999 0 999 999 999 999 999 999 999
999 999 999 0 999 999 999 999 999 999
999 999 999 999 0 999 999 999 999 999
999 999 999 999 999 0 999 999 999 999
999 999 999 999 999 999 0 999 999 999
999 999 999 999 999 999 999 0 999 999
999 999 999 999 999 999 999 999 0 999
999 999 999 999 999 999 999 999 999 0
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 5
0 4 3 6 2 7 2 5 3 3
4 0 5 3 7 5 3 7 2 7
5 7 0 7 2 9 3 2 9 1
3 6 2 0 2 4 6 4 2 3
3 5 7 4 0 6 9 7 6 7
9 8 5 2 2 0 4 7 6 5
5 4 6 3 2 3 0 5 4 3
3 6 2 3 4 2 4 0 8 9
4 6 5 4 3 5 3 2 0 8
2 1 3 4 5 7 8 6 4 0
3 5 2 6 1
2 5 3 2 1
6 9 2 5 6"""
        output = """47"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
