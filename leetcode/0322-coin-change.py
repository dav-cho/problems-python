##
#### Coin Change (medium)
########################################

# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If
# that amount of money cannot be made up by any combination of the coins,
# return -1.

# You may assume that you have an infinite number of each kind of coin.

# Example 1:
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Example 2:
# Input: coins = [2], amount = 3
# Output: -1

# Example 3:
# Input: coins = [1], amount = 0
# Output: 0
 
# Constraints:
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104

################################################################################

from functools import lru_cache


## dp bottom-up
##############################
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for remaining in range(coin, amount + 1):
                dp[remaining] = min(dp[remaining], 1 + dp[remaining - coin])
                
        return dp[amount] if dp[amount] != float('inf') else -1


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
                
        return dp[amount] if dp[amount] != float('inf') else -1


## dp top-down
##############################
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        @lru_cache(None)
        def dp(remaining):
            if remaining < 0:
                return -1
            if remaining == 0:
                return 0

            min_count = float('inf')
            for coin in coins:
                count = dp(remaining - coin)
                if count == -1:
                    continue
                min_count = min(min_count, count + 1)

            return min_count if min_count < float('inf') else -1

        return dp(amount)


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount < 1:
            return 0
        
        return self.helper(coins, amount, [0] * amount)
    
    def helper(self, coins, remaining, counts):
        if remaining < 0:
            return -1
        if remaining == 0:
            return 0
        if counts[remaining - 1] != 0:
            return counts[remaining - 1]
        
        min_count = float('inf')
        for coin in coins:
            res = self.helper(coins, remaining - coin, counts)
            if res >= 0 and res < min_count:
                min_count = 1 + res
                
        counts[remaining - 1] = min_count if min_count < float('inf') else -1
        
        return counts[remaining - 1]


## brute force (TLE)
##############################
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        return self.helper(0, coins, amount)
    
    def helper(self, coin_idx, coins, amount):
        if amount == 0:
            return 0
        if coin_idx < len(coins) and amount > 0:
            max_val = amount // coins[coin_idx]
            min_cost = float('inf')
            for x in range(max_val + 1):
                if amount >= x * coins[coin_idx]:
                    res = self.helper(coin_idx + 1,
                                      coins,
                                      amount - x * coins[coin_idx])
                    if res != -1:
                        min_cost = min(min_cost, res + x)
                        
            return min_cost if min_cost < float('inf') else -1
        
        return -1


## 
##############################
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().coinChange([1,2,5], 11), 3)
        self.assertEqual(Solution().coinChange([2], 3), -1)
        self.assertEqual(Solution().coinChange([1], 0), 0)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: (Brute force) [Time Limit Exceeded]
######################################################
# Time: O(S^n)
# - In the worst case, complexity is exponential in the number of the coins n.
#   The reason is that every coin denomination c_i could have at most S/c_i
#   values. Therefore the number of possible combinations is:
#       S/c_1 * S/c_2 * S/c_3 ... S/c_n = S/(c_1 * c_2 * c_3 ... c_n)

# Space: O(n)
# - In the worst case the maximum depth of recursion is nn. Therefore we need
#   O(n) space used by the system recursive stack.

## Java
#public class Solution {
#
#  public int coinChange(int[] coins, int amount) {
#    return coinChange(0, coins, amount);
#  }
#
#  private int coinChange(int idxCoin, int[] coins, int amount) {
#    if (amount == 0)
#      return 0;
#    if (idxCoin < coins.length && amount > 0) {
#      int maxVal = amount/coins[idxCoin];
#      int minCost = Integer.MAX_VALUE;
#      for (int x = 0; x <= maxVal; x++) {
#        if (amount >= x * coins[idxCoin]) {
#          int res = coinChange(idxCoin + 1, coins, amount - x * coins[idxCoin]);
#          if (res != -1)
#            minCost = Math.min(minCost, res + x);
#        }
#      }
#      return (minCost == Integer.MAX_VALUE)? -1: minCost;
#    }
#    return -1;
#  }
#}
#
#// Time Limit Exceeded


## Approach 2: (Dynamic programming - Top down) [Accepted]
##############################################################
# Time: O(S∗n)
# - Where S is the amount, n is denomination count. In the worst case the
#   recursive tree of the algorithm has height of S and the algorithm solves
#   only S subproblems because it caches precalculated solutions in a table.
#   Each subproblem is computed with nn iterations, one by coin denomination.
#   Therefore there is O(S∗n) time complexity.

# Space: O(S)
# - Where S is the amount to change We use extra space for the memoization
#   table.

## Java
#public class Solution {
#
#  public int coinChange(int[] coins, int amount) {
#    if (amount < 1) return 0;
#    return coinChange(coins, amount, new int[amount]);
#  }
#
#  private int coinChange(int[] coins, int rem, int[] count) {
#    if (rem < 0) return -1;
#    if (rem == 0) return 0;
#    if (count[rem - 1] != 0) return count[rem - 1];
#    int min = Integer.MAX_VALUE;
#    for (int coin : coins) {
#      int res = coinChange(coins, rem - coin, count);
#      if (res >= 0 && res < min)
#        min = 1 + res;
#    }
#    count[rem - 1] = (min == Integer.MAX_VALUE) ? -1 : min;
#    return count[rem - 1];
#  }
#}


## Approach 3: (Dynamic programming - Bottom up) [Accepted]
###############################################################
# Time: O(S∗n) - On each step the algorithm finds the next F(i) in n iterations,
#                where 1≤i≤S. Therefore in total the iterations are S∗n.
# Space: O(S) - We use extra space for the memoization table.
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


