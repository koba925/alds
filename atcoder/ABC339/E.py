# TK: Segment Tree セグメント木 
# https://github.com/not522/ac-library-python
# https://atcoder.github.io/ac-library/production/document_ja/segtree.html
# Range Maximum Queueとして使っている

def resolve():
    from atcoder.segtree import SegTree

    N, D = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]
    MAXVAL = max(A)

    memo = SegTree(max, 0, MAXVAL + 1)
    for a in A:
        memo.set(a, memo.prod(max(a - D, 0), min(a + D + 1, MAXVAL + 1)) + 1)

    print(memo.all_prod())



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
        input = """4 2
3 5 1 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 10
10 20 100 110 120"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """11 7
21 10 3 19 28 12 11 3 3 15 16"""
        output = """6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
