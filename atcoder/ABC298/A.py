def resolve():
    N = int(input())
    S = input()

    print("Yes" if "o" in S and "x" not in S else "No")

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
        input = """4
oo--"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
---"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1
o"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """100
ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooox"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
