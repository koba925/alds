def resolve():
    import itertools as it
    import functools as ft

    B = int(input())

    apowa = lambda a: ft.reduce(lambda acc, e: acc * e, [a] * a)

    for a in it.count(1):
        k = apowa(a)
        if k == B:
            print(a)
            break
        if k > B:
            print(-1)
            break
        

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

    def test_1(self):
        input = """1"""
        output = """1"""
        self.assertIO(input, output)
    
    def test_入力例_1(self):
        input = """27"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10000000000"""
        output = """10"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
