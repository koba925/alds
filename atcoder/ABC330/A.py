def resolve():
    N, L = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]

    print(len([a for a in A if a >= L]))

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
        input = """5 60
60 20 100 90 40"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 80
79 78 77 76"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 50
31 41 59 26 53 58 97 93 23 84"""
        output = """6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
