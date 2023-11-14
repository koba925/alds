def resolve():
    N = int(input())
    D = [int(e) for e in input().split()]

    ans = 0
    for month, days in enumerate(D, 1):
        for d in range(1, days + 1):
            ss = str(month) + str(d)
            for s in ss:
                if s != ss[0]: break
            else:
                ans += 1

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
        input = """12
31 29 31 30 31 30 31 31 30 31 30 31"""
        output = """13"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
10 1 2 3 4 5 6 7 8 100"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """30
73 8 55 26 97 48 37 47 35 55 5 17 62 2 60 23 99 73 34 75 7 46 82 84 29 41 32 31 52 32"""
        output = """15"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
