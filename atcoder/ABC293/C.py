def resolve():
    def solve(H, W, A):
        def dfs(row, col, nums):
            if A[row][col] in nums: return 0
            if row == H - 1 and col == W - 1: return 1
            nums.add(A[row][col])
            right = 0 if col == W - 1 else dfs(row, col + 1, nums)
            down =  0 if row == H - 1 else dfs(row + 1, col, nums)
            nums.remove(A[row][col])
            return right + down
        
        return dfs(0, 0, set())
    
    H, W = [int(e) for e in input().split()]
    A = [[int(e) for e in input().split()] for _ in range(H)]
    print(solve(H, W, A))


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
3 2 2
2 1 3
1 5 4"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 10
1 2 3 4 5 6 7 8 9 10
11 12 13 14 15 16 17 18 19 20
21 22 23 24 25 26 27 28 29 30
31 32 33 34 35 36 37 38 39 40
41 42 43 44 45 46 47 48 49 50
51 52 53 54 55 56 57 58 59 60
61 62 63 64 65 66 67 68 69 70
71 72 73 74 75 76 77 78 79 80
81 82 83 84 85 86 87 88 89 90
91 92 93 94 95 96 97 98 99 100"""
        output = """48620"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
