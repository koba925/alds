import sys

def resolve():
    a, b = [int(e) for e in sys.stdin.readline().split()]
    if a < 0 and b < 0:
        print("Positive" if (b - a) % 2 == 1 else "Negative")
    elif a > 0 and b > 0:
        print("Positive")
    else:
        print("Zero")

resolve()
exit()

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


if __name__ == "__main__":
    unittest.main()
