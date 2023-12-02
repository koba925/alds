def boundary(arr, is_ok):
    ng, ok = -1, len(arr)
    while ng + 1 < ok:
        mid = (ng + ok) // 2
        if is_ok(arr[mid]):
            ok = mid
        else:
            ng = mid
    return ok

def leftmost(nums, target):
    b = boundary(nums, lambda n: target <= n)
    return b if 0 <= b < len(nums) and nums[b] == target else -1 

def rightmost(nums, target):
    b = boundary(nums, lambda n: target < n) - 1
    return b if 0 <= b < len(nums) and nums[b] == target else -1 

def searchRange(nums: list[int], target: int) -> list[int]:
    left = leftmost(nums, target)
    right = rightmost(nums, target)
    return [left, right]

import unittest
class TestClass(unittest.TestCase):

    def test_1(self):
        self.assertEqual(searchRange([3, 3, 5, 5, 7, 7], 2), [-1, -1])

    def test_2(self):
        self.assertEqual(searchRange([3, 3, 5, 5, 7, 7], 3), [0, 1])

    def test_3(self):
        self.assertEqual(searchRange([3, 3, 5, 5, 7, 7], 4), [-1, -1])

    def test_4(self):
        self.assertEqual(searchRange([3, 3, 5, 5, 7, 7], 5), [2, 3])

    def test_5(self):
        self.assertEqual(searchRange([3, 3, 5, 5, 7, 7], 6), [-1, -1])

    def test_6(self):
        self.assertEqual(searchRange([3, 3, 5, 5, 7, 7], 7), [4, 5])

    def test_7(self):
        self.assertEqual(searchRange([3, 3, 5, 5, 7, 7], 8), [-1, -1])

unittest.main()