def resolve():
    def tmatch(A, B):
        def _tmatch(top, left):
            for row in range(M):
                for col in range(M):
                    if A[top + row][left + col] != B[row][col]:
                        return False
            return True
        
        for top in range(N - M + 1):
            for left in range(N - M + 1):
                if _tmatch(top, left): return True
        return False                        

    N, M = [int(e) for e in input().split()]
    A = [input() for _ in range(N)]
    B = [input() for _ in range(M)]
    print("Yes" if tmatch(A, B) else "No")

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
        input = """3 2
#.#
.#.
#.#
#.
.#"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 1
....
....
....
....
#"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
