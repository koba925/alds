import sys  # https://docs.python.org/ja/3/library/sys.html


def lower(N, H):
    moves = 0
    longest = 0
    for i in range(N - 1):
        if H[i] >= H[i + 1]:
            moves += 1
            longest = max(longest, moves)
        else:
            moves = 0
    return longest


def lower_editorial(N, H):
    checked = [False] * N
    longest = 0
    for i in range(N):
        if checked[i]:
            continue
        for j in range(i + 1, N):
            if H[j - 1] < H[j]:
                break
            checked[j] = True
            longest = max(longest, j - i)
    return longest


def resolve():
    N = int(sys.stdin.readline())
    H = [int(e) for e in sys.stdin.readline().split()]
    print(lower_editorial(N, H))


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
        input = """5
10 4 8 7 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7
4 4 5 6 6 5 5"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
1 2 3 4"""
        output = """0"""
        self.assertIO(input, output)

    def test_1(self):
        input = """1
10"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
