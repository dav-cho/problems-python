"""
498. Diagonal Traverse (medium)
"""

from collections import defaultdict
from itertools import product
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diags = defaultdict(list)
        for i, j in product(range(len(mat)), range(len(mat[0]))):
            diags[i + j].append(mat[i][j])
        for n, diag in diags.items():
            if not n % 2:
                diags[n] = diags[n][::-1]
        res = []
        for diag in diags.values():
            res += diag
        return res
