##
#### 136. Single Number (easy)
########################################


## bit manipulation
##############################
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        x = 0

        for num in nums:
            x ^= num

        return x


## math
##############################
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return sum(set(nums)) * 2 - sum(nums)


## hash table
##############################
from collections import Counter


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        counts = Counter(nums)

        for num, count in counts.items():
            if count == 1:
                return num


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.singleNumber([2, 2, 1]), 1)
        self.assertEqual(solution.singleNumber([4, 1, 2, 1, 2]), 4)
        self.assertEqual(solution.singleNumber([1]), 1)


if __name__ == "__main__":
    unittest.main()
