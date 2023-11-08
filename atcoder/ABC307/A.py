def resolve():
    N = int(input())
    A = [int(e) for e in input().split()]

    print(*[sum(A[i:i + 7]) for i in range(0, N * 7, 7)])

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
        input = """2
1000 2000 3000 4000 5000 6000 7000 2000 3000 4000 5000 6000 7000 8000"""
        output = """28000 35000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
14159 26535 89793 23846 26433 83279 50288 41971 69399 37510 58209 74944 59230 78164 6286 20899 86280 34825 34211 70679 82148"""
        output = """314333 419427 335328"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
