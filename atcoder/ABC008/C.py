# TODO: Get full mark

import sys

import itertools as it


def coin_TLE(N, C):
    total = 0
    for p in it.permutations(C):
        heads = [1] * N
        for i in range(N):
            for j in range(i + 1, N):
                if p[j] % p[i] == 0:
                    heads[j] = 1 - heads[j]
        total += sum(heads)
    return total / len(list(it.permutations(C)))

def coin(N, C):


def resolve():
    N = int(sys.stdin.readline())
    C = [int(sys.stdin.readline()) for _ in range(N)]
    print(coin(N, C))


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

    def test_入力例1(self):
        input = """3
2
4
8"""
        output = """2.166666666667"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """4
5
5
5
5"""
        output = """2.000000000000"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """5
2
3
2
6
12"""
        output = """3.100000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
