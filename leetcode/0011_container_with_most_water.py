"""
11. Container With Most Water (medium)
"""

from typing import List
import unittest


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        res = float("-Inf")
        while left < right:
            area = (right - left) * min(height[left], height[right])
            res = max(res, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return int(res)


## Tests
########################################################################################


class Test(unittest.TestCase):
    def test_cases(self):
        for height, expected in [
            ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
            ([1, 1], 1),
        ]:
            self.assertEqual(Solution().maxArea(height), expected)


if __name__ == "__main__":
    unittest.main()
