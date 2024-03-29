def resolve():
    N, K = [int(e) for e in input().split()]
    S = input()

    ans = []
    qualified = 0
    for s in S:
        if s == "o" and qualified < K:
            ans.append("o")
            qualified += 1
        else:
            ans.append("x")
    print("".join(ans))


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
        input = """10 3
oxxoxooxox"""
        output = """oxxoxoxxxx"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
