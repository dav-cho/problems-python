##
#### Best time to Buy and Sell Stock (easy)
###############################################

# You are given an array prices where prices[i] is the
# price of a given stock on the i'th day.

# You want to maximize your profit by choosing a
# single day to buy one stock and choosing a different
# day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and
# sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is
# not allowed because you must buy before you sell.

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# Constraints:
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

###############################################################################

## one pass (best)
##############################
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                res += prices[i] - prices[i - 1]

        return res


## peak valley
##############################
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        N = len(prices)
        res = i = 0

        while i < N - 1:
            while i < N - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]

            while i < N - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]

            res += peak - valley

        return res


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        N = len(prices)
        res, i = 0, 1

        while i < N:
            while i < N and prices[i] <= prices[i - 1]:
                i += 1
            valley = prices[i - 1]

            while i < N and prices[i] >= prices[i - 1]:
                i += 1
            peak = prices[i - 1]

            res += peak - valley

        return res


## brute force (TLE)
##############################
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        return self.calculate(prices, 0)

    def calculate(self, prices, s):
        res = 0

        if s >= len(prices):
            return res

        for i in range(len(prices)):
            max_profit = 0
            for j in range(i + 1, len(prices)):
                if prices[i] < prices[j]:
                    profit = self.calculate(prices, i + 1) + prices[j] - prices[i]
                    if profit > max_profit:
                        max_profit = profit

            if max_profit > res:
                res = max_profit

        return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.maxProfit([7,1,5,3,6,4]), 7)
        self.assertEqual(solution.maxProfit([1,2,3,4,5]), 4)
        self.assertEqual(solution.maxProfit([7,6,4,3,1]), 0)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Brute Force
##############################
# Time: O(n^n) - Recursive function is called n^n times.
# Space: O(n) - Depth of recursion is n.

## Java
#class Solution {
#    public int maxProfit(int[] prices) {
#        return calculate(prices, 0);
#    }
#
#    public int calculate(int prices[], int s) {
#        if (s >= prices.length)
#            return 0;
#        int max = 0;
#        for (int start = s; start < prices.length; start++) {
#            int maxprofit = 0;
#            for (int i = start + 1; i < prices.length; i++) {
#                if (prices[start] < prices[i]) {
#                    int profit = calculate(prices, i + 1) + prices[i] - prices[start];
#                    if (profit > maxprofit)
#                        maxprofit = profit;
#                }
#            }
#            if (maxprofit > max)
#                max = maxprofit;
#        }
#        return max;
#    }
#}


## Approach 2: Peak Valley Approach
#######################################
# Time: O(n) - Single pass.
# Space: O(1) - Constant space required.

## Java
#class Solution {
#    public int maxProfit(int[] prices) {
#        int i = 0;
#        int valley = prices[0];
#        int peak = prices[0];
#        int maxprofit = 0;
#        while (i < prices.length - 1) {
#            while (i < prices.length - 1 && prices[i] >= prices[i + 1])
#                i++;
#            valley = prices[i];
#            while (i < prices.length - 1 && prices[i] <= prices[i + 1])
#                i++;
#            peak = prices[i];
#            maxprofit += peak - valley;
#        }
#        return maxprofit;
#    }
#}


## Approach 3: Simple One Pass
##################################
# Time: O(n) - Single pass.
# Space: O(1) - Constant space needed.

## Java
#class Solution {
#    public int maxProfit(int[] prices) {
#        int maxprofit = 0;
#        for (int i = 1; i < prices.length; i++) {
#            if (prices[i] > prices[i - 1])
#                maxprofit += prices[i] - prices[i - 1];
#        }
#        return maxprofit;
#    }
#}


