def resolve():
    L, R = [int(e) for e in input().split()]

    min_rem = float("inf")
    for i in range(L, R):
        for j in range(i + 1, R + 1):
            min_rem = min(min_rem, i * j % 2019)
            if min_rem == 0:
                print(0)
                exit()                
    print(min_rem)

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
        input = """2020 2040"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 5"""
        output = """20"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
