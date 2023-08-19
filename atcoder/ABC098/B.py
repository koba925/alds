import sys

def cut_and_count(N, S):
    return max([len(set(S[:i]) & set(S[i:])) for i in range(N)])

def resolve():
    N = int(sys.stdin.readline())
    S = sys.stdin.readline().strip() 
    print(cut_and_count(N, S))

# resolve()

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
aabbca"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
aaaaaaaaaa"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """45
tgxgdqkyjzhyputjjtllptdfxocrylqfqjynmfbfucbir"""
        output = """9"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
