import sys
import collections as cl


def resolve():
    N = int(sys.stdin.readline())
    S = [sys.stdin.readline().strip() for _ in range(N)]
    M = int(sys.stdin.readline())
    T = [sys.stdin.readline().strip() for _ in range(M)]

    C = cl.Counter(S)
    D = cl.Counter(T)

    max_payment = -float("inf")
    for s in C.keys():
        payment = C[s] - D[s]
        max_payment = max(max_payment, payment)

    print(max(max_payment, 0))


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
apple
orange
apple
1
grape"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
apple
orange
apple
5
apple
apple
apple
apple
apple"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1
voldemort
10
voldemort
voldemort
voldemort
voldemort
voldemort
voldemort
voldemort
voldemort
voldemort
voldemort"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """6
red
red
blue
yellow
yellow
red
5
red
red
yellow
green
blue"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
