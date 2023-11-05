def resolve():
    N = int(input())
    S = input()

    print("Yes" if S.find("ab") >= 0 or S.find("ba") >= 0 else "No")

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

    def test_(self):
        input = """3
cba"""
        output = """Yes"""
        self.assertIO(input, output)
    
    def test_入力例_1(self):
        input = """3
abc"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
ba"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7
atcoder"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
