import sys
from io import StringIO
import unittest

def resolve():
    import collections as cl

    H, W, M = [int(e) for e in input().split()]
    TAX = [[int(e) for e in input().split()] for _ in range(M)]

    colors, row_painted, col_painted = cl.defaultdict(lambda: 0), set(), set()
    for t, a, x in reversed(TAX):
        match t:
            case 1:
                if a in row_painted or len(col_painted) >= W: continue
                colors[x] += W - len(col_painted)
                row_painted.add(a)
            case 2:
                if a in col_painted or len(row_painted) >= H: continue
                colors[x] += H - len(row_painted)
                col_painted.add(a)

    colors[0] += H * W - sum(colors.values())
    if colors[0] == 0: del colors[0]
    print(len(colors))
    for color in sorted(colors.keys()):
        print(color, colors[color])

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """3 4 4
1 2 5
2 4 0
1 3 3
1 3 2"""
        expected = """3
0 5
2 4
5 3"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """1 1 5
1 1 1
1 1 10
2 1 100
1 1 1000
2 1 10000"""
        expected = """1
10000 1"""
        self.assertIO(input, expected)

    def test_sample3(self):
        input = """5 5 10
1 1 1
1 2 2
1 3 3
1 4 4
1 5 5
2 1 6
2 2 7
2 3 8
2 4 9
2 5 10"""
        expected = """5
6 5
7 5
8 5
9 5
10 5"""
        self.assertIO(input, expected)

    def assertIO(self, input, expected):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        actual = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
