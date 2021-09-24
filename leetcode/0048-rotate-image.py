##
#### Rotate Image (medium)
########################################

# You are given an n x n 2D matrix representing an image, rotate the image by
# 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the
# input 2D matrix directly. DO NOT allocate another 2D matrix and do the
# rotation.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# Example 2:
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

# Example 3:
# Input: matrix = [[1]]
# Output: [[1]]

# Example 4:
# Input: matrix = [[1,2],[3,4]]
# Output: [[3,1],[4,2]]
 
# Constraints:
# matrix.length == n
# matrix[i].length == n
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000

# Bonus Question:
# If you're not too confident with matrices and linear algebra, get some more
# practice by also coding a method that transposes the matrix on the other
# diagonal, and another that reflects from top to bottom. You can test your
# functions by printing out the matrix before and after each operation. Finally,
# use your functions to find three more solutions to this problem. Each solution
# uses two matrix operations.

# Interview Tip: Terrified of being asked this question in an interview? Many
# people are: it can be intimidating due to the fiddly logic. Unfortunately, if
# you do a lot of interviewing, the probability of seeing it at least once is
# high, and some people have claimed to have seen it multiple times! This is
# one of the few questions where I recommend practicing until you can
# confidently code it and explain it without thinking too much.

################################################################################

## 
##############################
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        pass


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


## 
##############################
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        pass


## 
##############################
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.rotate([[1,2,3],[4,5,6],[7,8,9]]), [[7,4,1],[8,5,2],[9,6,3]])
        self.assertEqual(solution.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]), [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])
        self.assertEqual(solution.rotate([[1]]), [[1]])
        self.assertEqual(solution.rotate([[1,2],[3,4]]), [[3,1],[4,2]])


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Rotate Groups of Four Cells
##############################################
# Time: O(M) - As each cell is getting read once and written once.
# Space: O(1) - Because we do not use any other additional data structures.
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp


## Approach 2: Reverse on Diagonal and then Reverse Left to Right
#####################################################################
# Time: O(M) - Where M is the number of cells in the grid.
# - We perform two steps; transposing the matrix, and then reversing each row.
#   Transposing the matrix has a cost of O(M) because we're moving the value of
#   each cell once. Reversing each row also has a cost of O(M), because again
#   we're moving the value of each cell once.

# Space: O(1)
# - Because we do not use any other additional data structures.
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reflect(matrix)
    
    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]


## Discuss Solutions
########################

## pythonic
##############################
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        matrix[:] = map(list, zip(*matrix[::-1]))


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        matrix[:] = zip(*matrix[::-1])


## most direct
##############################
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        pass


## list comprehension
##############################
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        pass


## flip
##############################
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        pass


