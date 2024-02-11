def resolve():
    A, B, D = [int(e) for e in input().split()]

    ans = []
    while A <= B:
        ans.append(A)
        A += D
    print(*ans)

def resolve():
    A, B, D = [int(e) for e in input().split()]

    print(*range(A, B + 1, D))

# resolve()
# exit()


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
        input = """3 9 2"""
        output = """3 5 7 9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 10 1"""
        output = """10"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
