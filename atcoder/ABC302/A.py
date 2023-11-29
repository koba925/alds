def resolve():
    A, B = [int(e) for e in input().split()]
    print((A + B - 1) // B)

def resolve():
    def divceil(a, x): return int((a + x - 1) // x)
    A, B = [int(e) for e in input().split()]
    print(divceil(A, B))
    
    
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
        input = """7 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """123456789123456789 987654321"""
        output = """124999999"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """999999999999999998 2"""
        output = """499999999999999999"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
