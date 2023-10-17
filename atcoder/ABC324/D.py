import collections as cl

# sortした方が速いがCounterもTLEするほどではない

def resolve():
    N = int(input())
    S = input()
    # C = sorted(list(S))
    C = cl.Counter(S)

    ans, k = 0, 0
    while k ** 2 < 10 ** N:
        # CS = sorted(list(str(k ** 2).zfill(N))) 
        CS = cl.Counter(str(k ** 2).zfill(N))
        if C == CS: ans += 1
        k += 1
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

    def test_(self):
        input = """1
0"""
        output = """1"""
        self.assertIO(input, output)
    
    def test_入力例_1(self):
        input = """4
4320"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
010"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """13
8694027811503"""
        output = """840"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
