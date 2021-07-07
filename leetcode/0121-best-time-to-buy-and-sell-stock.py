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

## Approach 1: Brute Force
##############################
class Solution:
    def maxProfit(prices: list[int]) -> int:
        pass


## Approach 2: One Pass
###########################
class Solution:
    def maxProfit(prices: list[int]) -> int:
        pass


## LeetCode Solutions
#########################


## Approach 1: Brute Force
##############################
# time: O(N^2) - loop runs N(N - 1) / 2 times
# space: O(1) - only two variables
def maxProfit(prices: list[int]) -> int:
    max = 0

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]

            if profit > max:
                max = profit

    return max


## Java
# public class Solution {
#     public int maxProfit(int prices[]) {
#         int maxprofit = 0;
#         for (int i = 0; i < prices.length - 1; i++) {
#             for (int j = i + 1; j < prices.length; j++) {
#                 int profit = prices[j] - prices[i];
#                 if (profit > maxprofit)
#                     maxprofit = profit;
#             }
#         }
#         return maxprofit;
#     }
# }

import math

## Approach 2: One Pass
###########################
# time: O(N) - only a single pass needed
# space: O(1) - only two variables are used
def maxProfit(prices: list[int]) -> int:
    min_price = math.inf
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        if price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit


## Java
# public class Solution {
#     public int maxProfit(int prices[]) {
#         int minprice = Integer.MAX_VALUE;
#         int maxprofit = 0;
#         for (int i = 0; i < prices.length; i++) {
#             if (prices[i] < minprice)
#                 minprice = prices[i];
#             else if (prices[i] - minprice > maxprofit)
#                 maxprofit = prices[i] - minprice;
#         }
#         return maxprofit;
#     }
# }


result1 = maxProfit([7, 1, 5, 3, 6, 4])  # 5
result2 = maxProfit([7, 6, 4, 3, 1])  # 0
print("~ result1", result1)
print("~ result2", result2)
