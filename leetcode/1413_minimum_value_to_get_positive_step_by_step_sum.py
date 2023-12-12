"""
1413. Minimum Value to Get Positive Step by Step Sum (easy)
"""

import unittest
from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        t = s = 0

        for num in nums:
            t += num
            s = min(s, t)

        return -s + 1


## Tests
########################################################################################


class Test(unittest.TestCase):
    def test_cases(self):
        for nums, expected in [
            ([-3, 2, -3, 4, 2], 5),
            ([1, 2], 1),
            ([1, -2, -3], 5),
        ]:
            self.assertEqual(Solution().minStartValue(nums), expected)


if __name__ == "__main__":
    unittest.main()
