def resolve():
    N, K, S = [int(e) for e in input().split()]
    if S > 1:
        A = [S] * K + [S - 1] * (N - K)
    else:
        A = [1] * K + [2] * (N - K)
    print(*A)

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
        input = """4 2 3"""
        output = """1 2 3 4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 3 100"""
        output = """50 50 50 30 70"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
