import sys

def ok(X, Y):
    xa, xb = X.count("A"), X.count("B")
    ya, yb = Y.count("A"), Y.count("B")
    if xa > ya or xb > yb: return False
    da = ya - xa
    for i in range(len(X)):
        if X[i] == "C":
            if da > 0:
                X[i] = "A"
                da -= 1
            else:
                X[i] = "B"
    xa, ya = 0, 0
    for i in range(len(X)):
        if X[i] == "A": xa += 1
        if Y[i] == "A": ya += 1
        if xa < ya: return False
    return True


def replace_c_or_swap_ab(N, X, Y):
    sub_X, sub_Y = [], []
    for x, y in zip(X, Y):
        if y == "C":
            if x != "C": return False
            if ok(sub_X, sub_Y):
                sub_X, sub_Y = [], []
                continue
            else:
                return False
        sub_X.append(x)
        sub_Y.append(y)                                
    return ok(sub_X, sub_Y)

def resolve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, X, Y = sys.stdin.readline().strip().split()
        print("Yes" if replace_c_or_swap_ab(int(N), list(X), list(Y)) else "No")

resolve()
exit()

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
        input = """6
3 ABC ABC
1 C B
1 B C
2 AB BA
2 BA AB
3 CCB ABA"""
        output = """Yes
Yes
No
Yes
No
Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7
5 ABABA BABAB
5 ABCBC BBABA
5 CCCCC CBABC
5 BBAAA AAABB
5 AAABB BBAAA
5 ACACB BAACB
5 ACACB BBACA"""
        output = """No
Yes
Yes
No
Yes
Yes
No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
