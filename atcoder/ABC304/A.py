def resolve():
    N = int(input())
    SA = [input().split() for _ in range(N)]

    min_i = min((int(a), i) for i, [s, a] in enumerate(SA))[1]
    for i in range(N): print(SA[(i + min_i) % N][0])

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
alice 31
bob 41
carol 5
dave 92
ellen 65"""
        output = """carol
dave
ellen
alice
bob"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
takahashi 1000000000
aoki 999999999"""
        output = """aoki
takahashi"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
