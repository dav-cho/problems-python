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


def maxProfit(prices: list[int]) -> int:
    max = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            max += prices[i] - prices[i - 1]

    return max


## LeetCode Solutions
#########################


## Approach 1: Brute Force
##############################
# time: O(n^n) - recursive function is called n^n times
# space: O(n) - depth of recursion is n
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
# calculate the profits from each valley (low point) to peak (next high point)
# time: O(n) - single pass
# space: O(1) - no additional space besides a few variables
def maxProfit(prices: list[int]) -> int:
    i = 0
    valley = prices[0]
    peak = prices[0]
    max = 0

    last = len(prices) - 1
    while i < last:
        while i < last and prices[i] >= prices[i + 1]:
            i += 1

        valley = prices[i]

        while i < last and prices[i] <= prices[i + 1]:
            i += 1

        peak = prices[i]
        max += peak - valley

    return max


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
# accumulate sum of the profits of each consecutive transaction
# time: O(n) - single pass
# space: O(1) - no additional memory besides a few constant size variables
def maxProfit(prices: list[int]) -> int:
    max = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            max += prices[i] - prices[i - 1]

    return max


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

test1 = [7, 1, 5, 3, 6, 4]  # 7
test2 = [1, 2, 3, 4, 5]  # 4
test3 = [7, 6, 4, 3, 1]  # 0


def test(*args):
    count = 0

    def run():
        for test in args:
            result = maxProfit(test)
            nonlocal count
            print(f"~ test {count}")
            print(f"{test} --> {result}")
            count += 1

    return run()


test(test1, test2, test3)
