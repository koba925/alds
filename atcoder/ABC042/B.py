import sys

def iroha_easy(N, L, S):
    return("".join(sorted(S)))

def resolve():
    N, L = [int(e) for e in sys.stdin.readline().split()]
    S = [sys.stdin.readline().strip() for _ in range(N)]

    print(iroha_easy(N, L, S))

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
        input = """3 3
dxx
axx
cxx"""
        output = """axxcxxdxx"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
