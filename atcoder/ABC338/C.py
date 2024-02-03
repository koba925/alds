def resolve():
    N = int(input())
    Q = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]
    B = [int(e) for e in input().split()]

    MAX = 10 ** 6
    max_n = 0
    for na in range(MAX + 1):
        min_nb = MAX + 1
        for i in range (N):
            qb = (Q[i] - na * A[i]) 
            if qb < 0: break
            if B[i] > 0:
                min_nb = min(min_nb, qb // B[i])
        else:
            if min_nb != MAX + 1:
                max_n = max(max_n, na + min_nb)

    print(max_n)

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

    def test_my_1(self):
        input = """2
1000000 1000000
1 0
0 1"""
        output = """2000000"""
        self.assertIO(input, output)
    
    def test_入力例_1(self):
        input = """2
800 300
100 100
200 10"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
800 300
100 0
0 10"""
        output = """38"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
800 300
801 300
800 301"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10
1000000 1000000 1000000 1000000 1000000 1000000 1000000 1000000 1000000 1000000
0 1 2 3 4 5 6 7 8 9
9 8 7 6 5 4 3 2 1 0"""
        output = """222222"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
