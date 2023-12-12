"""
2270. Number of Ways to Split Array (medium)
"""

from typing import List
import unittest


# Sliding Window
class Solution:
    # O(1) space
    def waysToSplitArray(self, nums: List[int]) -> int:
        res = l = 0
        t = sum(nums)
        for i in range(len(nums) - 1):
            l += nums[i]
            if l >= t - l:
                res += 1
        return res

    # O(n) space
    def waysToSplitArray(self, nums: List[int]) -> int:
        p = [nums[0]]
        for i in range(1, len(nums)):
            p.append(nums[i] + p[-1])

        res = 0
        for i in range(len(nums) - 1):
            if p[i] >= p[-1] - p[i]:
                res += 1

        return res


## Tests
########################################################################################


class Test(unittest.TestCase):
    def test_cases(self):
        for nums, expected in [
            ([10, 4, -8, 7], 2),
            ([2, 3, 1, 0], 2),
            ([6, -1, 9], 0),
        ]:
            self.assertEqual(Solution().waysToSplitArray(nums), expected)


if __name__ == "__main__":
    unittest.main()
