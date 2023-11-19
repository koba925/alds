def resolve():
    N, Q = [int(e) for e in input().split()]
    C = [set([int(e)]) for e in input().split()]

    for _ in range(Q):
        a, b = [int(e) - 1 for e in input().split()]
        if len(C[a]) < len(C[b]):
            C[b] |= C[a]
            C[a] = set()
        else:
            C[a] |= C[b]
            C[b] = set()
            C[a], C[b] = C[b], C[a]
        print(len(C[b]))

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
        input = """6 5
1 1 1 2 2 3
1 2
6 4
5 1
3 6
4 6"""
        output = """1
2
1
1
3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 3
2 4 2 4 2
3 1
2 5
3 2"""
        output = """1
2
0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
