def resolve():
    A, B, C = [int(e) for e in input().split()]

    count = 0
    while A != B or B != C:
        count += 1
        m = min(A, B, C)
        if A == B == m:
            A += 1
            B += 1
        elif B == C == m:
            B += 1
            C += 1
        elif C == A == m:
            C += 1
            A += 1
        elif A == m:
            A += 2
        elif B == m:
            B += 2
        else:
            C += 2

    print(count)


def resolve():
    A = [int(e) for e in input().split()]
    M = max(A)
    S = sum(A)
    if M % 2 == S % 2:
        print((3 * M - S) // 2)
    else:
        print((3 * (M + 1) - S) // 2)


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
        input = """2 5 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 6 3"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """31 41 5"""
        output = """23"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
