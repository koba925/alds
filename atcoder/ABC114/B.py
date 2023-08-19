import sys

def resolve():
    S = sys.stdin.readline().strip()
    print(min(abs(int(S[i:i+3]) - 753) for i in range(len(S) - 2)))
    # min_diff = 2000
    # for i in range(len(S) - 2):
    #     X = int(S[i:i+3])
    #     diff = abs(X - 753)
    #     if diff < min_diff:
    #         min_diff = diff
    # print(min_diff)

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
        input = """1234567876"""
        output = """34"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """35753"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1111111111"""
        output = """642"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
