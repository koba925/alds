def resolve():
    N = int(input())
    XL = [[int(e) for e in input().split()] for _ in range(N)]
    R = sorted([(x + l - 1, x - l) for x, l in XL])

    ans, elast = 0, float("-inf")
    for e, b in R:
        if elast < b: 
            ans += 1
            elast = e

    print(ans)

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
2 4
4 3
9 3
100 5"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
8 20
1 10"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
10 1
2 1
4 1
6 1
8 1"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
