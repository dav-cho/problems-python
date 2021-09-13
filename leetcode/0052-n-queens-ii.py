##
#### N-Queens II (Hard)
###########################

# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
# such that no two queens attack each other.

# Given an integer n, return the number of distinct solutions to the n-queens
# puzzle.

# Example 1:
# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

# Example 2:
# Input: n = 1
# Output: 1

# Constraints:
# 1 <= n <= 9

################################################################################

## backtracking
##############################
class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, diagonals, anti_diagonals, cols):
            if row == n:
                return 1
            
            res = 0
            
            for col in range(n):
                curr_diagonal = row - col
                curr_anti_diagonal = row + col
                
                if (col in cols
                        or curr_diagonal in diagonals
                        or curr_anti_diagonal in anti_diagonals):
                    continue
                    
                cols.add(col)
                diagonals.add(curr_diagonal)
                anti_diagonals.add(curr_anti_diagonal)
                
                res += backtrack(row + 1, diagonals, anti_diagonals, cols)
                
                cols.remove(col)
                diagonals.remove(curr_diagonal)
                anti_diagonals.remove(curr_anti_diagonal)
                
            return res
        
        return backtrack(0, set(), set(), set())


class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, diagonals, anti_diagonals, cols):
            if row == n:
                return 1
            
            solutions = 0
            for col in range(n):
                curr_diagonal  = row - col
                curr_anti_diagonal = row + col
                if (col in cols
                        or curr_diagonal in diagonals
                        or curr_anti_diagonal in anti_diagonals):
                    continue
                
                cols.add(col)
                diagonals.add(curr_diagonal)
                anti_diagonals.add(curr_anti_diagonal)
                
                solutions += backtrack(row + 1, diagonals, anti_diagonals, cols)
                
                cols.remove(col)
                diagonals.remove(curr_diagonal)
                anti_diagonals.remove(curr_anti_diagonal)
            
            return solutions
        
        return backtrack(0, set(), set(), set())


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.totalNQueens(4), 2)
        self.assertEqual(solution.totalNQueens(1), 1)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Backtracking
###############################
# Time: O(N!) - Where N is the number of queens (which is the same as the width
#               and height of the board).
# - Unlike the brute force approach, we place a queen only on squares that aren't
#   attacked. For the first queen, we have N options. For the next queen, we
#   won't attempt to place it in the same column as the first queen, and there
#   must be at least one square attacked diagonally by the first queen as well. Thus, the maximum number of squares we can consider for the second queen is N - 2N−2. For the third queen, we won't attempt to place it in 2 columns already occupied by the first 2 queens, and there must be at least two squares attacked diagonally from the first 2 queens. Thus, the maximum number of squares we can consider for the third queen is N - 4N−4. This pattern continues, giving an approximate time complexity of N!N! at the end.

# Space: O(N) - where N is the number of queens (which is the same as the width
#               and height of the board).
# - Extra memory used includes the 3 sets used to store board state, as well as
#   the recursion call stack. All of this scales linearly with the number of
#   queens.

class Solution:
    def totalNQueens(self, n):
        def backtrack(row, diagonals, anti_diagonals, cols):
            # Base case - N queens have been placed
            if row == n:
                return 1

            solutions = 0
            for col in range(n):
                curr_diagonal = row - col
                curr_anti_diagonal = row + col
                # If the queen is not placeable
                if (col in cols 
                      or curr_diagonal in diagonals 
                      or curr_anti_diagonal in anti_diagonals):
                    continue

                # "Add" the queen to the board
                cols.add(col)
                diagonals.add(curr_diagonal)
                anti_diagonals.add(curr_anti_diagonal)

                # Move on to the next row with the updated board state
                solutions += backtrack(row + 1, diagonals, anti_diagonals, cols)

                # "Remove" the queen from the board since we have already
                # explored all valid paths using the above function call
                cols.remove(col)
                diagonals.remove(curr_diagonal)
                anti_diagonals.remove(curr_anti_diagonal)

            return solutions

        return backtrack(0, set(), set(), set())


