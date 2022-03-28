##
#### 240. Search a 2D Matrix II (medium)
############################################


## brute force
##############################
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for row in matrix:
            if target in row:
                return True

        return False


## binary search
##############################
class Solution:
    def binary_search(self, matrix, target, start, vertical):
        low = start
        high = len(matrix[0]) - 1 if vertical else len(matrix) - 1
        while low <= high:
            mid = (low + high) // 2
            if vertical:
                if matrix[start][mid] < target:
                    low = mid + 1
                elif matrix[start][mid] > target:
                    high = mid - 1
                else:
                    return True
            else:
                if matrix[mid][start] < target:
                    low = mid + 1
                elif matrix[mid][start] > target:
                    high = mid - 1
                else:
                    return True

        return False

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix:
            return False

        for i in range(min(len(matrix), len(matrix[0]))):
            horizontal_search = self.binary_search(matrix, target, i, False)
            vertical_search = self.binary_search(matrix, target, i, True)
            if horizontal_search or vertical_search:
                return True

        return False


class Solution:
    def binary_search(self, matrix, target, start, vertical):
        low = start
        high = len(matrix[0]) - 1 if vertical else len(matrix) - 1

        while high >= low:
            mid = (low + high) // 2
            if vertical:
                if matrix[start][mid] < target:
                    low = mid + 1
                elif matrix[start][mid] > target:
                    high = mid - 1
                else:
                    return True
            else:
                if matrix[mid][start] < target:
                    low = mid + 1
                elif matrix[mid][start] > target:
                    high = mid - 1
                else:
                    return True

        return False

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix:
            return False

        for i in range(min(len(matrix), len(matrix[0]))):
            vertical_found = self.binary_search(matrix, target, i, True)
            horizontal_found = self.binary_search(matrix, target, i, False)
            if vertical_found or horizontal_found:
                return True

        return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        def binary_search(start, vertical):
            low = start
            high = len(matrix[0]) - 1 if vertical else len(matrix) - 1
            while low <= high:
                mid = (low + high) // 2
                if vertical:
                    if matrix[start][mid] < target:
                        low = mid + 1
                    elif matrix[start][mid] > target:
                        high = mid - 1
                    else:
                        return True
                else:
                    if matrix[mid][start] < target:
                        low = mid + 1
                    elif matrix[mid][start] > target:
                        high = mid - 1
                    else:
                        return True

            return False

        for i in range(min(len(matrix), len(matrix[0]))):
            horizontal_search = binary_search(i, False)
            vertical_search = binary_search(i, True)
            if horizontal_search or vertical_search:
                return True

        return False


## divide and concquer
##############################
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix:
            return False

        def search_recursive(left, up, right, down):
            if left > right or up > down:
                return False
            elif target < matrix[up][left] or target > matrix[down][right]:
                return False

            mid = left + (right - left) // 2
            row = up
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1

            return search_recursive(left, row, mid - 1, down) or search_recursive(
                mid + 1, up, right, row - 1
            )

        return search_recursive(0, 0, len(matrix[0]) - 1, len(matrix) - 1)


## search space reduction
##############################
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not len(matrix) or not len(matrix[0]):
            return False

        height = len(matrix)
        width = len(matrix[0])
        row = height - 1
        col = 0
        while col < width and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:
                return True

        return False


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        height = len(matrix)
        width = len(matrix[0])
        row = height - 1
        col = 0
        while row >= 0 and col < width:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:
                return True

        return False


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(
            Solution().searchMatrix(
                [
                    [1, 4, 7, 11, 15],
                    [2, 5, 8, 12, 19],
                    [3, 6, 9, 16, 22],
                    [10, 13, 14, 17, 24],
                    [18, 21, 23, 26, 30],
                ],
                5,
            ),
            True,
        )
        self.assertEqual(
            Solution().searchMatrix(
                [
                    [1, 4, 7, 11, 15],
                    [2, 5, 8, 12, 19],
                    [3, 6, 9, 16, 22],
                    [10, 13, 14, 17, 24],
                    [18, 21, 23, 26, 30],
                ],
                20,
            ),
            False,
        )


if __name__ == "__main__":
    unittest.main()
