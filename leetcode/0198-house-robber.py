##
#### 198. House Robber (medium)
########################################


## best - from discuss solutions
####################################
class Solution:
    def rob(self, nums: list[int]) -> int:
        prev = curr = 0

        for num in nums:
            prev, curr = curr, max(curr, prev + num)

        return curr


## top-down to bottom-up
############################################
class Solution:
    def rob(self, nums: list[int]) -> int:
        def dp(i):
            if i == 0:
                return nums[0]
            elif i == 1:
                return max(nums[0], nums[1])

            if i not in memo:
                memo[i] = max(dp(i - 1), dp(i - 2) + nums[i])

            return memo[i]

        memo = {}
        return dp(len(nums) - 1)


class Solution:
    def rob(self, nums: list[int]) -> int:
        N = len(nums)

        if N == 0:
            return nums[0]

        dp = [0] * N
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, N):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[N - 1]


## optimized dynamic programming - bottom up
################################################
class Solution:
    def rob(self, nums: list[int]) -> int:
        N = len(nums)
        prev = 0
        curr = nums[0]

        for i in range(N - 2, -1, -1):
            prev, curr = curr, max(curr, prev + nums[i])

        return curr


class Solution:
    def rob(self, nums: list[int]) -> int:
        next_next_house = 0
        next_house = nums[0]

        for i in range(1, len(nums)):
            curr = max(next_house, next_next_house + nums[i])
            next_next_house = next_house
            next_house = curr

        return next_house


class Solution:
    def rob(self, nums: list[int]) -> int:
        N = len(nums)
        next_next_house = 0
        next_house = nums[0]

        for i in range(1, N):
            next_next_house, next_house = next_house, max(
                next_house, next_next_house + nums[i]
            )

        return next_house


## optimized dynamic programming - top down
###############################################
class Solution:
    def rob(self, nums: list[int]) -> int:
        N = len(nums)
        prev = 0
        curr = nums[N - 1]

        for i in range(N - 2, -1, -1):
            prev, curr = curr, max(curr, prev + nums[i])

        return curr


class Solution:
    def rob(self, nums: list[int]) -> int:
        N = len(nums)
        next_next_house = 0
        next_house = nums[N - 1]

        for i in range(N - 2, -1, -1):
            next_next_house, next_house = next_house, max(
                next_house, next_next_house + nums[i]
            )

        return next_house


## dp bottom-up iterative (tabulation)
##########################################
class Solution:
    def rob(self, nums: list[int]) -> int:
        N = len(nums)
        memo = {}
        memo[N] = 0
        memo[N - 1] = nums[N - 1]

        for i in range(N - 2, -1, -1):
            memo[i] = max(memo[i + 1], memo[i + 2] + nums[i])

        return memo[0]


class Solution:
    def rob(self, nums: list[int]) -> int:
        N = len(nums)
        memo = [None] * (N - 1) + [nums[N - 1], 0]

        for i in range(N - 2, -1, -1):
            memo[i] = max(memo[i + 1], memo[i + 2] + nums[i])

        return memo[0]


class Solution:
    def rob(self, nums: list[int]) -> int:
        N = len(nums)
        memo = {N: 0, N - 1: nums[N - 1]}

        for i in range(N - 2, -1, -1):
            memo[i] = max(memo[i + 1], memo[i + 2] + nums[i])

        return memo[0]


class Solution:
    def rob(self, nums: list[int]) -> int:
        N = len(nums)
        memo = {0: 0, 1: nums[0]}

        for i in range(2, N + 1):
            memo[i] = max(memo[i - 1], memo[i - 2] + nums[i - 1])

        return memo[N]


class Solution:
    def rob(self, nums: list[int]) -> int:
        N = len(nums)
        memo = {0: 0, 1: nums[0]}

        for i in range(1, N):
            memo[i + 1] = max(memo[i], memo[i - 1] + nums[i])

        return memo[N]


class Solution:
    def rob(self, nums: list[int]) -> int:
        N = len(nums)
        memo = {}
        memo[0] = 0
        memo[1] = nums[0]

        for i in range(1, N):
            memo[i + 1] = max(memo[i], memo[i - 1] + nums[i])

        return memo[N]


class Solution:
    def rob(self, nums: list[int]) -> int:
        N = len(nums)
        memo = {0: 0, 1: nums[0]}

        for i in range(1, N):
            memo[i + 1] = max(memo[i], memo[i - 1] + nums[i])

        return memo[N]


class Solution:
    def rob(self, nums: list[int]) -> int:
        N = len(nums)
        memo = [0, nums[0]] + [None] * (N - 1)

        for i in range(2, N + 1):
            memo[i] = max(memo[i - 1], memo[i - 2] + nums[i - 1])

        return memo[-1]


## dp top-down recursive (memoization)
##########################################
class Solution:
    def rob(self, nums: list[int]) -> int:
        @lru_cache(None)
        def dp(i):
            if i >= len(nums):
                return 0

            return max(dp(i + 1), dp(i + 2) + nums[i])

        return dp(0)


class Solution:
    def rob(self, nums: list[int]) -> int:
        memo = {}

        def helper(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]

            memo[i] = max(helper(i + 1), helper(i + 2) + nums[i])

            return memo[i]

        return helper(0)


class Solution:
    def rob(self, nums: list[int]) -> int:
        memo = {}

        def helper(i):
            if i < 0:
                return 0
            if i in memo:
                return memo[i]

            memo[i] = max(helper(i - 1), helper(i - 2) + nums[i])

            return memo[i]

        return helper(len(nums) - 1)


## Discuss Solutions
##############################
class Solution:
    def rob(self, nums: list[int]) -> int:
        prev = curr = 0

        for num in nums:
            prev, curr = curr, max(curr, prev + num)

        return curr


class Solution:
    def rob(self, nums: list[int]) -> int:
        a = b = 0

        for i in range(len(nums)):
            if i % 2:
                a = max(a + nums[i], b)
            else:
                b = max(a, b + nums[i])

        return max(a, b)


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.rob([1, 2, 3, 1]), 4)
        self.assertEqual(solution.rob([2, 7, 9, 3, 1]), 12)


if __name__ == "__main__":
    unittest.main()
