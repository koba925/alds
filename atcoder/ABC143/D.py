def resolve():
    from bisect import bisect_left

    N = int(input())
    L = sorted(int(e) for e in input().split())

    ans = 0
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            kmax = bisect_left(L, L[i] + L[j])
            ans += kmax - j - 1

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

    def test_1(self):
        input = """16
1 2 2 3 3 3 4 4 4 4 6 6 6 6 6 6"""
        output = """18"""
        self.assertIO(input, output)
    
    def test_入力例_1(self):
        input = """4
3 4 2 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
1 1000 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7
218 786 704 233 645 728 389"""
        output = """23"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
    # T = set()
    # i = 0
    # while i < N - 2:    
    #     j = i + 1
    #     while j < N - 1:
    #         kmax = bisect_left(L, L[i] + L[j])
    #         for k in range(j + 1, kmax):
    #             T.add((L[i], L[j], L[k]))
    #         j += 1
    #     i += 1


    # MAX = 1000

    # H = [0] * (MAX + 1)
    # for  l in [int(e) for e in input().split()]:
    #     H[l] = min(H[l] + 1, 3)

    # L = []
    # for l in range(MAX + 1):
    #     for i in range(H[l]):
    #         L.append(l)

    # N = len(L)

    # C = [0] * (MAX + 1)
    # for l in set(L):
    #     C[l] = 1
    # C = list(it.accumulate(C))

    # H = [0] * (MAX + 1)
    # for  l in [int(e) for e in input().split()]:
    #     H[l] = min(H[l] + 1, 3)

    # L = []
    # for l in range(MAX + 1):
    #     for i in range(H[l]):
    #         L.append(l)

    # N = len(L)

    # ans, i = 0, 0
    # while i < N - 2:    
    #     j = i + 1
    #     while j < N - 1:
    #         kmax = bisect_left(L, L[i] + L[j])
    #         ans += kmax - j - 1
    #         j += 1
    #     i += 1

