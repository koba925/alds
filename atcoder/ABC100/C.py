import sys


def resolve():
    def multi2(n):
        c = 0
        while n % 2 == 0:
            c += 1
            n //= 2
        return c

    N = int(sys.stdin.readline())
    A = [int(e) for e in sys.stdin.readline().split()]

    print(sum(multi2(a) for a in A))


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
        input = """3
5 2 4"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
631 577 243 199"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
2184 2126 1721 1800 1024 2528 3360 1945 1280 1776"""
        output = """39"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
