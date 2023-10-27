def resolve():
    H, W = [int(e) for e in input().split()]
    S = [list(input()) for _ in range(H)]

    moves = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

    for srow in range(H):
        for scol in range(W):
            for drow, dcol in moves:
                nrow, ncol = srow, scol 
                for c in "snuke":
                    if nrow < 0 or  H <= nrow: break
                    if ncol < 0 or  W <= ncol: break
                    if S[nrow][ncol] != c: break
                    nrow, ncol = nrow + drow, ncol + dcol
                else:
                    nrow, ncol = srow, scol 
                    for _ in "snuke":
                        print(nrow + 1, ncol + 1)
                        nrow, ncol = nrow + drow, ncol + dcol
                    return

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
        input = """6 6
vgxgpu
amkxks
zhkbpp
hykink
esnuke
zplvfj"""
        output = """5 2
5 3
5 4
5 5
5 6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 5
ezzzz
zkzzz
ezuzs
zzznz
zzzzs"""
        output = """5 5
4 4
3 3
2 2
1 1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 10
kseeusenuk
usesenesnn
kskekeeses
nesnusnkkn
snenuuenke
kukknkeuss
neunnennue
sknuessuku
nksneekknk
neeeuknenk"""
        output = """9 3
8 3
7 3
6 3
5 3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
