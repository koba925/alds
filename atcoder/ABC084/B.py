import sys
import re


def postal_code(A, B, S):
    p = re.compile(r"\d{" + str(A) + "}-\d{" + str(B) + "}")
    return p.match(S) is not None


def resolve():
    A, B = [int(e) for e in sys.stdin.readline().split()]
    S = sys.stdin.readline().strip()
    print("Yes" if postal_code(A, B, S) else "No")


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
        input = """3 4
269-6650"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 1
---"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 2
7444"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
