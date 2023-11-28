def resolve():
    import collections as cl

    MOD = 10 ** 9 + 7
    sub_mod = lambda a, b: (a - b) % MOD
    mul_mod = lambda a, b: (a * b) % MOD

    N = int(input())
    C = cl.Counter(input())

    ans = 1
    for c in C.values():
        ans = mul_mod(ans, c + 1)
    ans = sub_mod(ans, 1)
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
        input = """4
abcd"""
        output = """15"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
baa"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
abcab"""
        output = """17"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
