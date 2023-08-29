import sys


def resolve():
    N, H, X = [int(e) for e in sys.stdin.readline().split()]
    P = [int(e) for e in sys.stdin.readline().split()]
    for i, p in enumerate(P, 1):
        if p >= X - H:
            print(i)
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

    def test_入力例_1(self):
        input = """3 100 200
50 100 999"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 10 21
10 999"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 500 999
38 420 490 585 613 614 760 926 945 999"""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
