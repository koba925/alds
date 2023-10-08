def resolve():
    S = input()
    for i in range(1, 16, 2):
        if S[i] != "0":
            print("No")
            break
    else:
        print("Yes")

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
        input = """1001000000001010"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1010100000101000"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1111111111111111"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
