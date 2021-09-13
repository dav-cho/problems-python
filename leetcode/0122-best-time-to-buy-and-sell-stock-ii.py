##
#### Best Time to Buy and Sell Stock II (easy)
##################################################

# You are given an array prices where prices[i] is the
# price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete as
# many transactions as you like (i.e., buy one and sell one
# share of the stock multiple times).

# Note: You may not engage in multiple transactions simultaneously
# (i.e., you must sell the stock before you buy again).


# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on
# day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on
# day 5 (price = 6), profit = 6-3 = 3.

# Example 2:
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell
# on day 5 (price = 5), profit = 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later,
# as you are engaging multiple transactions at the same time.
# You must sell before buying again.

# Example 3:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e., max profit = 0.

# Constraints:
# 1 <= prices.length <= 3 * 104
# 0 <= prices[i] <= 104

################################################################################

## brute force
##############################
class Solution:
    def maxProfit(prices: list[int]) -> int:
        def calculate(start):
            if start >= len(prices):
                return 0

            max = 0
            for i in range(start, len(prices)):
                max_profit = 0
                for j in range(i + 1, len(prices)):
                    if prices[i] < prices[j]:
                        profit = calculate(j + 1) + prices[j] - prices[i]
                        if profit > max_profit:
                            max_profit = profit
                if max_profit > max:
                    max = max_profit

            return max

        return calculate(0)

## peak valley
##############################
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        i = 0
        max_profit = 0
        
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]
            
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]
            
            max_profit += peak - valley
            
        return max_profit


## one pass
##############################
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
                
        return max_profit


## Tests
############

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
# Time: O(n^n) - Recursive function is called n^n times
# Space: O(n) - Depth of recursion is n

## Java
# class Solution {
#     public int maxProfit(int[] prices) {
#         return calculate(prices, 0);
#     }
#
#     public int calculate(int prices[], int s) {
#         if (s >= prices.length)
#             return 0;
#         int max = 0;
#         for (int start = s; start < prices.length; start++) {
#             int maxprofit = 0;
#             for (int i = start + 1; i < prices.length; i++) {
#                 if (prices[start] < prices[i]) {
#                     int profit = calculate(prices, i + 1) + prices[i] - prices[start];
#                     if (profit > maxprofit)
#                         maxprofit = profit;
#                 }
#             }
#             if (maxprofit > max)
#                 max = maxprofit;
#         }
#         return max;
#     }
# }

## Approach 2: Peak Valley Approach
#######################################
# Time: O(n) - Single pass.
# Space: O(1) - Constant space required.

## Java
# class Solution {
#     public int maxProfit(int[] prices) {
#         int i = 0;
#         int valley = prices[0];
#         int peak = prices[0];
#         int maxprofit = 0;
#         while (i < prices.length - 1) {
#             while (i < prices.length - 1 && prices[i] >= prices[i + 1])
#                 i++;
#             valley = prices[i];
#             while (i < prices.length - 1 && prices[i] <= prices[i + 1])
#                 i++;
#             peak = prices[i];
#             maxprofit += peak - valley;
#         }
#         return maxprofit;
#     }
# }

## Approach 3: Simple One Pass
##################################
# Time: O(n) - Single pass.
# Space: O(1) - Constant space needed.

## Java
# class Solution {
#     public int maxProfit(int[] prices) {
#         int maxprofit = 0;
#         for (int i = 1; i < prices.length; i++) {
#             if (prices[i] > prices[i - 1])
#                 maxprofit += prices[i] - prices[i - 1];
#         }
#         return maxprofit;
#     }
# }

