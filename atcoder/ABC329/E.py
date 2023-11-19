def resolve():
    import collections as cl

    def is_good(i, X):
        replace = False
        for j, t in enumerate(T):
            if X[i + j] == t:
                replace = True
            elif X[i + j] != "#":
                return False
        return replace

    N, M = [int(e) for e in input().split()]
    S = input()
    T = input()

    X = list(S)
    Q = cl.deque()
    
    for i in range(0, N - M + 1):
        if is_good(i, X):
            Q.append(i)

    while Q:
        i = Q.popleft()
        X[i : i + M] = ["#"] * M
        for j in range(max(i - M + 1, 0), min(i + M, N - M + 1)):
            if is_good(j, X): 
                Q.append(j)

    print("Yes" if all(x == "#" for x in X) else "No")


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
        input = """7 3
ABCBABC
ABC"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 3
ABBCABC
ABC"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """12 2
XYXXYXXYYYXY
XY"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
