import itertools as it

def resolve():
    p, q = input().split()
    pos = dict(zip("ABCDEFG", it.accumulate([3, 1, 4, 1, 5, 9], initial=0)))
    print(abs(pos[p] - pos[q]))

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
        input = """A C"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """G B"""
        output = """20"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """C F"""
        output = """10"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
