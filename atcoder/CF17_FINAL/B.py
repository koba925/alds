def resolve():
    import collections as cl
    C = cl.Counter(input())
    print("YES" if max(C["a"], C["b"], C["c"]) <= min(C["a"], C["b"], C["c"]) + 1 else "NO")

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
        input = """abac"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """aba"""
        output = """NO"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """babacccabab"""
        output = """YES"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
