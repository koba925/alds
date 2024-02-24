def resolve():
    N = int(input())
    S = input()

    for i in range(1, N):
        for l in range(1, N - i + 1):
            if S[l - 1] == S[l + i - 1]:
                print(l - 1)
                break
        else:
            print(l)

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
        input = """6
abcbac"""
        output = """5
1
2
0
1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
