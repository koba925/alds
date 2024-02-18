def resolve():
    import operator as op
    import itertools as it

    from atcoder.segtree import SegTree

    N, Q = [int(e) for e in input().split()]
    S = input()
    alt = [s != t for s, t in it.pairwise(S)]
    alt = SegTree(op.and_, True, alt)

    for _ in range(Q):
        q, l, r = [int(e) for e in input().split()]
        l -= 1
        r -= 1
        match q:
            case 1: 
                if 0 < l: alt.set(l - 1, not alt.get(l - 1))
                if r < N - 1: alt.set(r, not alt.get(r))
            case 2:
                print("Yes" if alt.prod(l, r) else "No")


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
        input = """5 6
10100
2 1 3
2 1 5
1 1 4
2 1 5
1 3 3
2 2 4"""
        output = """Yes
No
Yes
No"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 2
1
1 1 1
2 1 1"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
