import sys

sys.setrecursionlimit(2000000)

def nth_perm_1(N, target):
    def rec(l, perm, rest):
        nonlocal n

        if l == N:
            n += 1
            return perm == target
            
        for i in range(len(rest)):
            found = rec(l + 1, perm + [rest[i]], rest[:i] + rest[i + 1:])
            if found:
                return True
        return False
    
    n = 0
    rec(0, [], list(range(1, N + 1)))
    return n
        
def nth_perm_2(N, target):
    def rec(i):
        if i == N:
            nonlocal n
            n += 1
            return perm == target

        for j in range(N):
            if used[j]:
                continue
            perm[i] = orig[j]
            used[j] = True
            if rec(i + 1):
                return True
            used[j] = False
        return False

    orig = list(range(1, N + 1))
    used = [False] * N

    perm = [None] * N
    n = 0
    rec(0)
    return n

from itertools import permutations

def nth_perm_stdlib(N, target):
    t = tuple(target)
    for n, p in enumerate(permutations(range(1, N + 1), N), 1):
        if p == t:
            return n

def next_permutation(p):
    lp = len(p)
    l = r = lp - 1
    more = False

    while l >= 0:
        l -= 1
        if p[l] < p[l + 1]:
            break
    
    if l >= 0:
        more = True
        while p[l] > p[r]:
            r -= 1
        p[l], p[r] = p[r], p[l]

    l += 1
    r = lp - 1
    while l < r:
        p[l], p[r] = p[r], p[l]
        l += 1
        r -= 1
    
    return more

def nth_perm_next_permutation(N, target):
    n, p = 1, list(range(1, N + 1))

    while p != target:
        next_permutation(p)
        n += 1
    
    return n

def count_order(N, P, Q):
    a = nth_perm_2(N, P)
    b = nth_perm_2(N, Q)
    return abs(a - b)    

def resolve():
    N = int(sys.stdin.readline())
    P = [int(e) for e in sys.stdin.readline().split()]
    Q = [int(e) for e in sys.stdin.readline().split()]    
    print(count_order(N, P, Q))

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
1 3 2
3 1 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8
7 3 5 4 2 1 6 8
3 8 2 5 4 6 7 1"""
        output = """17517"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
1 2 3
1 2 3"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
