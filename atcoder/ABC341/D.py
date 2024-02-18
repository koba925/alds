def resolve_TLE():
    N, M, K = [int(e) for e in input().split()]

    n, m, nums = N, M, []
    while n != m:
        if n < m:
            nums.append(n)
            n += N
        else:
            nums.append(m)
            m += M
        if len(nums) == K:
            print(nums[-1])
            break
    else:
        print(n * ((K - 1) // len(nums)) + nums[(K - 1) % len(nums)])

def resolve():
    import math
    
    N, M, K = [int(e) for e in input().split()]
    L = math.lcm(N, M)

    left, right = 0, 10 ** (8 + 8 + 10) + 1
    while left + 1 < right:
        mid = (left + right) // 2
        if mid // N + mid // M - mid // L * 2 < K:
            left = mid
        else:
            right = mid
    
    print(right)

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

    def test_my_1(self):
        input = """1 2 1"""
        output = """1"""
        self.assertIO(input, output)
    
    def test_入力例_1(self):
        input = """2 3 5"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 2 3"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100000000 99999999 10000000000"""
        output = """500000002500000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
