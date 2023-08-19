import sys

sys.setrecursionlimit(2000000)

def debug(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)

def cookie_exchanges(A, B, C):
    count = 0
    past = set()
    while A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
        A, B, C = B // 2 + C // 2, A // 2 + C // 2, A // 2 + B // 2
        if (A, B, C) in past:
            return -1
        past.add((A, B, C))
        count += 1
    return count

def resolve():
    A, B, C = [int(e) for e in sys.stdin.readline().split()]
    print(cookie_exchanges(A, B, C))

# resolve()

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
        input = """4 12 20"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """14 14 14"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """454 414 444"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
