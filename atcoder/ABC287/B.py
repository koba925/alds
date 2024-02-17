def resolve():
    N, M = [int(e) for e in input().split()]
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    
    print(len([s for s in S if s[3:] in T]))


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
        input = """3 3
142857
004159
071028
159
287
857"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 4
235983
109467
823476
592801
000333
333
108
467
983"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 4
000000
123456
987111
000000
000
111
999
111"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
