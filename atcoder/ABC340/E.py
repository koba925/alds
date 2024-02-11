# TK: 遅延セグメント木 Lazy Segment Tree RAQ Range Addition Query
# ソース：https://github.com/not522/ac-library-python/blob/master/atcoder/lazysegtree.py
# サンプル：https://github.com/not522/ac-library-python/blob/master/example/lazysegtree_practice_l.py
# 解説： https://betrue12.hateblo.jp/entry/2020/09/22/194541
# TODO: AOJのDSLをやる

def resolve_TLE():
    N, M = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]
    B = [int(e) for e in input().split()]

    for b in B:
        C = 0
        a = A[b]
        A[b] = 0
        r = a // N
        a = a % N
        while a > 0:
            C += 1
            A[(b + C) % N] += 1
            a -= 1
        for i in range(N):
            A[i] += r
    
    print(*A)

def resolve():
    from atcoder.lazysegtree import LazySegTree
    from operator import add

    N, M = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]
    B = [int(e) for e in input().split()]

    st = LazySegTree(lambda _1, _2: 0, 0, add, add, 0, A)

    for b in B:
        a = st.get(b)
        st.set(b, 0)
        r, q = divmod(a, N)
        if b + q + 1 < N:
            st.apply(0, b + 1, r)
            st.apply(b + 1, b + q + 1, r + 1)
            st.apply(b + q + 1, N, r)
        else:
            st.apply(0, (b + q + 1) % N, r + 1)
            st.apply((b + q + 1) % N, b + 1, r)
            st.apply(b + 1, N, r + 1)

    print(*[st.get(i) for i in range(N)])

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
        input = """5 3
1 2 3 4 5
2 4 0"""
        output = """0 4 2 7 2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 10
1000000000 1000000000 1000000000
0 1 0 1 0 1 0 1 0 1"""
        output = """104320141 45436840 2850243019"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 4
1
0 0 0 0"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
