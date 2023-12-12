##
#### 494. Target Sum (medium)
#################################


## recursive
################
class Solution:
    def __init__(self):
        self.count = 0

    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        self.calculate(nums, 0, 0, target)
        return self.count

    def calculate(self, nums, i, total, target):
        if i == len(nums):
            if total == target:
                self.count += 1
        else:
            self.calculate(nums, i + 1, total + nums[i], target)
            self.calculate(nums, i + 1, total - nums[i], target)


## recursion with memoization
#################################
class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        idx = len(nums) - 1
        curr_sum = 0
        self.memo = {}
        return self.dp(nums, target, idx, curr_sum)

    def dp(self, nums, target, idx, curr_sum):
        if idx < 0 and curr_sum == target:
            return 1
        if idx < 0:
            return 0
        if (index, curr_sum) in self.memo:
            return self.memo[(index, curr_sum)]

        add = self.dp(nums, target, idx - 1, curr_sum + nums[idx])
        subtract = self.dp(nums, target, idx - 1, curr_sum - nums[idx])

        return add + subtract


## 2d dynamic programming
#############################
class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        pass


## 1d dynamic programming
#############################
class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.findTargetSumWays([1, 1, 1, 1, 1], 3), 5)
        self.assertEqual(solution.findTargetSumWays([1], 1), 1)


if __name__ == "__main__":
    unittest.main()
