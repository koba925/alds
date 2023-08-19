import sys

def resolve():
    N = int(sys.stdin.readline())
    S = sys.stdin.readline().strip()
    x = maxx = 0
    for s in S:
        if s == "I":
            x += 1
            maxx = max(maxx, x)
        else:
            x -= 1
    print(maxx)

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
        input = """5
IIDID"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7
DDIDDII"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
