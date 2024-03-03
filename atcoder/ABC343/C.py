def resolve():
    def solve(N):
        for n in range(int(N ** (1/3)) + 1, 0, -1):
            strncube = str(n ** 3)
            if strncube == strncube[::-1] and n ** 3 <= N: return n ** 3
    
    print(solve(int(input())))

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
        input = """345"""
        output = """343"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """123456789012345"""
        output = """1334996994331"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
