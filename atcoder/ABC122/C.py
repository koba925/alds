def resolve():
    import itertools as it
    
    N, Q = [int(e) for e in input().split()]
    S = input()
    LR = [[int(e) - 1 for e in input().split()] for _ in range(Q)]

    AC = [0] + list(it.accumulate(1 if a == "A" and c == "C" else 0 for a,c in it.pairwise(S)))
    print(*[AC[r] - AC[l] for l, r in LR], sep="\n")

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
        input = """8 3
ACACTACG
3 7
2 3
1 8"""
        output = """2
0
3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
