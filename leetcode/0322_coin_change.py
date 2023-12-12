##
#### 322. Coin Change (medium)
########################################


from functools import lru_cache


## dp bottom-up
##############################
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for remaining in range(coin, amount + 1):
                dp[remaining] = min(dp[remaining], 1 + dp[remaining - coin])

        return dp[amount] if dp[amount] != float("inf") else -1


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)

        return dp[amount] if dp[amount] != float("inf") else -1


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

            min_count = float("inf")
            for coin in coins:
                count = dp(remaining - coin)
                if count == -1:
                    continue
                min_count = min(min_count, count + 1)

            return min_count if min_count < float("inf") else -1

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

        min_count = float("inf")
        for coin in coins:
            res = self.helper(coins, remaining - coin, counts)
            if res >= 0 and res < min_count:
                min_count = 1 + res

        counts[remaining - 1] = min_count if min_count < float("inf") else -1

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
            min_cost = float("inf")
            for x in range(max_val + 1):
                if amount >= x * coins[coin_idx]:
                    res = self.helper(coin_idx + 1, coins, amount - x * coins[coin_idx])
                    if res != -1:
                        min_cost = min(min_cost, res + x)

            return min_cost if min_cost < float("inf") else -1

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
        self.assertEqual(Solution().coinChange([1, 2, 5], 11), 3)
        self.assertEqual(Solution().coinChange([2], 3), -1)
        self.assertEqual(Solution().coinChange([1], 0), 0)


if __name__ == "__main__":
    unittest.main()
