def resolve():
    def just_k():
        for row in range(N + 1):
            for col in range(M + 1):
                black = row * (M - col) + (N - row) * col
                if black == K:
                    return True
        return False

    N, M, K = [int(e) for e in input().split()]
    print("Yes" if just_k() else "No")
        

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
        input = """2 2 2"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 2 1"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 5 8"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """7 9 20"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
