def resolve():
    N, P, Q, R, S = [int(e) for e in input().split()]
    P, Q, R, S = P - 1, Q - 1, R - 1, S - 1
    A = [int(e) for e in input().split()]
    B = A[:P] + A[R:S + 1] + A[Q + 1:R] + A[P:Q + 1] + A[S + 1:]
    print(*B)

def resolve():
    N, P, Q, R, S = [int(e) for e in input().split()]
    P, Q, R, S = P - 1, Q - 1, R - 1, S - 1
    G = R - P
    A = [int(e) for e in input().split()]

    B = []
    for i in range(N):
        if P <= i <= Q:
            B.append(A[i + G])
        elif R <= i <= S:
            B.append(A[i - G])
        else:
            B.append(A[i]) 
    print(*B)

def resolve():
    N, P, Q, R, S = [int(e) for e in input().split()]
    P, Q, R, S = P - 1, Q - 1, R - 1, S - 1
    A = [int(e) for e in input().split()]
    A[P:Q+1], A[R:S+1] = A[R:S+1], A[P:Q+1]
    print(*A)

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
        input = """8 1 3 5 7
1 2 3 4 5 6 7 8"""
        output = """5 6 7 4 1 2 3 8"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 2 3 4 5
2 2 1 1 1"""
        output = """2 1 1 2 1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 1 1 2 2
50 100"""
        output = """100 50"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10 2 4 7 9
22 75 26 45 72 81 47 29 97 2"""
        output = """22 47 29 97 72 81 75 26 45 2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
