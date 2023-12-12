##
#### 1335. Minimum Difficulty of a Job Schedule (hard)
###########################################################


from functools import lru_cache


## bottom-up space optimized (1D)
#####################################
class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1

        dp = [float("inf")] * n
        dp[-1] = jobDifficulty[-1]

        for i in range(n - 2, -1, -1):
            dp[i] = max(dp[i + 1], jobDifficulty[i])

        for day in range(d - 1, 0, -1):
            for i in range(day - 1, n - (d - day)):
                dp[i] = float("inf")
                hardest = 0
                for j in range(i, n - (d - day)):
                    hardest = max(hardest, jobDifficulty[j])
                    dp[i] = min(dp[i], hardest + dp[j + 1])

        return dp[0]


## bottom-up (2D)
##############################
class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1

        dp = [[float("inf")] * (d + 1) for _ in range(n)]
        dp[-1][d] = jobDifficulty[-1]

        for i in range(n - 2, -1, -1):
            dp[i][d] = max(dp[i + 1][d], jobDifficulty[i])

        for day in range(d - 1, 0, -1):
            for i in range(day - 1, n - (d - day)):
                hardest = 0
                for j in range(i, n - (d - day)):
                    hardest = max(hardest, jobDifficulty[j])
                    dp[i][day] = min(dp[i][day], hardest + dp[j + 1][day + 1])

        return dp[0][1]


## top-down
##############################
class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1

        hardest_remaining = [0] * n
        hardest = 0
        for i in range(n - 1, -1, -1):
            hardest = max(hardest, jobDifficulty[i])
            hardest_remaining[i] = hardest

        @lru_cache(None)
        def dp(i, day):
            if day == d:
                return hardest_remaining[i]

            res = float("inf")
            hardest = 0
            days_remaining = d - day
            for j in range(i, n - days_remaining):
                hardest = max(hardest, jobDifficulty[j])
                res = min(res, hardest + dp(j + 1, day + 1))

            return res

        return dp(0, 1)


##
##############################
class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().minDifficulty([6, 5, 4, 3, 2, 1], 2), 7)
        self.assertEqual(Solution().minDifficulty([9, 9, 9], 4), -1)
        self.assertEqual(Solution().minDifficulty([1, 1, 1], 3), 3)


if __name__ == "__main__":
    unittest.main()
