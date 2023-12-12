##
#### 221. Maximal Square (medium)
########################################


## optimized dp
##############################
class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [0] * (n + 1)
        prev = 0
        res = 0

        for row in range(1, m + 1):
            for col in range(1, n + 1):
                temp = dp[col]

                if matrix[row - 1][col - 1] == "1":
                    dp[col] = 1 + min(dp[col], dp[col - 1], prev)
                    res = max(res, dp[col])
                else:
                    dp[col] = 0

                prev = temp

        return res * res


class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [0] * (cols + 1)
        res = 0
        prev = 0

        for row in reversed(range(rows)):
            for col in reversed(range(cols)):
                temp = dp[col]

                if matrix[row][col] == "1":
                    dp[col] = 1 + min(dp[col], dp[col + 1], prev)
                    res = max(res, dp[col])
                else:
                    dp[col] = 0

                prev = temp

        return res * res


class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [0] * (n + 1)
        prev = 0
        res = 0

        for row in range(1, m + 1):
            for col in range(1, n + 1):
                temp = dp[col]

                if matrix[row - 1][col - 1] == "1":
                    above = dp[col]
                    left = dp[col - 1]
                    above_left = prev

                    dp[col] = 1 + min(above, left, above_left)
                    res = max(res, dp[col])
                else:
                    dp[col] = 0

                prev = temp

        return res * res


## dp
##############################
class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        res = 0

        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if matrix[row - 1][col - 1] == "1":
                    above = dp[row - 1][col]
                    left = dp[row][col - 1]
                    above_left = dp[row - 1][col - 1]

                    dp[row][col] = 1 + min(above, left, above_left)
                    res = max(res, dp[row][col])

        return res * res


class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        res = 0

        for row in reversed(range(rows)):
            for col in reversed(range(cols)):
                if matrix[row][col] == "1":
                    dp[row][col] = 1 + min(
                        dp[row + 1][col], dp[row][col + 1], dp[row + 1][col + 1]
                    )
                    res = max(res, dp[row][col])

        return res * res


class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        if not matrix:
            return 0

        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        res = 0

        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if matrix[row - 1][col - 1] != "1":
                    continue

                above = dp[row - 1][col]
                left = dp[row][col - 1]
                above_left = dp[row - 1][col - 1]

                dp[row][col] = 1 + min(above, left, above_left)
                res = max(res, dp[row][col])

        return res * res


class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        res = 0

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == "1":
                    dp[row + 1][col + 1] = 1 + min(
                        dp[row][col], dp[row + 1][col], dp[row][col + 1]
                    )
                    res = max(res, dp[row + 1][col + 1])

        return res * res


class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        res = 0

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == "1":
                    left = dp[row + 1][col]
                    above = dp[row][col + 1]
                    above_left = dp[row][col]

                    dp[row + 1][col + 1] = 1 + min(left, above, above_left)
                    res = max(res, dp[row + 1][col + 1])

        return res * res


## brute force (TLE)
##############################
class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        R = len(matrix)
        C = len(matrix[0]) if R > 0 else 0
        res = 0

        for row in range(R):
            for col in range(C):
                if matrix[row][col] != "1":
                    continue

                S = 1  # length of square
                flag = True

                while S + row < R and S + col < C and flag:
                    for k in range(col, S + col + 1):
                        if matrix[row + S][k] == "0":
                            flag = False
                            break

                    for k in range(row, S + row + 1):
                        if matrix[k][col + S] == "0":
                            flag = False
                            break

                    if flag:
                        S += 1

                res = max(res, S)

        return res * res


##
##############################
class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(
            Solution().maximalSquare(
                [
                    ["1", "0", "1", "0", "0"],
                    ["1", "0", "1", "1", "1"],
                    ["1", "1", "1", "1", "1"],
                    ["1", "0", "0", "1", "0"],
                ]
            ),
            4,
        )
        self.assertEqual(Solution().maximalSquare([["0", "1"], ["1", "0"]]), 1)


if __name__ == "__main__":
    unittest.main()
