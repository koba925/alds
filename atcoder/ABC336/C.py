def resolve():
    def even_digits(N):
        if N == 1: return "0"

        N -= 1
        ans = []
        while N > 0:
            ans.append(str(N % 5 * 2))
            N = N // 5
        return "".join(reversed(ans))

    print(even_digits(int(input())))

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

    def test_my1(self):
        input = """1"""
        output = """2"""
        self.assertIO(input, output)
    
    def test_入力例_1(self):
        input = """8"""
        output = """24"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """133"""
        output = """2024"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """31415926535"""
        output = """2006628868244228"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
