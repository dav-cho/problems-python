"""
268. Missing Number (easy)
"""

import unittest
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """Hash set.

        Time complexity: O(n)
        Space complexity: O(n)
        """
        num_set = set(nums)
        for num in range(len(nums) + 1):
            if num not in num_set:
                return num

    def missingNumber(self, nums: List[int]) -> int:
        """Bit manipulation.

        Time complexity: O(n)
        Space complexity: O(1)
        """
        missing = len(nums)
        for i in range(missing):
            missing ^= i ^ nums[i]
        return missing

    def missingNumber(self, nums: List[int]) -> int:
        """Gauss' Formula.

        Time complexity: O(n)
        Space complexity: O(1)
        """
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)


## Tests ###############################################################################


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)
        self.assertEqual(Solution().missingNumber([0]), 1)


if __name__ == "__main__":
    unittest.main()
