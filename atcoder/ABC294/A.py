def resolve():
    N = int(input())
    print(*[int(e) for e in input().split() if int(e) % 2 == 0])

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
1 2 3 5 6"""
        output = """2 6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
2 2 2 3 3"""
        output = """2 2 2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
22 3 17 8 30 15 12 14 11 17"""
        output = """22 8 30 12 14"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
