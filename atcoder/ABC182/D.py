import sys  # https://docs.python.org/ja/3/library/sys.html


def wandering(N, A):
    pos, net_move, max_move, max_pos = 0, 0, 0, 0
    for i in range(N):
        net_move += A[i]
        max_move = max(max_move, net_move)
        max_pos = max(max_pos, pos + max_move)
        pos += net_move

    return max_pos


def resolve():
    N = int(sys.stdin.readline())
    A = [int(e) for e in sys.stdin.readline().split()]
    print(wandering(N, A))


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
2 -1 -2"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
-2 1 3 -1 -1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
-1000 -1000 -1000 -1000 -1000"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
