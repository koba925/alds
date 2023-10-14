def resolve():
    N = int(input())
    A = [int(e) for e in input().split()]
    B = [0] * N
    F = []

    for i, a in enumerate(A):
        B[a - 1] += 1
        if B[a - 1] == 2: F.append((i, a))
    F.sort()
    print(*[a for _, a in F])

def resolve():
    N = int(input())
    A = [int(e) for e in input().split()]

    cnt = [0] * N
    ans = []

    for i in A:
        cnt[i - 1] += 1
        if cnt[i - 1] == 2: ans.append(i)

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
        input = """3
1 1 3 2 3 2 2 3 1"""
        output = """1 3 2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1
1 1 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
2 3 4 3 4 1 3 1 1 4 2 2"""
        output = """3 4 1 2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
