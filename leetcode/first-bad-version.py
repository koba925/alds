# def isBadVersion(version: int) -> bool:
#     return n >= 3

class Solution:
    def firstBadVersion(self, n: int) -> int:
        good = 0
        bad = n + 1
        while good + 1 < bad:
            mid = (good + bad) // 2
            if isBadVersion(mid):
                bad = mid
            else:
                good = mid
        return bad

import unittest

class TestClass(unittest.TestCase):
    def test_find_in_the_middle(self):
        globals()["isBadVersion"] = lambda version: version >= 3
        self.assertEqual(Solution().firstBadVersion(5), 3)

    def test_bad_version_far_too_small(self):
        globals()["isBadVersion"] = lambda version: version >= -10
        self.assertEqual(Solution().firstBadVersion(5), 1)

    def test_bad_version_too_small(self):
        globals()["isBadVersion"] = lambda version: version >= 0
        self.assertEqual(Solution().firstBadVersion(5), 1)

    def test_find_at_left_edge(self):
        globals()["isBadVersion"] = lambda version: version >= 1
        self.assertEqual(Solution().firstBadVersion(5), 1)

    def test_find_at_right_edge(self):
        globals()["isBadVersion"] = lambda version: version >= 5
        self.assertEqual(Solution().firstBadVersion(5), 5)

    def test_version_too_large(self):
        globals()["isBadVersion"] = lambda version: version >= 6
        self.assertEqual(Solution().firstBadVersion(5), 6)

    def test_version_far_too_large(self):
        globals()["isBadVersion"] = lambda version: version >= 10
        self.assertEqual(Solution().firstBadVersion(5), 6)

unittest.main()