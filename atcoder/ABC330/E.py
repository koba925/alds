def resolve():
    import collections as cl
    from sortedcontainers import SortedSet

    N, Q = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]

    max_mex = N + 1
    AS = set(A)
    G = SortedSet(b for b in range(max_mex + 1) if b not in AS)

    I = cl.defaultdict(set)
    for i, a in enumerate(A):
        I[a].add(i)

    for _ in range(Q):
        i, x = [int(e) for e in input().split()]
        i -= 1

        a = A[i]
        I[a].remove(i)
        if len(I[a]) == 0 and a <= max_mex: G.add(a)

        if len(I[x]) == 0 and x <= max_mex: G.remove(x)
        A[i] = x
        I[x].add(i)

        print(G[0])

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
        input = """8 5
2 0 2 2 1 1 2 5
4 3
4 4
6 3
8 1000000000
2 1"""
        output = """4
3
6
5
0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
