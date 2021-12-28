##
#### Set Matrix Zeroes (medium)
########################################

# Given an m x n integer matrix matrix, if an element is 0, set its entire
# row and column to 0's, and return the matrix.

# You must do it in place.
 
# Example 1:

# [1,1,1]        [1,0,1]
# [1,0,1]   ->   [0,0,0]
# [1,1,1]        [1,0,1]

# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Example 2:

# [0,1,2,0]        [0,0,0,0]
# [3,4,5,2]   ->   [0,4,5,0]
# [1,3,1,5]        [0,3,1,0]

# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 
# Constraints:
# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -231 <= matrix[i][j] <= 231 - 1

################################################################################


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
        self.assertEqual(Solution().setZeroes([[1,1,1],[1,0,1],[1,1,1]]), [[1,0,1],[0,0,0],[1,0,1]])
        self.assertEqual(Solution().setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]), [[0,0,0,0],[0,4,5,0],[0,3,1,0]])


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Additional Memory Approach
#############################################
# Time: O(M * N) - Where M and N are the number of rows and columns.
# Space: O(M + N)
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C = len(matrix[0])
        rows, cols = set(), set()

        # Essentially, we mark the rows and columns that are to be made zero
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # Iterate over the array once again and using the rows and cols sets, update the elements
        for i in range(R):
            for j in range(C):
                if i in rows or j in cols:
                    matrix[i][j] = 0


## Approach 2: O(1) Space, Efficient Solution
#################################################
# Time: O(M * N)
# Space: O(1)
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        is_col = False
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            # Since first cell for both first row and first column is the same i.e. matrix[0][0]
            # We can use an additional variable for either the first row/column.
            # For this solution we are using an additional variable for the first column
            # and using matrix[0][0] for the first row.
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, C):
                # If an element is zero, we set the first element of the corresponding row and column to 0
                if matrix[i][j]  == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # Iterate over the array once again and using the first row and first column, update the elements.
        for i in range(1, R):
            for j in range(1, C):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        # See if the first row needs to be set to zero as well
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0

        # See if the first column needs to be set to zero as well        
        if is_col:
            for i in range(R):
                matrix[i][0] = 0


