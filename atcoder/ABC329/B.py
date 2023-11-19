def resolve():
    N = int(input())
    A = [int(e) for e in input().split()]
    print(sorted(set(A))[-2])

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
2 1 3 3 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
4 3 2 1"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8
22 22 18 16 22 18 18 22"""
        output = """18"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
