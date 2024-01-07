def resolve():
    import functools as ft

    N, M = [int(e) for e in input().split()]
    S = []
    for _ in range(M):
        _, *s = [int(e) for e in input().split()]
        S.append(ft.reduce(lambda acc, b: acc | 2 ** (b - 1), s, 0))
    P = [int(e) for e in input().split()]

    ans = 0
    for ss in range(2 ** N):
        for s, p in zip(S, P):
            ons = (ss & s).bit_count() 
            if ons & 1 != p: break
        else: ans += 1
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
    
    def test_入力例_1(self):
        input = """2 2
2 1 2
1 2
0 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 3
2 1 2
1 1
1 2
0 0 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 2
3 1 2 5
2 2 3
1 0"""
        output = """8"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
