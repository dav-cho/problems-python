##
#### 122. Best Time to Buy and Sell Stock II (easy)
#######################################################


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
        self.assertEqual(solution.maxProfit([7, 1, 5, 3, 6, 4]), 7)
        self.assertEqual(solution.maxProfit([1, 2, 3, 4, 5]), 4)
        self.assertEqual(solution.maxProfit([7, 6, 4, 3, 1]), 0)


if __name__ == "__main__":
    unittest.main()
