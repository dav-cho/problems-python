"""
1480. Running Sum of 1d Array (easy)
"""

import unittest
from typing import List


# Sliding Window
class Solution:
    # i starts from 0
    def runningSum(self, nums: List[int]) -> List[int]:
        for i, num in enumerate(nums[1:]):
            nums[i + 1] = nums[i] + num
        return nums

    # Same array
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]
        return nums

    # Seperate array
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [nums[0]]
        for i in range(1, len(nums)):
            res.append(nums[i] + res[-1])
        return res


## Tests
########################################################################################


class Test(unittest.TestCase):
    def test_cases(self):
        for nums, expected in [
            ([1, 2, 3, 4], [1, 3, 6, 10]),
            ([1, 1, 1, 1, 1], [1, 2, 3, 4, 5]),
            ([3, 1, 2, 10, 1], [3, 4, 6, 16, 17]),
        ]:
            self.assertEqual(Solution().runningSum(nums), expected)


if __name__ == "__main__":
    unittest.main()
