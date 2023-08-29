# LL: 組み合わせには itertools.combinations を使う

import sys

sys.setrecursionlimit(2000000)


def debug(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)


C = sum(([10**n, 5 * 10**n] for n in range(10)), [])


def coins(price):
    ret = 0
    for c in reversed(C):
        n, price = divmod(price, c)
        ret += n
    return ret


def try_coins_self(N, K, A):
    def combinations(i, n, total):
        nonlocal min_coins
        # debug(i, n, total, used)
        if n == K:
            min_coins = min(min_coins, coins(total))
            return
        # if i == N or i + (K - n) > N:
        if i + (K - n) > N:
            return
        combinations(i + 1, n, total)
        # used[i] = True
        combinations(i + 1, n + 1, total + A[i])
        # used[i] = False

    # used = [False] * N
    min_coins = float("inf")
    combinations(0, 0, 0)
    return min_coins


import itertools as it


def try_coins(N, K, A):
    return min(coins(sum(prices)) for prices in it.combinations(A, K))


def resolve():
    N, K = [int(e) for e in sys.stdin.readline().split()]
    A = [int(e) for e in sys.stdin.readline().split()]
    print(try_coins(N, K, A))


# resolve()
# exit()

import unittest
from io import StringIO
import sys


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
25 29 62"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 1
10000 2 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 3
1415 9265 3589 7932 3846 2643 3832 7950 2884 1971"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
