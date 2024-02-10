def resolve():
    N, K = [int(e) for e in input().split()]
    S = [input() for _ in range(N)]
    print(*sorted(S[:K]), sep="\n")

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
        input = """5 3
abc
aaaaa
xyz
a
def"""
        output = """aaaaa
abc
xyz"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 4
z
zyx
zzz
rbg"""
        output = """rbg
z
zyx
zzz"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 1
abc
arc
agc"""
        output = """abc"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
