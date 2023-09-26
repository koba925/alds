def resolve():
    S = input()
    K = int(input())
    for s in S[:K]:
        if s != "1":
            print(s)
            break
    else:
        print(1)


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
        input = """1214
4"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
157"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """299792458
9460730472580800"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
