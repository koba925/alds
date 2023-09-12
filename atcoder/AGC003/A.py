def resolve():
    S = input()
    n = S.find("N")
    s = S.find("S")
    e = S.find("E")
    w = S.find("W")
    if (
        (n == -1 and s != -1)
        or (s == -1 and n != -1)
        or (e == -1 and w != -1)
        or (w == -1 and e != -1)
    ):
        print("No")
    else:
        print("Yes")


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
        input = """SENW"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """NSNNSNSN"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """NNEW"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """W"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
