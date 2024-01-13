def resolve():
    H, W = [int(e) for e in input().split()]
    [print(input().replace("TT", "PC")) for _ in range(H)]

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
        input = """2 3
TTT
T.T"""
        output = """PCT
T.T"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 5
TTT..
.TTT.
TTTTT"""
        output = """PCT..
.PCT.
PCTPC"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
