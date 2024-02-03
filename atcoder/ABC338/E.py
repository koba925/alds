def resolve():
    from collections import namedtuple
    Point = namedtuple("Point", "left, pair")

    N = int(input())
    points = [Point(True, -1)] * (2 * N)
    for pair in range(N):
        a, b = [int(e) for e in input().split()]
        a, b = min(a, b), max(a, b)
        points[a - 1] = Point(True, pair)
        points[b - 1] = Point(False, pair)
    
    stack = []
    for left, pair in points:
        if left:
            stack.append(pair)
        else:
            pair_left = stack.pop()
            if pair_left != pair:
                print("Yes")
                break
    else:
        print("No")

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
1 3
4 2
5 6"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
6 1
4 3
2 5"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
2 4
3 7
8 6
5 1"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
