def resolve():
    import collections as cl
    
    N = int(input())
    A = [int(e) for e in input().split()]
    ans = cl.deque()
    for i, a in enumerate(A):
        if i % 2 == N % 2:
            ans.append(a)
        else:
            ans.appendleft(a)

    print(*ans)

def resolve():
    N = int(input())
    left, right = [], []
    for i, a in enumerate(input().split()):
        (right if i % 2 == N % 2 else left).append(a)
    print(*reversed(left), *right)

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
1 2 3 4"""
        output = """4 2 1 3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
1 2 3"""
        output = """3 1 2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1
1000000000"""
        output = """1000000000"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """6
0 6 7 6 7 0"""
        output = """0 6 6 0 7 7"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
