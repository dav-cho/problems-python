##
#### 48. Rotate Image (medium)
########################################


##
##############################
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        pass


## best*
###############################
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        N = len(matrix)

        # reverse diagonally
        for i in range(N):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # reverse horizontally
        for row in matrix:
            for col in range(N // 2):
                row[col], row[~col] = row[~col], row[col]


## rotate in groups of four
###############################
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        N = len(matrix)

        for i in range(N // 2):
            for j in range(N - N // 2):
                temp = matrix[~j][i]
                matrix[~j][i] = matrix[~i][~j]
                matrix[~i][~j] = matrix[j][~i]
                matrix[j][~i] = matrix[i][j]
                matrix[i][j] = temp


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        N = len(matrix)

        for i in range(N // 2 + N % 2):
            for j in range(N // 2):
                temp = matrix[~j][i]
                matrix[~j][i] = matrix[~i][~j]
                matrix[~i][~j] = matrix[j][~i]
                matrix[j][~i] = matrix[i][j]
                matrix[i][j] = temp


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        N = len(matrix)

        for i in range(N // 2 + N % 2):
            for j in range(N // 2):
                temp = matrix[N - 1 - j][i]
                matrix[-j - 1][i] = matrix[-i - 1][-j - 1]
                matrix[-i - 1][-j - 1] = matrix[j][-i - 1]
                matrix[j][-i - 1] = matrix[i][j]
                matrix[i][j] = temp


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        N = len(matrix)

        for i in range(N // 2 + N % 2):
            for j in range(N // 2):
                temp = matrix[N - 1 - j][i]
                matrix[N - 1 - j][i] = matrix[N - 1 - i][N - j - 1]
                matrix[N - 1 - i][N - j - 1] = matrix[j][N - 1 - i]
                matrix[j][N - 1 - i] = matrix[i][j]
                matrix[i][j] = temp


## reverse / flip
##############################
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        matrix.reverse()

        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


## reverse diagonal, then left to right
###########################################
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        N = len(matrix)

        for i in range(N // 2):
            matrix[i], matrix[~i] = matrix[~i], matrix[i]

        for i in range(N):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        N = len(matrix)

        for i in range(N):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            for j in range(N // 2):
                row[j], row[~j] = row[~j], row[j]


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        N = len(matrix)

        for i in range(N):
            for j in range(i):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        for i in range(N):
            for j in range(N // 2):
                matrix[i][j], matrix[i][~j] = matrix[i][~j], matrix[i][j]


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        N = len(matrix)

        for i in range(N):
            for j in range(i, N):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        for i in range(N):
            for j in range(N // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        def transpose():
            for i in range(N):
                for j in range(i, N):
                    matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        def reflect():
            for i in range(N):
                for j in range(N // 2):
                    matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]

        N = len(matrix)
        transpose()
        reflect()


## pythonic
##############################
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        matrix[:] = map(list, zip(*matrix[::-1]))


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(
            solution.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            [[7, 4, 1], [8, 5, 2], [9, 6, 3]],
        )
        self.assertEqual(
            solution.rotate(
                [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
            ),
            [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]],
        )
        self.assertEqual(solution.rotate([[1]]), [[1]])
        self.assertEqual(solution.rotate([[1, 2], [3, 4]]), [[3, 1], [4, 2]])


if __name__ == "__main__":
    unittest.main()
