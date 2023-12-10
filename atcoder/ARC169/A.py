def resolve_at_contest_WA():
    def debug(*args, **kwargs): print(*args, **kwargs, file=sys.stderr)

    def sign(n):
        return "+" if n > 0 else "-" if n < 0 else "0"

    N = int(input())
    A = [0] + [int(e) for e in input().split()]
    P = [0, 0] + [int(e) for e in input().split()]

    for _ in range(100):
        for i in range(2, N + 1):
            A[P[i]] += A[i]

    print(sign(A[1]))

def resolve_second_try_WA():
    import sys
    sys.setrecursionlimit(1000000)

    def sign(n):
        return "+" if n > 0 else "-" if n < 0 else "0"

    N = int(input())
    A = [0] + [int(e) for e in input().split()]
    P = [0, 0] + [int(e) for e in input().split()]

    G = [[] for _ in range(N + 1)]    
    for i, p in enumerate(P[2:], 2):
        G[p].append(i)


    def max_depth(p):
        return 1 + max(max_depth(q) for q in G[p]) if G[p] else 0
    
    def sum_at_depth(p, d):
        return A[p] if d == 0 else sum(sum_at_depth(q, d - 1) for q in G[p])

    depth = max_depth(1)
    dominant = sum_at_depth(1, depth)
    ans = A[1] if dominant == 0 else dominant
    print(sign(ans))

def resolve():
    N = int(input())
    A = [0] + [int(e) for e in input().split()]
    P = [0, 0] + [int(e) for e in input().split()]

    D = [0] * (N + 1)
    for i, p in enumerate(P[2:], 2):
        D[i] = D[p] + 1

    S = [0] * (N + 1)
    for d, a in zip(D, A):
        S[d] += a

    for s in reversed(S):
        if s < 0: print("-"); break
        elif s > 0: print("+"); break
    else:
        print("0")

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

    def test_1(self):
        input = """3
1 0 0
3 2"""
        output = """+"""
        self.assertIO(input, output)
    
    def test_入力例_1(self):
        input = """4
1 -2 3 -4
1 2 3"""
        output = """-"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
0 1 -1
1 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
1 -1 1 -1 1
1 1 2 2"""
        output = """+"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """20
568273618 939017124 -32990462 -906026662 403558381 -811698210 56805591 0 436005733 -303345804 96409976 179069924 0 0 0 -626752087 569946496 0 0 0
1 1 1 4 4 6 7 2 2 3 3 8 13 14 9 9 15 18 19"""
        output = """+"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
