import sys


def resolve():
    R, G, B, N = [int(e) for e in sys.stdin.readline().split()]

    count = 0
    r = 0
    while R * r <= N:
        Rr = R * r
        g = 0
        while Rr + G * g <= N:
            Gg = G * g
            if (N - Rr - Gg) % B == 0:
                count += 1
            g += 1
        r += 1

    print(count)


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
        input = """1 2 3 4"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """13 1 4 3000"""
        output = """87058"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
