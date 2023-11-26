def resolve_at_contest():
    N, L, R = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]

    print(*[
        L if a <= L else
        R if R <= a else
        a
        for a in A
    ])

def resolve():
    N, L, R = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]

    print(*[min(max(L, a), R) for a in A])

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
        input = """5 4 7
3 1 4 9 7"""
        output = """4 4 4 7 7"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 10 10
11 10 9"""
        output = """10 10 10"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
