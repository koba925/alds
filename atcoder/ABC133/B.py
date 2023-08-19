import sys  # https://docs.python.org/ja/3/library/sys.html


def good_distance(N, D, X):
    count = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            dist_sq = sum((y - z) ** 2 for y, z in zip(X[i], X[j]))
            d = 0
            while d * d <= dist_sq:
                if d * d == dist_sq:
                    count += 1
                    break
                d += 1
    return count


def resolve():
    N, D = [int(e) for e in sys.stdin.readline().split()]
    X = [[int(e) for e in sys.stdin.readline().split()] for _ in range(N)]
    print(good_distance(N, D, X))


# resolve()
# exit()

import sys
import unittest
from io import StringIO


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
        input = """3 2
1 2
5 5
-2 8"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 4
-3 7 8 2
-12 1 10 2
-2 8 9 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 1
1
2
3
4
5"""
        output = """10"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
