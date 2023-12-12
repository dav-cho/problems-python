"""
643. Maximum Average Subarray I (easy)
"""

import unittest
from typing import List


# Sliding Window
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = curr_sum = sum(nums[:k])
        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, curr_sum)

        return max_sum / k


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = curr = sum(nums[:k])

        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            res = max(res, curr)

        return res / k

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = 0
        for i in range(k):
            curr += nums[i]

        res = curr
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            res = max(res, curr)

        return res / k


# Cumulative Sum
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums = [nums[0]]

        for i in range(1, len(nums)):
            sums.append(nums[i] + sums[-1])

        res = sums[k - 1]
        for i in range(k, len(nums)):
            res = max(res, sums[i] - sums[i - k])

        return res / k


## Tests
########################################################################################


class Test(unittest.TestCase):
    def test_cases(self):
        for nums, k, expected in [
            ([1, 12, -5, -6, 50, 3], 4, 12.75000),
            ([5], 1, 5.00000),
        ]:
            self.assertEqual(Solution().findMaxAverage(nums, k), expected)


if __name__ == "__main__":
    unittest.main()
