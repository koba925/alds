def resolve():
    N = int(input())
    S = [input() for _ in range(N)]

    P = sorted(
        enumerate([s.count("o") for s in S], 1), 
        key=lambda x: x[1],
        reverse=True
    )
    print(*[p[0] for p in P])

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
        input = """3
-xx
o-x
oo-"""
        output = """3 2 1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7
-oxoxox
x-xxxox
oo-xoox
xoo-ooo
ooxx-ox
xxxxx-x
oooxoo-"""
        output = """4 7 3 1 5 2 6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
