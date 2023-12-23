"""
118. Pascal's Triangle (easy)
"""

from typing import List


class Iterative1:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            row = [None] * (i + 1)
            row[0] = row[-1] = 1
            for j in range(1, i):
                row[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(row)
        return res


class Iterative2:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows == 1:
            return res
        for i in range(1, numRows):
            row = [1]
            for j in range(1, i):
                row.append(res[i - 1][j - 1] + res[i - 1][j])
            row.append(1)
            res.append(row)
        return res
