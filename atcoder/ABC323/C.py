def resolve():
    N, M = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]
    S = [input() for _ in range(N)]
    
    T = [sum(a for a, c in zip(A, s) if c == "o") + i for i, s in enumerate(S, 1)]
    best = max(T)

    B = list(reversed(sorted(enumerate(A), key=lambda x: x[1])))
    for i in range(N):
        j, count = 0, 0
        while T[i] < best:
            if S[i][B[j][0]] == "x":
                T[i] += B[j][1]
                count += 1
            j += 1
        print(count)


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
        input = """3 4
1000 500 700 2000
xxxo
ooxx
oxox"""
        output = """0
1
1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 5
1000 1500 2000 2000 2500
xxxxx
oxxxx
xxxxx
oxxxx
oxxxx"""
        output = """1
1
1
1
0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7 8
500 500 500 500 500 500 500 500
xxxxxxxx
oxxxxxxx
ooxxxxxx
oooxxxxx
ooooxxxx
oooooxxx
ooooooxx"""
        output = """7
6
5
4
3
2
0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
