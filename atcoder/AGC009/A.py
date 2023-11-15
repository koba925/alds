def resolve():
    N = int(input())
    A, B = zip(*[[int(e) for e in input().split()] for _ in range(N)])

    ans = 0
    for i in reversed(range(N)):
        rem = (A[i] + ans) % B[i]
        ans += 0 if rem == 0 else B[i] - rem
    
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
        input = """3
3 5
2 7
9 4"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7
3 1
4 1
5 9
2 6
5 3
5 8
9 7"""
        output = """22"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
