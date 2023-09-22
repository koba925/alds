import sys


def divisors_of(N: int) -> list[int]:
    i, divisors = 1, []
    while i * i <= N:
        if N % i == 0:
            divisors.append(i)
            if N // i != i:
                divisors.append(N // i)
        i += 1
    return sorted(divisors)


def resolve():
    N = int(sys.stdin.readline())
    print(min([n - 1 + N // n - 1 for n in divisors_of(N)]))


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
        input = """10"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """50"""
        output = """13"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10000000019"""
        output = """10000000018"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
