def islands_and_bridges_mine(N, A):
    total = sum(A)
    if total % N != 0:
        return -1

    per_island = total // N
    bridges = 0
    group_count, group_pop = 0, 0
    for a in A:
        group_count += 1
        group_pop += a
        if group_count * per_island != group_pop:
            bridges += 1
        else:
            group_count, group_pop = 0, 0
    return bridges


def resolve_mine():
    N = int(input())
    A = [int(e) for e in input().split()]
    print(islands_and_bridges_mine(N, A))


def islands_and_bridges(N, A):
    total = sum(A)
    if total % N != 0:
        return -1

    per_island = total // N
    bridges, left = 0, 0
    for k, a in enumerate(A, 1):
        left += a
        if left != per_island * k:
            bridges += 1
    return bridges


def resolve():
    N = int(input())
    A = [int(e) for e in input().split()]
    print(islands_and_bridges(N, A))


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
1 2 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """5
2 0 0 0 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """2
0 99"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """4
0 0 0 0"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
