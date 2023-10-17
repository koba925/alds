from bisect import bisect_left

def resolve():
    N, T = input().split()
    N = int(N)
    S = [input() for _ in range(N)]

    lt = len(T)
    top, bottom = [0] * N, [0] * N

    for i in range(N):
        itop = ibottom = 0
        s = S[i]
        ls = len(s)
        for j in range(ls):
            if itop < lt and s[j] == T[itop]:
                top[i] += 1
                itop += 1
            if ibottom < lt and s[ls - 1 - j] == T[lt - 1 - ibottom]:
                bottom[i] += 1
                ibottom += 1

    top.sort()
    bottom.sort()

    ans = 0
    for t in top:
        b = bisect_left(bottom, lt - t)
        ans += N - b

    print(ans)
    
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

    def test_1(self):
        input = """8 abc
addddd
ddddda
abdddd
ddddab
cddddd
dddddc
bcdddd
ddddbc
"""
        output = """12"""
        self.assertIO(input, output)
    
    def test_入力例_1(self):
        input = """3 bac
abba
bcb
aaca"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 xx
x
x
x
x
x"""
        output = """25"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 y
x"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10 ms
mkgn
m
hlms
vmsle
mxsm
nnzdhi
umsavxlb
ffnsybomr
yvmm
naouel"""
        output = """68"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
