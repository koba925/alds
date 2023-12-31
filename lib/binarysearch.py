A = [1, 2, 2, 2, 3]

# 通常は https://docs.python.org/3/library/bisect.html を使う
# k以上の値でもっとも左に現れる要素のインデックスを返すので、
# 一致しているかを確認する必要がある

from bisect import bisect_left


def in_array(a, k) -> int:
    l = bisect_left(a, k)
    return l < len(a) and a[l] == k


# 最も左で一致する位置を返す
# 見つからなければ -1 を返す

# def binary_search(e, S):
#     left = -1
#     right = len(S)
#     while left < right - 1:
#         mid = (left + right) // 2
#         if e <= S[mid]:
#             right = mid
#         else:
#             left = mid
#     return right if right < len(S) and S[right] == e else -1
#
# print([binary_search(i, a) for i in range(5)])

# 条件を満たす最も左の位置を返す
# すべて満たせば0
# 全く満たさなければlen(S)

# def binary_search(is_ok, S):

#     def bisect(ng, ok, is_ok):
#         while abs(ok - ng) > 1:
#             mid = (ng + ok) // 2
#             if is_ok(mid):
#                 ok = mid
#             else:
#                 ng = mid
#         return ok
#
#     return bisect(-1, len(S), is_ok)
#
# print([binary_search(lambda n: i <= a[n], a) for i in range(5)])

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
