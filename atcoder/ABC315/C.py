import sys  # https://docs.python.org/ja/3/library/sys.html


def resolve():
    N = int(sys.stdin.readline())
    SF = []
    for _ in range(N):
        f, s = [int(e) for e in sys.stdin.readline().split()]
        SF.append((s, f))
    SF.sort(reverse=True)
    top = SF[0]
    max_second = 0
    for i in range(1, N):
        max_second = max(max_second, SF[i][0] // (2 if top[1] == SF[i][1] else 1))
    print(top[0] + max_second)


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
        input = """4
1 4
2 10
2 8
3 6"""
        output = """16"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
4 10
3 2
2 4
4 12"""
        output = """17"""
        self.assertIO(input, output)

    def test_1(self):
        input = """2
1 10
1 2
"""
        output = """11"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
