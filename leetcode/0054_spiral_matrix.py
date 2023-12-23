"""
54. Spiral matrix (medium)
"""

from typing import List


class Recursive1:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        row = list(matrix.pop(0))
        rotated = list(zip(*matrix))[::-1]
        return row + self.spiralOrder(rotated)


class Iterative1:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        left = 0
        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
            bottom -= 1
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
            left += 1
        return res


class Iterative2:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top = 0
        right = len(matrix[0])
        bottom = len(matrix)
        left = 0
        while top < bottom and left < right:
            for col in range(left, right):
                res.append(matrix[top][col])
            top += 1
            if top == bottom:
                break
            for row in range(top, bottom):
                res.append(matrix[row][right - 1])
            right -= 1
            if left == right:
                break
            for col in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][col])
            bottom -= 1
            for row in range(bottom - 1, top - 1, -1):
                res.append(matrix[row][left])
            left += 1
        return res
