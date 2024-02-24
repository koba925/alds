def resolve():
    N = int(input())
    ans = max(len(s) for s in input().split("-"))
    print(ans if ans != 0 and ans != N else -1)

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

    def test_my_1(self):
        input = """3
ooo"""
        output = """-1"""
        self.assertIO(input, output)

    def test_my_2(self):
        input = """3
oo-"""
        output = """2"""
        self.assertIO(input, output)
    
    def test_入力例_1(self):
        input = """10
o-oooo---o"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1
-"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """30
-o-o-oooo-oo-o-ooooooo--oooo-o"""
        output = """7"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
