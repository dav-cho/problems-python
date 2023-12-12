"""
1. Two Sum (easy)
"""

import unittest
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}

        for i, num in enumerate(nums):
            comp = target - num

            if comp in complements:
                return [complements[comp], i]

            complements[num] = i


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}

        for i in range(len(nums)):
            comp = target - nums[i]

            if comp in complements:
                return [complements[comp], i]

            complements[nums[i]] = i


## Tests
########################################################################################


class Test(unittest.TestCase):
    def test_cases(self):
        for nums, target, expected in [
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1]),
        ]:
            self.assertEqual(Solution().twoSum(nums, target), expected)


if __name__ == "__main__":
    unittest.main()
