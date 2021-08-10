
##
#### Target Sum (medium)
############################

# You are given an integer array nums and an integer target.

# You want to build an expression out of nums by adding one of the symbols
# '+' and '-' before each integer in nums and then concatenate all the integers.

# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before
# 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates
# to target.

# Example 1:
# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3

# Example 2:
# Input: nums = [1], target = 1
# Output: 1

# Constrains:
# 1 <= nums.length <= 20
# 0 <= nums[i] <= 1000
# 0 <= sum(nums[i]) <= 1000
# -1000 <= target <= 1000

################################################################################

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
        self.assertEqual(solution.findTargetSumWays([1,1,1,1,1], 3), 5)
        self.assertEqual(solution.findTargetSumWays([1], 1), 1)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Brute Force
##############################
# Time: O(2^n) - Size of recursion tree will be 2^n. n refers to the size of
#                nums array.
# Space: O(n) - The depth of the recursion tree can go upto n.
## Java
#public class Solution {
#    int count = 0;
#    public int findTargetSumWays(int[] nums, int S) {
#        calculate(nums, 0, 0, S);
#        return count;
#    }
#    public void calculate(int[] nums, int i, int sum, int S) {
#        if (i == nums.length) {
#            if (sum == S)
#                count++;
#        } else {
#            calculate(nums, i + 1, sum + nums[i], S);
#            calculate(nums, i + 1, sum - nums[i], S);
#        }
#    }
#}


## Approach 2: Recursion with Memoization
#############################################
# Time: O(l * n) - The memo array of size l*n has been filled just once. Here,
#                  l refers to the range of sum and n refers to the size of
#                  numsnums array.
# Space: O(l * n) - The depth of recursion tree can go upto n. The memo array
#                   contains l * n elements.
## Java
#public class Solution {
#    int count = 0;
#    public int findTargetSumWays(int[] nums, int S) {
#        int[][] memo = new int[nums.length][2001];
#        for (int[] row: memo)
#            Arrays.fill(row, Integer.MIN_VALUE);
#        return calculate(nums, 0, 0, S, memo);
#    }
#    public int calculate(int[] nums, int i, int sum, int S, int[][] memo) {
#        if (i == nums.length) {
#            if (sum == S)
#                return 1;
#            else
#                return 0;
#        } else {
#            if (memo[i][sum + 1000] != Integer.MIN_VALUE) {
#                return memo[i][sum + 1000];
#            }
#            int add = calculate(nums, i + 1, sum + nums[i], S, memo);
#            int subtract = calculate(nums, i + 1, sum - nums[i], S, memo);
#            memo[i][sum + 1000] = add + subtract;
#            return memo[i][sum + 1000];
#        }
#    }
#}


## Approach 3: 2D Dynamic Programming
#########################################
# Time: O(l*n) - The entire nums array is travesed 2001(constant no.: ll) times.
#                n refers to the size of nums array. l refers to the range of
#                sumsum possible.
# Space: O(l*n) - dp array of size l*n is used.
## Java
#public class Solution {
#    public int findTargetSumWays(int[] nums, int S) {
#        int[][] dp = new int[nums.length][2001];
#        dp[0][nums[0] + 1000] = 1;
#        dp[0][-nums[0] + 1000] += 1;
#        for (int i = 1; i < nums.length; i++) {
#            for (int sum = -1000; sum <= 1000; sum++) {
#                if (dp[i - 1][sum + 1000] > 0) {
#                    dp[i][sum + nums[i] + 1000] += dp[i - 1][sum + 1000];
#                    dp[i][sum - nums[i] + 1000] += dp[i - 1][sum + 1000];
#                }
#            }
#        }
#        return S > 1000 ? 0 : dp[nums.length - 1][S + 1000];
#    }
#}


## Approach 4: 1D Dynamic Programming
#########################################
# Time: O(l.n) - The entire nums array is traversed l times. n refers to the
#                size of numsnums array. l refers to the range of sum possible.
# Space: O(n) - dp array of size n is used.
## Java
#public class Solution {
#    public int findTargetSumWays(int[] nums, int S) {
#        int[] dp = new int[2001];
#        dp[nums[0] + 1000] = 1;
#        dp[-nums[0] + 1000] += 1;
#        for (int i = 1; i < nums.length; i++) {
#            int[] next = new int[2001];
#            for (int sum = -1000; sum <= 1000; sum++) {
#                if (dp[sum + 1000] > 0) {
#                    next[sum + nums[i] + 1000] += dp[sum + 1000];
#                    next[sum - nums[i] + 1000] += dp[sum + 1000];
#                }
#            }
#            dp = next;
#        }
#        return S > 1000 ? 0 : dp[S + 1000];
#    }
#}
