def resolve():
    import itertools as it

    repunits = [int("1" * n) for n in range(1, 13)]
    trios = list(it.combinations_with_replacement(repunits, 3))
    sum_trios = sorted(a + b + c for a, b, c in trios)
    print(sum_trios[int(input()) - 1])

def resolve():
    N = int(input())

    L = 12
    repunits = [int("1" * n) for n in range(1, L + 1)]

    for i in range(L):
        for j in range(i + 1):
            for k in range(j + 1):
                N -= 1
                if N == 0:
                    print(repunits[i] + repunits[j] + repunits[k])
                    exit()

resolve()
exit()

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
        input = """5"""
        output = """113"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """19"""
        output = """2333"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """333"""
        output = """112222222233"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
