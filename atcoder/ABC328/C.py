def resolve():
    import itertools as it

    N, Q = [int(e) for e in input().split()]
    S = input()
    SS = [0] + list(it.accumulate(1 if a == b else 0 for a, b in it.pairwise(S)))

    for _ in range(Q):
        l, r = [int(e) for e in input().split()]
        print(SS[r - 1] - SS[l - 1])

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
        input = """11 4
mississippi
3 9
4 10
4 6
7 7"""
        output = """2
2
0
0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 1
aaaaa
1 5"""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
