def resolve():
    N, M = [int(e) for e in input().split()]
    S = input()

    muji = logo = max_logo = 0
    for s in S:
        match s:
            case "0": 
                muji = logo = 0
            case "1": 
                if muji < M:
                    muji += 1
                else:
                    logo += 1
                    max_logo = max(max_logo, logo)
            case "2":
                logo += 1
                max_logo = max(max_logo, logo)
    print(max_logo)

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
        input = """6 1
112022"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 1
222"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 1
01"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
