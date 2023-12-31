def resolve():
    N = int(input())
    H = [int(e) for e in input().split()]

    ans = 0
    for h in range(101):
        water = False
        for i in range(N):
            if not water and H[i] > 0:
                ans += 1
                water = True
            if H[i] == 0:
                water = False
            if H[i] > 0:
                H[i] -= 1
    print(ans)

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
1 2 2 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
3 1 2 3 1"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8
4 23 75 0 23 96 50 100"""
        output = """221"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
