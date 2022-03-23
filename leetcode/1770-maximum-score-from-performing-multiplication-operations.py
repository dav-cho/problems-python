##
#### Maximum Score from Performing Multiplication Operations (medium)
#########################################################################

# You are given two integer arrays nums and multipliers of size n and m
# respectively, where n >= m. The arrays are 1-indexed.

# You begin with a score of 0. You want to perform exactly m operations. On
# the ith operation (1-indexed), you will:

# - Choose one integer x from either the start or the end of the array nums.
# - Add multipliers[i] * x to your score.
# - Remove x from the array nums.

# Return the maximum score after performing m operations.

# Example 1:
# Input: nums = [1,2,3], multipliers = [3,2,1]
# Output: 14
# Explanation: An optimal solution is as follows:
# - Choose from the end, [1,2,3], adding 3 * 3 = 9 to the score.
# - Choose from the end, [1,2], adding 2 * 2 = 4 to the score.
# - Choose from the end, [1], adding 1 * 1 = 1 to the score.
# The total score is 9 + 4 + 1 = 14.

# Example 2:
# Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
# Output: 102
# Explanation: An optimal solution is as follows:
# - Choose from the start, [-5,-3,-3,-2,7,1], adding -5 * -10 = 50 to the score.
# - Choose from the start, [-3,-3,-2,7,1], adding -3 * -5 = 15 to the score.
# - Choose from the start, [-3,-2,7,1], adding -3 * 3 = -9 to the score.
# - Choose from the end, [-2,7,1], adding 1 * 4 = 4 to the score.
# - Choose from the end, [-2,7], adding 7 * 6 = 42 to the score. 
# The total score is 50 + 15 - 9 + 4 + 42 = 102.
 
# Constraints:
# n == nums.length
# m == multipliers.length
# 1 <= m <= 103
# m <= n <= 105
# -1000 <= nums[i], multipliers[i] <= 1000

################################################################################

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
        self.assertEqual(Solution().maximumScore([1,2,3], [3,2,1]), 14)
        self.assertEqual(Solution().maximumScore([-5,-3,-3,-2,7,1], [-10,-5,3,4,6]), 102)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Top-down Implementation
##########################################
# Time: 
# Space: 
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # lru_cache from functools automatically memoizes the function
        @lru_cache(2000)
        def dp(i, left):
            # Base case
            if i == m:
                return 0

            mult = multipliers[i]
            right = n - 1 - (i - left)
            
            # Recurrence relation
            return max(mult * nums[left] + dp(i + 1, left + 1), 
                       mult * nums[right] + dp(i + 1, left))
                       
        n, m = len(nums), len(multipliers)
        return dp(0, 0)


## Approach 2: Bottom-up Implementation
###########################################
# Time: 
# Space: 
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        
        for i in range(m - 1, -1, -1):
            for left in range(i, -1, -1):
                mult = multipliers[i]
                right = n - 1 - (i - left)
                dp[i][left] = max(mult * nums[left] + dp[i + 1][left + 1], 
                                  mult * nums[right] + dp[i + 1][left])        
        return dp[0][0]


