# LL: 定数倍 pypyはグローバルスコープで実行した方が速いみたい

import sys

N, P, Q = [int(e) for e in sys.stdin.readline().split()]
A = [int(e) for e in sys.stdin.readline().split()]

ans = 0
for ia in range(N - 4):
    a = A[ia]
    for ib in range(ia + 1, N - 3):
        ab = a * A[ib] % P
        for ic in range(ib + 1, N - 2):
            abc = ab * A[ic] % P
            for id in range(ic + 1, N - 1):
                abcd = abc * A[id] % P
                for ie in range(id + 1, N):
                    abcde = abcd * A[ie] % P
                    if abcde == Q:
                        ans += 1

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
        input = """6 7 1
1 2 3 4 5 6"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 1 0
0 0 0 0 0 0 0 0 0 0"""
        output = """252"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

# import itertools as it
# def debug(*args, **kwargs):
#     print(*args, **kwargs, file=sys.stderr)
# def select5_combinations_TLE(N, P, Q, A):
#     ans = 0
#     for a, b, c, d, e in it.combinations(A, 5):
#         if a * b * c * d * e % P == Q:
#             ans += 1
#             # debug(a, b, c, d, e)
#     return ans

# sys.setrecursionlimit(2000000)


# def select5(N, P, Q, A):
#     c = 0
#     for i1 in range(N - 4):
#         m1 = A[i1] % P
#         for i2 in range(i1 + 1, N - 3):
#             m2 = m1 * A[i2] % P
#             for i3 in range(i2 + 1, N - 2):
#                 m3 = m2 * A[i3] % P
#                 for i4 in range(i3 + 1, N - 1):
#                     m4 = m3 * A[i4] % P
#                     for i5 in range(i4 + 1, N):
#                         if m4 * A[i5] % P == Q:
#                             c += 1
#     return c


# # こっちの方が速いのか・・・？ → そんなことはない
# def select5_editorial(N, P, Q, A):
#     Answer = 0

#     for i in range(0, N):
#         for j in range(i + 1, N):
#             for k in range(j + 1, N):
#                 for l in range(k + 1, N):
#                     for m in range(l + 1, N):
#                         v = ((((A[i] * A[j] % P) * A[k] % P) * A[l] % P) * A[m]) % P
#                         if v == Q:
#                             Answer += 1

#     return Answer


# def resolve():
#     N, P, Q = [int(e) for e in sys.stdin.readline().split()]
#     A = [int(e) for e in sys.stdin.readline().split()]
#     # print(select5(N, P, Q, A))
#     print(select5_editorial(N, P, Q, A))

# # 関数に入れないで実行
# # pypy3だと入れない方が速いみたい

# N, P, Q = [int(e) for e in sys.stdin.readline().split()]
# A = [int(e) for e in sys.stdin.readline().split()]

# c = 0
# for i1 in range(N - 4):
#     m1 = A[i1] % P
#     for i2 in range(i1 + 1, N - 3):
#         m2 = m1 * A[i2] % P
#         for i3 in range(i2 + 1, N - 2):
#             m3 = m2 * A[i3] % P
#             for i4 in range(i3 + 1, N - 1):
#                 m4 = m3 * A[i4] % P
#                 for i5 in range(i4 + 1, N):
#                     if m4 * A[i5] % P == Q:
#                         c += 1

# print(c)

# # resolve()
# exit()
