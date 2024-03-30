import sys
from io import StringIO
import unittest

def resolve():
    N = int(input())
    A = [int(e) for e in input().split()]
    Q = int(input())
    for _ in range(Q):
        q, *p = [int(e) for e in input().split()]
        match q:
            case 1: A[p[0] - 1] = p[1]
            case 2: print(A[p[0] - 1])

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """3
1 3 5
7
2 2
2 3
1 3 0
2 3
1 2 8
2 2
2 1"""
        expected = """3
5
0
8
1"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """5
22 2 16 7 30
10
1 4 0
1 5 0
2 2
2 3
2 4
2 5
1 4 100
1 5 100
2 3
2 4"""
        expected = """2
16
0
0
16
100"""
        self.assertIO(input, expected)

    def test_sample3(self):
        input = """7
478 369 466 343 541 42 165
20
2 1
1 7 729
1 6 61
1 6 838
1 3 319
1 4 317
2 4
1 1 673
1 3 176
1 5 250
1 1 468
2 6
1 7 478
1 5 595
2 6
1 6 599
1 6 505
2 3
2 5
2 1"""
        expected = """478
317
838
838
176
595
468"""
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
