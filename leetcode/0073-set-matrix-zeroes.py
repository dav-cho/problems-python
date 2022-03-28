##
#### 73. Set Matrix Zeroes (medium)
########################################


## no extra memory (space efficient)
########################################
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        M = len(matrix)
        N = len(matrix[0])
        first_col_zero = False
        for row in range(M):
            if matrix[row][0] == 0:
                first_col_zero = True
            for col in range(1, N):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(1, M):
            for col in range(1, N):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if matrix[0][0] == 0:
            for col in range(N):
                matrix[0][col] = 0
        if first_col_zero:
            for row in range(M):
                matrix[row][0] = 0


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        R = len(matrix)
        C = len(matrix[0])
        first_col_zero = False
        for row in range(R):
            if matrix[row][0] == 0:
                first_col_zero = True
            for col in range(1, C):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(1, R):
            for col in range(1, C):
                if not matrix[row][0] or not matrix[0][col]:
                    matrix[row][col] = 0

        if matrix[0][0] == 0:
            for col in range(C):
                matrix[0][col] = 0
        if first_col_zero:
            for row in range(R):
                matrix[row][0] = 0


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        R = len(matrix)
        C = len(matrix[0])
        is_col = False
        for row in range(R):
            if matrix[row][0] == 0:
                is_col = True
            for col in range(1, C):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(1, R):
            for col in range(1, C):
                if not matrix[row][0] or not matrix[0][col]:
                    matrix[row][col] = 0

        if matrix[0][0] == 0:
            for col in range(C):
                matrix[0][col] = 0
        if is_col:
            for row in range(R):
                matrix[row][0] = 0

        return matrix


## extra memory
##############################
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        R = len(matrix)
        C = len(matrix[0])

        rows = set()
        cols = set()
        for row in range(R):
            for col in range(C):
                if matrix[row][col] == 0:
                    rows.add(row)
                    cols.add(col)

        for i in range(R):
            for j in range(C):
                if i in rows or j in cols:
                    matrix[i][j] = 0

        return matrix


## first attempt
##############################
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        M = len(matrix)
        N = len(matrix[0])
        rows = [False] * M
        cols = [False] * N
        for row in range(M):
            for col in range(N):
                if matrix[row][col] == 0:
                    rows[row] = True
                    cols[col] = True

        for row in range(M):
            if rows[row]:
                for col in range(N):
                    matrix[row][col] = 0
        for col in range(N):
            if cols[col]:
                for row in range(M):
                    matrix[row][col] = 0

        return matrix


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(
            Solution().setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]),
            [[1, 0, 1], [0, 0, 0], [1, 0, 1]],
        )
        self.assertEqual(
            Solution().setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]),
            [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
        )


if __name__ == "__main__":
    unittest.main()
