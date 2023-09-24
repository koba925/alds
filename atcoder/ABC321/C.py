import sys


def resolve_nosort():
    K = int(sys.stdin.readline())

    numbers = list(range(1, 10))
    i = 0
    while i < len(numbers):
        for j in range(0, numbers[i] % 10):
            numbers.append(numbers[i] * 10 + j)
        i += 1

    print(numbers[K - 1])


def resolve():
    K = int(sys.stdin.readline())

    numbers = []
    for s in range(2, 2**10):
        n = ""
        for i in range(10):
            if s >> i & 1 == 1:
                n += str(i)
        numbers.append(int(n[::-1]))
    numbers.sort()

    print(numbers[K - 1])


# resolve()
# exit()

import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        self.maxDiff = None
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """15"""
        output = """32"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """321"""
        output = """9610"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """777"""
        output = """983210"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
