import sys
from io import StringIO
import unittest

def resolve():
    import itertools as it

    N = int(input())
    S = input()
    C = [int(e) for e in input().split()]

    cost01 = [0 if p == s else c for p, s, c in zip(it.cycle("01"), S, C)]
    cost10 = [0 if p == s else c for p, s, c in zip(it.cycle("10"), S, C)]
    cost01a = list(it.accumulate(cost01, initial = 0))
    cost10a = list(it.accumulate(cost10, initial = 0))

    min_cost = float("inf")
    for i in range(1, N):
        min_cost = min(min_cost, cost01a[i] + cost10a[N] - cost10a[i])
        min_cost = min(min_cost, cost10a[i] + cost01a[N] - cost01a[i])

    print(min_cost)

class TestClass(unittest.TestCase):
    def test_my_1(self):
        input = """2
01
1 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_my_2(self):
        input = """2
00
1 2"""
        output = """0"""
        self.assertIO(input, output)
    
    
    def test_sample1(self):
        input = """5
00011
3 9 2 6 4"""
        expected = """7"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """4
1001
1 2 3 4"""
        expected = """0"""
        self.assertIO(input, expected)

    def test_sample3(self):
        input = """11
11111100111
512298012 821282085 543342199 868532399 690830957 973970164 928915367 954764623 923012648 540375785 925723427"""
        expected = """2286846953"""
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

