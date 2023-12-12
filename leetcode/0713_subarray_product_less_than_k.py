"""
Subarray Product Less Than K (medium)
"""

from typing import List
from functools import reduce
import unittest


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = res = 0
        curr = 1

        for right in range(len(nums)):
            curr *= nums[right]
            while left <= right and curr >= k:
                curr //= nums[left]
                left += 1
            res += right - left + 1

        return res


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        ans = left = 0
        product = 1

        for right, val in enumerate(nums):
            product *= val
            while product >= k:
                product //= nums[left]
                left += 1
            ans += right - left + 1

        return ans


## Tests
########################################################################################


class Test(unittest.TestCase):
    def test_cases(self):
        for nums, k, expected in [
            ([10, 5, 2, 6], 100, 8),
            ([1, 2, 3], 0, 0),
        ]:
            self.assertEqual(Solution().numSubarrayProductLessThanK(nums, k), expected)


if __name__ == "__main__":
    unittest.main()
