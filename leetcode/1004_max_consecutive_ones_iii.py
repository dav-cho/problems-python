"""
1004. Max Consecutive Ones III (medium)
"""

from typing import List
import unittest


# Sliding Window
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        for r in range(len(nums)):
            k -= 1 - nums[r]
            if k < 0:
                k += 1 - nums[l]
                l += 1

        return r - l + 1


## Tests
########################################################################################


class Test(unittest.TestCase):
    def test_cases(self):
        for nums, k, expected in [
            ([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2, 6),
            ([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3, 10),
        ]:
            self.assertEqual(Solution().longestOnes(nums, k), expected)


if __name__ == "__main__":
    unittest.main()
