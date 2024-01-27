def resolve_set():
    def gap_existence(N, X, A):
        if X == 0: return True
        B = set()
        for a in A:
            if a + X in B or a - X in B:
                return True
            B.add(a)

        return False
    
    N, X = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]
    print("Yes" if gap_existence(N, X, A) else "No")

def resolve():
    N, X = [int(e) for e in input().split()]
    A = sorted(int(e) for e in input().split())

    i = j = 0
    while i < N and j < N:
        if A[j] - A[i] > X: i += 1
        elif A[j] - A[i] < X: j += 1
        else:
            print("Yes")
            break
    else: print("No")

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
3 1 4 1 5 9"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 -4
-2 -7 -1 -8 -2 -8"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 0
141421356 17320508"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
