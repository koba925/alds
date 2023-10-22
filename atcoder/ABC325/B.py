def resolve():
    N = int(input())
    counts = [0] * 24
    for _ in range(N):
        w, x = [int(e) for e in input().split()]
        for t in range(24):
            if 9 <= (x + t) % 24 < 18:
                counts[t] += w
    print(max(counts))

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
5 0
3 3
2 18"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
1 10
1000000 20"""
        output = """1000000"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
31 3
20 8
11 5
4 3
47 14
1 18"""
        output = """67"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
