import sys

sys.setrecursionlimit(2000000)

def shortest(K, N, A):
    A.sort()
    dist_to_next = [A[i] - A[i - 1] for i in range(N)]
    return K - max(dist_to_next + [A[0] + (K - A[N - 1])])
    
def resolve():
    K, N = [int(e) for e in sys.stdin.readline().split()]
    A = [int(e) for e in sys.stdin.readline().split()]
    print(shortest(K, N, A))

resolve()

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
        input = """20 3
5 10 15"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """20 3
0 5 15"""
        output = """10"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
