##
#### 121. Best Time to Buy and Sell Stock (easy)
####################################################


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
        min_price = float("inf")
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
        self.assertEqual(solution.maxProfit([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(solution.maxProfit([7, 6, 4, 3, 1]), 0)


if __name__ == "__main__":
    unittest.main()
