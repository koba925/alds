def resolve():
    N = int(input())
    A = [int(e) for e in input().split()]

    called = [False] * N
    for i, a in enumerate(A):
        if not called[i]:
            called[a - 1] = True
    ans = [i + 1 for i, called in enumerate(called) if not called]
    print(len(ans))
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
        input = """5
3 1 4 5 4"""
        output = """2
2 4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """20
9 7 19 7 10 4 13 9 4 8 10 15 16 3 18 19 12 13 2 12"""
        output = """10
1 2 5 6 8 11 14 17 18 20"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
