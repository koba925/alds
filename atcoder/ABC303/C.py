def resolve():
    N, M, H, K = [int(e) for e in input().split()]
    S = input()
    P = set([tuple([int(e) for e in input().split()]) for _ in range(M)])
    T = (0, 0)
    dx = {"R": 1, "L": -1, "U": 0, "D": 0}
    dy = {"R": 0, "L": 0, "U": 1, "D": -1}

    for s in S:
        T = (T[0] + dx[s], T[1] + dy[s])
        H -= 1
        if H < 0:
            print("No")
            break
        if T in P and H < K:
            H = K
            P.remove(T)
    else:
        print("Yes")

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
        input = """4 2 3 1
RUDL
-1 -1
1 0"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 2 1 5
LDRLD
0 0
-1 -1"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
