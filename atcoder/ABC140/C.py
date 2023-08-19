import sys  # https://docs.python.org/ja/3/library/sys.html

BMAX = 10**5 + 1


def resolve():
    N = int(sys.stdin.readline())
    B = [BMAX] + [int(e) for e in sys.stdin.readline().split()] + [BMAX]

    print(sum(min(B[i], B[i + 1]) for i in range(N)))


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
        input = """3
2 5"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
3"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
0 153 10 10 23"""
        output = """53"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
