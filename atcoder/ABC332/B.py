def resolve():
    K, G, M = [int(e) for e in input().split()]

    g = m = 0
    for _ in range(K):
        if g == G:
            g = 0
        elif m == 0:
            m = M
        elif G - g >= m:
            g += m
            m = 0
        else:
            m -= (G - g)
            g = G

    print(g, m)

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
        input = """5 300 500"""
        output = """200 500"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 100 200"""
        output = """0 0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
