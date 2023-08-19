import sys

def resolve():
    N, Q = [int(e) for e in sys.stdin.readline().split()]
    A = [None] + [int(e) for e in sys.stdin.readline().split()]
    V = [None] + [A[i + 1] - A[i] for i in range(1, N)]
    E = sum(abs(v) for v in V[1:])

    for _ in range(Q):
        l, r, v = [int(e) for e in sys.stdin.readline().split()]

        if l > 1:
            before = abs(V[l - 1])
            V[l - 1] += v
            after = abs(V[l - 1])
            E += (after - before)
        if r < N:
            before = abs(V[r])
            V[r] -= v
            after = abs(V[r])
            E += (after - before)
 
        print(E)


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
        input = """3 3
1 2 3
2 3 1
1 2 -1
1 3 2"""
        output = """3
4
4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """20 10
61 51 92 -100 -89 -65 -89 -64 -74 7 87 -2 51 -39 -50 63 -23 36 74 37
2 2 -45
6 19 82
2 9 36
7 13 71
16 20 90
18 20 -24
14 17 -78
10 11 -55
7 19 -26
20 20 -7"""
        output = """1164
1328
1256
1350
1440
1416
1572
1482
1430
1437"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
