##
#### Maximal Square (medium)
########################################

# Given an m x n binary matrix filled with 0's and 1's, find the largest
# square containing only 1's and return its area.

# Example 1:
# Input: matrix = [["1","0","1","0","0"],
#                  ["1","0","1","1","1"],
#                  ["1","1","1","1","1"],
#                  ["1","0","0","1","0"]]
# Output: 4

# Example 2:
# Input: matrix = [["0","1"],
#                  ["1","0"]]
# Output: 1

# Example 3:
# Input: matrix = [["0"]]
# Output: 0
 
# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] is '0' or '1'.

################################################################################


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
                
                if matrix[row - 1][col - 1] == '1':
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
                
                if matrix[row][col] == '1':
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
                
                if matrix[row - 1][col - 1] == '1':
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
                if matrix[row - 1][col - 1] == '1':
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
                if matrix[row][col] == '1':
                    dp[row][col] = 1 + min(dp[row + 1][col], dp[row][col + 1], dp[row + 1][col + 1])
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
                if matrix[row - 1][col - 1] != '1':
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
                if matrix[row][col] == '1':
                    dp[row + 1][col + 1] = 1 + min(dp[row][col], dp[row + 1][col], dp[row][col + 1])
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
                if matrix[row][col] == '1':
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
                if matrix[row][col] != '1':
                    continue
                    
                S = 1           # length of square
                flag = True
                
                while S + row < R and S + col < C and flag:
                    for k in range(col, S + col + 1):
                        if matrix[row + S][k] == '0':
                            flag = False
                            break
                            
                    for k in range(row, S + row + 1):
                        if matrix[k][col + S] == '0':
                            flag = False
                            break;
                            
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
        self.assertEqual(Solution().maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]), 4)
        self.assertEqual(Solution().maximalSquare([["0","1"],["1","0"]]), 1)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Brute Force [Accepted]
#########################################
# Time: O((mn)^2) - In worst case, we need to traverse the complete matrix for
#                   every 1.
# Space: O(1) - No extra space is used.

## Java
#public class Solution {
#    public int maximalSquare(char[][] matrix) {
#        int rows = matrix.length, cols = rows > 0 ? matrix[0].length : 0;
#        int maxsqlen = 0;
#        for (int i = 0; i < rows; i++) {
#            for (int j = 0; j < cols; j++) {
#                if (matrix[i][j] == '1') {
#                    int sqlen = 1;
#                    boolean flag = true;
#                    while (sqlen + i < rows && sqlen + j < cols && flag) {
#                        for (int k = j; k <= sqlen + j; k++) {
#                            if (matrix[i + sqlen][k] == '0') {
#                                flag = false;
#                                break;
#                            }
#                        }
#                        for (int k = i; k <= sqlen + i; k++) {
#                            if (matrix[k][j + sqlen] == '0') {
#                                flag = false;
#                                break;
#                            }
#                        }
#                        if (flag)
#                            sqlen++;
#                    }
#                    if (maxsqlen < sqlen) {
#                        maxsqlen = sqlen;
#                    }
#                }
#            }
#        }
#        return maxsqlen * maxsqlen;
#    }
#}


## Approach 2: (Dynamic Programming) [Accepted]
###################################################
# Time: O(mn) - Single pass.
# Space: O(mn) - Another matrix of same size is used for dp.

## Java
#public class Solution {
#    public int maximalSquare(char[][] matrix) {
#        int rows = matrix.length, cols = rows > 0 ? matrix[0].length : 0;
#        int[][] dp = new int[rows + 1][cols + 1];
#        int maxsqlen = 0;
#        for (int i = 1; i <= rows; i++) {
#            for (int j = 1; j <= cols; j++) {
#                if (matrix[i-1][j-1] == '1'){
#                    dp[i][j] = Math.min(Math.min(dp[i][j - 1], dp[i - 1][j]), dp[i - 1][j - 1]) + 1;
#                    maxsqlen = Math.max(maxsqlen, dp[i][j]);
#                }
#            }
#        }
#        return maxsqlen * maxsqlen;
#    }
#}


## Approach 3: (Better Dynamic Programming) [Accepted]
##########################################################
# Time: O(mn) - Single pass.
# Space: O(n) - Another array which stores elements in a row is used for dp.

## Java
#public class Solution {
#    public int maximalSquare(char[][] matrix) {
#        int rows = matrix.length, cols = rows > 0 ? matrix[0].length : 0;
#        int[] dp = new int[cols + 1];
#        int maxsqlen = 0, prev = 0;
#        for (int i = 1; i <= rows; i++) {
#            for (int j = 1; j <= cols; j++) {
#                int temp = dp[j];
#                if (matrix[i - 1][j - 1] == '1') {
#                    dp[j] = Math.min(Math.min(dp[j - 1], prev), dp[j]) + 1;
#                    maxsqlen = Math.max(maxsqlen, dp[j]);
#                } else {
#                    dp[j] = 0;
#                }
#                prev = temp;
#            }
#        }
#        return maxsqlen * maxsqlen;
#    }
#}


