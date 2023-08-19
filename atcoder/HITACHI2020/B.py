import sys

def nice_shopping(A, a, B, b, M, m):
    return min(min(a) + min(b), min(a[x] + b[y] - c for x, y, c in m))

def resolve():
    A, B, M = [int(e) for e in sys.stdin.readline().split()]
    a = [int(e) for e in sys.stdin.readline().split()]
    b = [int(e) for e in sys.stdin.readline().split()]
    m = []
    for _ in range(M):
        x, y, c = [int(e) for e in sys.stdin.readline().split()]
        m.append([x - 1, y - 1, c])    
    print(nice_shopping(A, a, B, b, M, m))

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
        input = """2 3 1
3 3
3 3 3
1 2 1"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 1 2
10
10
1 1 5
1 1 10"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 2 1
3 5
3 5
2 2 2"""
        output = """6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
