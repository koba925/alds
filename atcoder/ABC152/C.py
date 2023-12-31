import sys


def low_elements(N, P):
    min_elem = N + 1
    ret = 0
    for p in P:
        if p <= min_elem:
            ret += 1
            min_elem = p
    return ret


def resolve():
    N = int(sys.stdin.readline())
    P = [int(e) for e in sys.stdin.readline().split()]
    print(low_elements(N, P))


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
        input = """5
4 2 5 1 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
4 3 2 1"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
1 2 3 4 5 6"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """8
5 7 4 2 6 8 1 3"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """1
1"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
