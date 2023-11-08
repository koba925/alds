def resolve_tle():
    import sys
    sys.setrecursionlimit(2000000)

    import functools as ft

    N, A, B, C, D = [int(e) for e in input().split()]
    S = "_" + input()

    @ft.cache
    def rec(s, f):
        if s == A and f == B:
            return True
        if s - 1 >= A and S[s - 1] != "#" and s - 1 != f:
            if rec(s - 1, f): return True
        if s - 2 >= A and S[s - 2] != "#" and s - 2 != f:
            if rec(s - 2, f): return True
        if f - 1 >= B and S[f - 1] != "#" and f - 1 != s:
            if rec(s, f - 1): return True
        if f - 2 >= B and S[f - 2] != "#" and f - 2 != s:
            if rec(s, f - 2): return True
        return False

    print("Yes" if rec(C, D) else "No")

def resolve():

    def pass_by():
        nonlocal A, B, C, D
        
        while A < B:
            if A + 1 <= C and S[A + 1] == "." and A + 1 != B:
                A += 1
            elif A + 2 <= C and S[A + 2] == "." and A + 2 != B:
                A += 2
            elif B + 1 <= D and S[B + 1] == ".":
                B += 1
            elif B + 2 <= D and S[B + 2] == ".":
                B += 2
            else:
                return False
        return True
    
    def go(i, g):
        while i < g:
            if S[i + 1] == ".":
                i += 1
            elif S[i + 2] == ".":
                i += 2
            else:
                return False
        return True

    def kenken():
        nonlocal A, B, C, D
        
        if D < C:
            if not pass_by():
                return False
            A, B, C, D = B, A, D, C
        return go(B, D) and go(A, C)
    
    N, A, B, C, D = [int(e) for e in input().split()]
    S = "_" + input()

    print("Yes" if kenken() else "No")

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
        input = """7 1 3 6 7
.#..#.."""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 1 3 7 6
.#..#.."""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """15 1 3 15 13
...#.#...#.#..."""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
