def resolve():
    N = int(input())
    while N % 2 == 0:
        N //= 2
    while N % 3 == 0:
        N //= 3
    print("Yes" if N == 1 else "No")

def resolve():
    N = int(input())

    power2 = 0
    while N % 2 ** (power2 + 1) == 0:
        power2 += 1

    power3 = 0
    while N % 3 ** (power3 + 1) == 0:
        power3 += 1

    print("Yes" if N == 2 ** power2 * 3 ** power3 else "No")

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
        input = """324"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """32"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """37748736"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
