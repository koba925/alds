def resolve():
    W, H, N = [int(e) for e in input().split()]
    left, bottom, right, top = 0, 0, W, H
    for _ in range(N):
        x, y, a = [int(e) for e in input().split()]
        match a:
            case 1: left = max(left, x)
            case 2: right = min(right, x)
            case 3: bottom = max(bottom, y)
            case 4: top = min(top, y)
    print(max(right - left, 0) * max(top - bottom, 0))

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
        input = """5 4 2
2 1 1
3 3 4"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 4 3
2 1 1
3 3 4
1 4 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 10 5
1 6 1
4 1 3
6 9 4
9 4 2
3 1 3"""
        output = """64"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
