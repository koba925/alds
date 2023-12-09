def resolve_contest():
    import itertools as it

    N = int(input())
    A = [int(e) for e in input().split()]

    S = sum(A)
    B = [0] * (10 ** 6 + 1)
    for a in A:
        B[a] += a
    C = list(it.accumulate(B))

    print(*[S - C[a] for a in A])

def resolve():
    import collections as cl

    N = int(input())
    A = [int(e) for e in input().split()]

    B = cl.defaultdict(list)
    for x, a in enumerate(A):
        B[a].append(x)

    ans = [0] * N
    s = 0
    for a, xs in reversed(sorted(B.items())):
        for x in xs:
            ans[x] = s
        s += a * len(xs)
    
    print(*ans)

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
        input = """5
1 4 1 4 2"""
        output = """10 0 10 0 8"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
31 42 59 26 53 58 97 93 23 54"""
        output = """456 414 190 487 361 249 0 97 513 307"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """50
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1"""
        output = """0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
