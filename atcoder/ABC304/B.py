def resolve():
    truncate = lambda N, k: N // 10 ** k * 10 ** k
    N = int(input())
    if N < 10 ** 3: print(N)
    elif N < 10 ** 4: print(truncate(N, 1))
    elif N < 10 ** 5: print(truncate(N, 2))
    elif N < 10 ** 6: print(truncate(N, 3))
    elif N < 10 ** 7: print(truncate(N, 4))
    elif N < 10 ** 8: print(truncate(N, 5))
    else: print(truncate(N, 6))

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
        input = """20230603"""
        output = """20200000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """304"""
        output = """304"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """500600"""
        output = """500000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
