def resolve():
    def alf_to_i(c: str) -> int: return ord(c) - ord("A") + 1

    S = input()

    ans = 0
    for s in S:
        ans *= 26
        ans += alf_to_i(s)
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
        input = """AB"""
        output = """28"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """C"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """BRUTMHYHIIZP"""
        output = """10000000000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
