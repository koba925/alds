def resolve():
    N = int(input())
    A = [int(e) - 1 for e in input().split()]
    B = {a: i for i, a in enumerate(A)}

    ans = []
    a = B[-2]
    ans.append(a + 1)
    for _ in range(N - 1):
        a = B[a]
        ans.append(a + 1)
    print(*ans)

def resolve():
    N = int(input())
    A = [0 if e == -1 else e for e in [int(e) for e in input().split()]]

    ans = []

    B = [-1] * (N + 1)
    for i, a in enumerate(A, 1):
        B[a] = i

    a = B[0]
    while a != -1:
        ans.append(a)
        a = B[a]
    
    print(*ans)

def resolve():
    N = int(input())
    A = [int(e) - 1 for e in input().split()]

    ans = []
    B = [-1] * N
    for i, a in enumerate(A):
        if a == -2:
            b = i
        else:
            B[a] = i
   
    while b != -1:
        ans.append(b + 1)
        b = B[b]
    
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
        input = """6
4 1 -1 5 3 2"""
        output = """3 5 4 1 2 6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
-1 1 2 3 4 5 6 7 8 9"""
        output = """1 2 3 4 5 6 7 8 9 10"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """30
3 25 20 6 18 12 26 1 29 -1 21 17 23 9 8 30 10 15 22 27 4 13 5 11 16 24 28 2 19 7"""
        output = """10 17 12 6 4 21 11 24 26 7 30 16 25 2 28 27 20 3 1 8 15 18 5 23 13 22 19 29 9 14"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
