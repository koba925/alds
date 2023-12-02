def resolve():
    N, A, B = [int(e) for e in input().split()]
    C = [int(e) for e in input().split()]
    R = {c:i for i, c in enumerate(C, 1)}
    print(R[A + B])

def resolve():
    N, A, B = [int(e) for e in input().split()]
    C = [int(e) for e in input().split()]
    print(C.index(A + B) + 1)

def resolve():
    N, A, B = [int(e) for e in input().split()]
    C = [int(e) for e in input().split()]
    for i in range(N):
        if C[i] == A + B:
            print(i + 1)
            break

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
        input = """3 125 175
200 300 400"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 1 1
2"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 123 456
135 246 357 468 579"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
