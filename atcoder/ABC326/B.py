def resolve():
    def is326(n):
        digits = [int(e) for e in str(n)]
        return digits[0] * digits[1] == digits[2]
    
    N = int(input())
    while not is326(N):
        N += 1

    print(N)

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
        input = """320"""
        output = """326"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """144"""
        output = """144"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """516"""
        output = """600"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
