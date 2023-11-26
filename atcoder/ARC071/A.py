def resolve():
    import collections as cl
    import string

    N = int(input())
    C = [cl.Counter(input()) for _ in range(N)]
    print("".join(a * min(c[a] for c in C) for a in string.ascii_lowercase))

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
cbaa
daacc
acacac"""
        output = """aac"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
a
aa
b"""
        output = """"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
