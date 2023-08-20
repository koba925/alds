import sys  # https://docs.python.org/ja/3/library/sys.html


def resolve():
    A, B, K = [int(e) for e in sys.stdin.readline().split()]
    if B - A + 1 >= 2 * K:
        print(*range(A, A + K), *range(B - K + 1, B + 1), sep="\n")
    else:
        print(*range(A, B + 1), sep="\n")


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
        input = """3 8 3"""
        output = """\
3
4
5
6
7
8"""
        self.assertIO(input, output)

    def test_2(self):
        input = """3 8 1"""
        output = """\
3
8"""
        self.assertIO(input, output)

    def test_3(self):
        input = """3 7 2"""
        output = """\
3
4
6
7"""
        self.assertIO(input, output)

    def test_4(self):
        input = """3 3 100"""
        output = """\
3"""
        self.assertIO(input, output)

    def test_入力例_1(self):
        input = """3 8 2"""
        output = """3
4
7
8"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 8 3"""
        output = """4
5
6
7
8"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 9 100"""
        output = """2
3
4
5
6
7
8
9"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
