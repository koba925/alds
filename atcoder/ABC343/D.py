def resolve():
    import collections as cl

    N, T = [int(e) for e in input().split()]
    S = [0] * N
    D = cl.defaultdict(lambda: 0)
    D[0] = N
    for _ in range(T):
        a, b = [int(e) for e in input().split()]
        a -= 1
        before = S[a]
        S[a] += b
        after = S[a]
        if D[before] <= 1:
            del D[before]
        else:
            D[before] -= 1
        D[after] += 1
        print(len(D))

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
        input = """3 4
1 10
3 20
2 10
2 10"""
        output = """2
3
2
2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 3
1 3
1 4
1 3"""
        output = """1
1
1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 10
7 2620
9 2620
8 3375
1 3375
6 1395
5 1395
6 2923
10 3375
9 5929
5 1225"""
        output = """2
2
3
3
4
4
5
5
6
5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
