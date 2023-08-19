import sys

def exception_handling_sort(N, A):
    first, second = sorted(A, reverse=True)[0:2]
    return (second if a == first else first for a in A)

def exception_handling_leftright(N, A):
    max_left = [0] * N
    for i in range(1, N):
        max_left[i] = max(max_left[i - 1], A[i - 1])    

    max_right = [0] * N
    for i in reversed(range(N - 1)):
        max_right[i] = max(max_right[i + 1], A[i + 1])    

    return (max(max_left[i], max_right[i]) for i in range(N))

def resolve():
    N = int(sys.stdin.readline())
    A = [int(sys.stdin.readline()) for _ in range(N)]

    print(*exception_handling_leftright(N, A), sep="\n")    

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
1
4
3"""
        output = """4
3
4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
5
5"""
        output = """5
5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
