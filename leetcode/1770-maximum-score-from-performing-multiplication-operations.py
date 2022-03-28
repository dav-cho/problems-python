##
#### 1770. Maximum Score from Performing Multiplication Operations (medium)
###############################################################################


from functools import lru_cache


## dp bottom-up
##############################
# memo[i][left] = max possible score with i operations and left left operations


class Solution:
    def maximumScore(self, nums: list[int], multipliers: list[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        memo = [[0] * (m + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for left in range(i, -1, -1):
                mult = multipliers[i]
                right = n - 1 - (i - left)
                left_score = mult * nums[left] + memo[i + 1][left + 1]
                right_score = mult * nums[right] + memo[i + 1][left]

                memo[i][left] = max(left_score, right_score)

        return memo[0][0]


class Solution:
    def maximumScore(self, nums: list[int], multipliers: list[int]) -> int:
        n, m = len(nums), len(multipliers)
        memo = [[0] * (m + 1) for _ in range(m + 1)]

        for i in reversed(range(m)):
            for left in reversed(range(i + 1)):
                mult = multipliers[i]
                right = n - 1 - (i - left)
                left_score = mult * nums[left] + memo[i + 1][left + 1]
                right_score = mult * nums[right] + memo[i + 1][left]
                memo[i][left] = max(left_score, right_score)

        return memo[0][0]


class Solution:
    def maximumScore(self, nums: list[int], multipliers: list[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        memo = [[0] * (m + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for left in range(i + 1):
                mult = multipliers[i]
                right = n - 1 - (i - left)
                left_score = mult * nums[left] + memo[i + 1][left + 1]
                right_score = mult * nums[right] + memo[i + 1][left]

                memo[i][left] = max(left_score, right_score)

        return memo[0][0]


## dp top-down
##############################
class Solution:
    def maximumScore(self, nums: list[int], multipliers: list[int]) -> int:
        m = len(multipliers)
        n = len(nums)

        @lru_cache(None)
        def dp(i, left):
            if i == m:
                return 0

            mult = multipliers[i]
            right = n - 1 - (i - left)
            left_score = mult * nums[left] + dp(i + 1, left + 1)
            right_score = mult * nums[right] + dp(i + 1, left)

            return max(left_score, right_score)

        res = dp(0, 0)
        dp.cache_clear()

        return res


class Solution:
    def maximumScore(self, nums: list[int], multipliers: list[int]) -> int:
        n = len(nums)
        m = len(multipliers)

        @lru_cache(2000)
        def dp(i, left):
            if i == m:
                return 0

            mult = multipliers[i]
            right = n - 1 - (i - left)
            left_score = mult * nums[left] + dp(i + 1, left + 1)
            right_score = mult * nums[right] + dp(i + 1, left)

            return max(left_score, right_score)

        return dp(0, 0)


class Solution:
    def maximumScore(self, nums: list[int], multipliers: list[int]) -> int:
        m = len(multipliers)
        n = len(nums)
        memo = [[0] * (m + 1) for _ in range(n + 1)]

        def dp(i, left):
            if i == m:
                return 0
            if memo[i][left]:
                return memo[i][left]

            mult = multipliers[i]
            right = n - 1 - (i - left)
            left_score = mult * nums[left] + dp(i + 1, left + 1)
            right_score = mult * nums[right] + dp(i + 1, left)

            memo[i][left] = max(left_score, right_score)

            return memo[i][left]

        return dp(0, 0)


##
##############################
class Solution:
    def maximumScore(self, nums: list[int], multipliers: list[int]) -> int:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().maximumScore([1, 2, 3], [3, 2, 1]), 14)
        self.assertEqual(
            Solution().maximumScore([-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6]), 102
        )


if __name__ == "__main__":
    unittest.main()
