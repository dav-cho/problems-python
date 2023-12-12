##
#### 1143. Longest Common Subsequence (medium)
##################################################


from functools import lru_cache


## bottom-up dp space optimized
###################################
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        if m > n:
            return self.longestCommonSubsequence(text2, text1)

        prev = [0] * (m + 1)
        for col in reversed(range(n)):
            curr = [0] * (m + 1)
            for row in reversed(range(m)):
                if text1[row] == text2[col]:
                    curr[row] = 1 + prev[row + 1]
                else:
                    curr[row] = max(curr[row + 1], prev[row])

            prev = curr

        return prev[0]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1)
        cols = len(text2)
        if rows > cols:
            return self.longestCommonSubsequence(text2, text1)

        prev = [0] * (rows + 1)
        for col in reversed(range(cols)):
            curr = [0] * (rows + 1)
            for row in reversed(range(rows)):
                if text1[row] == text2[col]:
                    below_right = prev[row + 1]
                    curr[row] = 1 + below_right
                else:
                    below = curr[row + 1]
                    right = prev[row]
                    curr[row] = max(below, right)

            prev = curr

        return prev[0]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        if n > m:
            text1, text2 = text2, text1
            n, m = m, n

        prev = [0] * (n + 1)

        for col in range(m - 1, -1, -1):
            curr = [0] * (n + 1)

            for row in range(n - 1, -1, -1):
                if text1[row] == text2[col]:
                    curr[row] = 1 + prev[row + 1]
                else:
                    curr[row] = max(prev[row], curr[row + 1])

            prev = curr

        return prev[0]


## bottom-up dp
##############################
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1), len(text2)
        memo = [[0] * (cols + 1) for _ in range(rows + 1)]

        for row in reversed(range(rows)):
            for col in reversed(range(cols)):
                if text1[row] == text2[col]:
                    below_right = memo[row + 1][col + 1]
                    memo[row][col] = 1 + below_right
                else:
                    below = memo[row + 1][col]
                    right = memo[row][col + 1]
                    memo[row][col] = max(below, right)

        return memo[0][0]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1), len(text2)
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        if rows > cols:
            return self.longestCommonSubsequence(text2, text1)

        for char1 in reversed(range(rows)):
            for char2 in reversed(range(cols)):
                if text1[char1] == text2[char2]:
                    dp[char1][char2] = 1 + dp[char1 + 1][char2 + 1]
                else:
                    dp[char1][char2] = max(dp[char1 + 1][char2], dp[char1][char2 + 1])

        return dp[0][0]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1), len(text2)
        memo = [[0] * (cols + 1) for _ in range(rows + 1)]

        for row in reversed(range(rows)):
            for col in reversed(range(cols)):
                if text1[row] == text2[col]:
                    memo[row][col] = 1 + memo[row + 1][col + 1]
                else:
                    memo[row][col] = max(memo[row + 1][col], memo[row][col + 1])

        return memo[0][0]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        memo = [[0] * (n + 1) for _ in range(m + 1)]

        for col in reversed(range(n)):
            for row in reversed(range(m)):
                if text1[row] == text2[col]:
                    memo[row][col] = 1 + memo[row + 1][col + 1]
                else:
                    memo[row][col] = max(memo[row + 1][col], memo[row][col + 1])

        return memo[0][0]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for col in reversed(range(m)):
            for row in reversed(range(n)):
                if text1[row] == text2[col]:
                    dp[row][col] = 1 + dp[row + 1][col + 1]
                else:
                    dp[row][col] = max(dp[row + 1][col], dp[row][col + 1])

        return dp[0][0]


## improved top-down memoization
####################################
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(maxsize=None)
        def dp(p1, p2):
            if p1 == len(text1) or p2 == len(text2):
                return 0
            if text1[p1] == text2[p2]:
                return 1 + dp(p1 + 1, p2 + 1)

            return max(dp(p1, p2 + 1), dp(p1 + 1, p2))

        return dp(0, 0)


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(maxsize=None)
        def dp(p1, p2):
            if p1 == len(text1) or p2 == len(text2):
                return 0

            if text1[p1] == text2[p2]:
                return 1 + dp(p1 + 1, p2 + 1)

            option1 = dp(p1, p2 + 1)
            option2 = dp(p1 + 1, p2)

            return max(option1, option2)

        return dp(0, 0)


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def dp(p1, p2):
            if p1 == len(text1) or p2 == len(text2):
                return 0
            if (p1, p2) in memo:
                return memo[(p1, p2)]

            if text1[p1] == text2[p2]:
                memo[(p1, p2)] = 1 + dp(p1 + 1, p2 + 1)
            else:
                memo[(p1, p2)] = max(dp(p1, p2 + 1), dp(p1 + 1, p2))

            return memo[(p1, p2)]

        return dp(0, 0)


## top-down memoization
##############################
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(maxsize=None)
        def dp(p1, p2):
            if p1 == len(text1) or p2 == len(text2):
                return 0

            option1 = dp(p1 + 1, p2)
            option2 = 0
            first = text2.find(text1[p1], p2)

            if first != -1:
                option2 = 1 + dp(p1 + 1, first + 1)

            return max(option1, option2)

        return dp(0, 0)


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def dp(p1, p2):
            if p1 == len(text1) or p2 == len(text2):
                return 0
            if (p1, p2) in memo:
                return memo[(p1, p2)]

            option_1 = dp(p1 + 1, p2)

            option_2 = 0
            first = text2.find(text1[p1], p2)

            if first != -1:
                option_2 = 1 + dp(p1 + 1, first + 1)

            memo[(p1, p2)] = max(option_1, option_2)

            return memo[(p1, p2)]

        return dp(0, 0)


##
##############################
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().longestCommonSubsequence("abcde", "ace"), 3)
        self.assertEqual(Solution().longestCommonSubsequence("abc", "abc"), 3)
        self.assertEqual(Solution().longestCommonSubsequence("abc", "def"), 0)


if __name__ == "__main__":
    unittest.main()
