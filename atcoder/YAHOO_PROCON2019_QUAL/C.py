def hit_pocket(K, A, B):
    if B - 2 <= A:
        return 1 + K
    if K <= A:
        return 1 + K
    inc = (K - (A - 1)) // 2
    rest = (K - (A - 1)) % 2
    return A + inc * (B - A) + rest

def resolve():
    K, A, B = [int(e) for e in input().split()]
    print(hit_pocket(K, A, B))

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
        input = """4 2 6"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 3 4"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """314159265 35897932 384626433"""
        output = """48518828981938099"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
