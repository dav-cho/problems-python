##
#### Best Time to Buy and Sell Stock (easy)
###############################################

# You are given an array prices where prices[i] is the price of a given stock
# on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you
# cannot achieve any profit, return 0.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 
# Constraints:
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

################################################################################


## one-pass
##############################
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        low = prices[0]
        res = 0
        
        for i in range(1, len(prices)):
            low = min(low, prices[i])
            res = max(res, prices[i] - low)
            
        return res


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        low = prices[0]
        res = 0
        
        for price in prices[1:]:
            low = min(low, price)
            res = max(res, price - low)
            
        return res


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        low = prices[0]
        res = 0
        
        for price in prices:
            low = min(low, price)
            res = max(res, price - low)
            
        return res


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
            
        return max_profit


## dp
##############################
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        N = len(prices)
        memo = [0] * N
        low = prices[0]
        
        for i in range(1, N):
            low = min(low, prices[i])
            memo[i] = max(memo[i - 1], prices[i] - low)
            
        return memo[-1]


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        N = len(prices)
        min_price = prices[0]
        memo = [0] * N
        
        for i in range(1, N):
            min_price = min(min_price, prices[i])
            memo[i] = max(memo[i - 1], prices[i] - min_price)
            
        return memo[-1]


## kidane's algorithm
##############################
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        curr_max = res = 0
        
        for i in range(1, len(prices)):
            curr_max = max(0, curr_max + prices[i] - prices[i - 1])
            res = max(res, curr_max)
            
        return res


## brute force
##############################
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        N = len(prices)
        res = 0
        
        for i in range(N):
            for j in range(i + 1, N):
                res = max(res, prices[j] - prices[i])
                
        return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.maxProfit([7,1,5,3,6,4]), 5)
        self.assertEqual(solution.maxProfit([7,6,4,3,1]), 0)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Brute Force
##############################
# Time: O(n^2) - Loop runs (n(n - 2)) / 2 times.
# Space: O(1) - Only two variables, maxprofit and profit, are used.

## Java
#public class Solution {
#    public int maxProfit(int prices[]) {
#        int maxprofit = 0;
#        for (int i = 0; i < prices.length - 1; i++) {
#            for (int j = i + 1; j < prices.length; j++) {
#                int profit = prices[j] - prices[i];
#                if (profit > maxprofit)
#                    maxprofit = profit;
#            }
#        }
#        return maxprofit;
#    }
#}


## Approach 2: One Pass
##############################
# Time: O(n) - Only a single pass is needed.
# Space: O(1) - Only two variables used.

## Java
#public class Solution {
#    public int maxProfit(int prices[]) {
#        int minprice = Integer.MAX_VALUE;
#        int maxprofit = 0;
#        for (int i = 0; i < prices.length; i++) {
#            if (prices[i] < minprice)
#                minprice = prices[i];
#            else if (prices[i] - minprice > maxprofit)
#                maxprofit = prices[i] - minprice;
#        }
#        return maxprofit;
#    }
#}


