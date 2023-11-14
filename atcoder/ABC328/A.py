def resolve():
    N, X = [int(e) for e in input().split()]
    S = [int(e) for e in input().split()]
    print(sum(s for s in S if s <= X))

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
        input = """6 200
100 675 201 200 199 328"""
        output = """499"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8 675
675 675 675 675 675 675 675 675"""
        output = """5400"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8 674
675 675 675 675 675 675 675 675"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
