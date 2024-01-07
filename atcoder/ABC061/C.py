def resolve():
    import collections as cl

    N, K = [int(e) for e in input().split()]
    nums = cl.defaultdict(int)
    for _ in range(N):
        a, b = [int(e) for e in input().split()]
        nums[a] += b
    for a in sorted(nums.keys()):
        K -= nums[a]
        if K <= 0:
            print(a)
            break

def resolve():
    from sortedcontainers import SortedDict

    N, K = [int(e) for e in input().split()]
    nums = SortedDict()
    for _ in range(N):
        a, b = [int(e) for e in input().split()]
        nums[a] = nums.get(a, 0) + b
    for a, c in nums.items():
        K -= c
        if K <= 0:
            print(a)
            break

def resolve():
    N, K = [int(e) for e in input().split()]
    nums = [0] * 100001
    for _ in range(N):
        a, b = [int(e) for e in input().split()]
        nums[a] += b
    for a, c in enumerate(nums):
        K -= c
        if K <= 0:
            print(a)
            break

    

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
        input = """3 4
1 1
2 2
3 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 500000
1 100000
1 100000
1 100000
1 100000
1 100000
100000 100000
100000 100000
100000 100000
100000 100000
100000 100000"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
