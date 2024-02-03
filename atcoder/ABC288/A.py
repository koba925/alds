def resolve():
    N = int(input())
    for _ in range(N): print(sum([int(e) for e in input().split()]))

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
3 5
2 -6
-5 0
314159265 123456789"""
        output = """8
-4
-5
437616054"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
