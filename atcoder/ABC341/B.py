def resolve1():
    N = int(input())
    A = [int(e) for e in input().split()]
    S, T = list(zip(*[[int(e) for e in input().split()] for _ in range(N - 1)]))

    for i in range(N - 1):
        A[i + 1] += A[i] // S[i] * T[i]
    
    print(A[N - 1])

def resolve2():
    N = int(input())
    A = [int(e) for e in input().split()]
    ST = [tuple([int(e) for e in input().split()]) for _ in range(N - 1)]

    for i in range(N - 1):
        A[i + 1] += A[i] // ST[i][0] * ST[i][1]
    
    print(A[N - 1])

def resolve():
    import collections as cl
    Exc = cl.namedtuple("Ex", "s, t")

    N = int(input())
    A = [int(e) for e in input().split()]
    exc = [Exc(*[int(e) for e in input().split()]) for _ in range(N - 1)]

    for i in range(N - 1):
        A[i + 1] += A[i] // exc[i].s * exc[i].t
    
    print(A[N - 1])

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
        input = """4
5 7 0 3
2 2
4 3
5 2"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
32 6 46 9 37 8 33 14 31 5
5 5
3 1
4 3
2 2
3 2
3 2
4 4
3 3
3 1"""
        output = """45"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
