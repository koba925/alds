def resolve():
    def rows():
        for r in range(9):
            exists = [False] * 9
            for c in range(9):
                exists[A[r][c] - 1] = True
            if not all(exists):
                return False
        return True
    
    def cols():
        for c in range(9):
            exists = [False] * 9
            for r in range(9):
                exists[A[r][c] - 1] = True
            if not all(exists):
                return False
        return True

    def squares():
        for t in (0, 3, 6):
            for l in (0, 3, 6):
                exists = [False] * 9
                for r in range(3):
                    for c in range(3):
                        exists[A[t + r][l + c] - 1] = True
                if not all(exists):
                    return False
        return True

    A = [[int(e) for e in input().split()] for _ in range(9)]
    print("Yes" if rows() and cols() and squares() else "No")


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
        input = """1 2 3 4 5 6 7 8 9
4 5 6 7 8 9 1 2 3
7 8 9 1 2 3 4 5 6
2 3 4 5 6 7 8 9 1
5 6 7 8 9 1 2 3 4
8 9 1 2 3 4 5 6 7
3 4 5 6 7 8 9 1 2
6 7 8 9 1 2 3 4 5
9 1 2 3 4 5 6 7 8"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 2 3 4 5 6 7 8 9
2 3 4 5 6 7 8 9 1
3 4 5 6 7 8 9 1 2
4 5 6 7 8 9 1 2 3
5 6 7 8 9 1 2 3 4
6 7 8 9 1 2 3 4 5
7 8 9 1 2 3 4 5 6
8 9 1 2 3 4 5 6 7
9 1 2 3 4 5 6 7 8"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 2 3 4 5 6 7 8 9
4 5 6 7 8 9 1 2 3
7 8 9 1 2 3 4 5 6
1 2 3 4 5 6 7 8 9
4 5 6 7 8 9 1 2 3
7 8 9 1 2 3 4 5 6
1 2 3 4 5 6 7 8 9
4 5 6 7 8 9 1 2 3
7 8 9 1 2 3 4 5 6"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
