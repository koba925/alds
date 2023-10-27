def resolve():
    import math
    
    N, P = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]
    o = len([a for a in A if a % 2 == 0])
    e = len([a for a in A if a % 2 == 1])
    oc = sum([math.comb(o, k) for k in range(0, o + 1)])
    ec = sum([math.comb(e, k) for k in range(P % 2, e + 1, 2)])
    print(oc * ec)

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
        input = """3 1
2 2 1"""
        output = """4"""
        self.assertIO(input, output)
    
    def test_入力例_1(self):
        input = """2 0
1 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 1
50"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 0
1 1 1"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """45 1
17 55 85 55 74 20 90 67 40 70 39 89 91 50 16 24 14 43 24 66 25 9 89 71 41 16 53 13 61 15 85 72 62 67 42 26 36 66 4 87 59 91 4 25 26"""
        output = """17592186044416"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
