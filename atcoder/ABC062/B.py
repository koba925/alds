import sys  # https://docs.python.org/ja/3/library/sys.html


def resolve():
    H, W = [int(e) for e in sys.stdin.readline().split()]
    A = [sys.stdin.readline().strip() for _ in range(H)]
    print("#" * (W + 2))
    for a in A:
        print("#" + a + "#")
    print("#" * (W + 2))


def resolve():
    H, W = [int(e) for e in sys.stdin.readline().split()]
    A = [list(sys.stdin.readline().strip()) for _ in range(H)]
    B = [["#"] * (W + 2)]
    for a in A:
        B.append(["#"] + a + ["#"])
    B.append(["#"] * (W + 2))

    for b in B:
        print("".join(b))


def resolve():
    H, W = [int(e) for e in sys.stdin.readline().split()]
    A = [list(sys.stdin.readline().strip()) for _ in range(H)]

    B = [["#"] * (W + 2) for _ in range(H + 2)]
    for r in range(H):
        for c in range(W):
            B[r + 1][c + 1] = A[r][c]

    for b in B:
        print("".join(b))


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
        input = """2 3
abc
arc"""
        output = """#####
#abc#
#arc#
#####"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 1
z"""
        output = """###
#z#
###"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
