import sys


def resolve():
    N, A, B = [int(e) for e in sys.stdin.readline().split()]

    if (A - B) % 2 == 0:
        ans = abs(A - B) // 2
    else:
        r1 = (A - 1) + 1 + (B - A - 1) // 2 if A < B else (B - 1) + 1 + (A - B - 1) // 2
        r2 = (N - A) + 1 + (A - B - 1) // 2 if A > B else (N - B) + 1 + (B - A - 1) // 2
        ans = min(r1, r2)

    print(ans)


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
        input = """5 1 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_2(self):
        input = """5 4 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_(self):
        input = """5 5 5"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_1(self):
        input = """5 2 4"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 2 3"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
