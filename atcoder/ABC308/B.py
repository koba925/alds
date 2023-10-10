import sys
def resolve():
    N, M = [int(e) for e in input().split()]
    C = input().split()
    D = input().split()
    P = [int(e) for e in input().split()]

    price_tab = dict(zip(D, P[1:]))
    print(sum(price_tab[c] if c in price_tab else P[0] for c in C))

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
        input = """3 2
red green blue
blue red
800 1600 2800"""
        output = """5200"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 2
code queen atcoder
king queen
10 1 1"""
        output = """21"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
