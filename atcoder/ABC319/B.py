import sys


def resolve():
    N = int(sys.stdin.readline())

    ans = ""
    for i in range(N + 1):
        for j in range(1, 10):
            if N % j == 0 and i % (N // j) == 0:
                ans += str(j)
                break
        else:
            ans += "-"

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

    def test_入力例_1(self):
        input = """12"""
        output = """1-643-2-346-1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7"""
        output = """17777771"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1"""
        output = """11"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
