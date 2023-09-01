# TK: 0がない世界の位取り記法

import sys

d = "abcdefghijklmnopqrstuvwxyz"


def dalmatians(n: int) -> str:
    temp = []

    while n > 0:
        n -= 1
        temp.append(d[n % 26])
        n //= 26

    return "".join(reversed(temp))


def resolve():
    N = int(sys.stdin.readline())
    print(dalmatians(N))


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
        input = """1"""
        output = """a"""
        self.assertIO(input, output)

    def test_26(self):
        input = """26"""
        output = """z"""
        self.assertIO(input, output)

    def test_27(self):
        input = """27"""
        output = """aa"""
        self.assertIO(input, output)

    def test_52(self):
        input = """52"""
        output = """az"""
        self.assertIO(input, output)

    def test_53(self):
        input = """53"""
        output = """ba"""
        self.assertIO(input, output)

    def test_702(self):
        input = """702"""
        output = """zz"""
        self.assertIO(input, output)

    def test_703(self):
        input = """703"""
        output = """aaa"""
        self.assertIO(input, output)

    # def test_123456789(self):
    #     input = """123456789"""
    #     output = """jjddja"""
    #     self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
