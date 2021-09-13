##
#### Sudoku Solver (hard)
#############################

# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

# 1. Each of the digits 1-9 must occur exactly once in each row.
# 2. Each of the digits 1-9 must occur exactly once in each column.
# 3. Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

# The '.' character indicates empty cells.

# Example 1:
# Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
# Explanation: The input board is shown above and the only valid solution is shown below:

# Constraints:
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit or '.'.
# It is guaranteed that the input board has only one solution.

################################################################################

## 
##############################
class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
## 
##############################
from collections import defaultdict


class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        def could_place(x, row, col):
            return not (x in rows[row] or x in cols[col]
                        or x in boxes[box_idx(row, col)])

        def place(x, row, col):
            rows[row][x] += 1
            cols[col][x] += 1
            boxes[box_idx(row, col)][x] += 1
            board[row][col] = str(x)

        def remove(x, row, col):
            del rows[row][x]
            del cols[col][x]
            del boxes[box_idx(row, col)][x]
            board[row][col] = '.'

        def place_next(row, col):
            if row == N - 1 and col == N - 1:
                nonlocal solved
                solved = True
            else:
                if col == N - 1:
                    backtrack(row + 1, 0)
                else:
                    backtrack(row, col + 1)

        def backtrack(row=0, col=0):
            if board[row][col] == '.':
                for x in range(1, 10):
                    if could_place(x, row, col):
                        place(x, row, col)
                        place_next(row, col)
                        if not solved:
                            remove(x, row, col)
            else:
                place_next(row, col)

        n = 3
        N = n * n
        box_idx = lambda row, col: (row // n) * n + col // n

        rows = [defaultdict(int) for _ in range(N)]
        cols = [defaultdict(int) for _ in range(N)]
        boxes = [defaultdict(int) for _ in range(N)]

        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    x = int(board[i][j])
                    place(x, i, j)

        solved = False
        backtrack()


class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        def could_place(x, row, col):
            return not (x in rows[row] or x in cols[col]
                        or x in boxes[box_idx(row, col)])
        
        def place_number(x, row, col):
            rows[row][x] += 1
            cols[col][x] += 1
            boxes[box_idx(row, col)][x] += 1
            board[row][col] = str(x)
        
        def remove_number(x, row, col):
            del rows[row][x]
            del cols[col][x]
            del boxes[box_idx(row, col)][x]
            board[row][col] = '.'
        
        def place_next_numbers(row, col):
            if row == N - 1 and col == N - 1:
                nonlocal sudoku_solved
                sudoku_solved = True
            else:
                if col == N - 1:
                    backtrack(row + 1, 0)
                else:
                    backtrack(row, col + 1)
                
        def backtrack(row=0, col=0):
            if board[row][col] == '.':
                for x in range(1, 10):
                    if could_place(x, row, col):
                        place_number(x, row, col)
                        place_next_numbers(row, col)
                        if not sudoku_solved:
                            remove_number(x, row, col)
            else:
                place_next_numbers(row, col)
        
        n = 3
        N = n * n
        box_idx = lambda row, col: (row // n) * n + col // n
        
        rows = [defaultdict(int) for _ in range(N)]
        cols = [defaultdict(int) for _ in range(N)]
        boxes = [defaultdict(int) for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    x = int(board[i][j])
                    place_number(x, i, j)
        
        sudoku_solved = False
        backtrack()


class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        def could_place(x, row, col):
            return not (x in rows[row] or x in cols[col]
                        or x in boxes[box_idx(row, col)])
        
        def place_number(x, row, col):
            rows[row][x] += 1
            cols[col][x] += 1
            boxes[box_idx(row, col)][x] += 1
            board[row][col] = str(x)
            
        def remove_number(x, row, col):
            del rows[row][x]
            del cols[col][x]
            del boxes[box_idx(row, col)][x]
            board[row][col] = '.'
            
        def place_next_numbers(row, col):
            if col == N - 1 and row == N - 1:
                nonlocal sudoku_solved
                sudoku_solved = True
            else:
                if col == N - 1:
                    backtrack(row + 1, 0)
                else:
                    backtrack(row, col + 1)
                    
        def backtrack(row=0, col=0):
            if board[row][col] == '.':
                for x in range(1, 10):
                    if could_place(x, row, col):
                        place_number(x, row, col)
                        place_next_numbers(row, col)
                        if not sudoku_solved:
                            remove_number(x, row, col)
            else:
                place_next_numbers(row, col)
                
        n = 3
        N = n * n
        box_idx = lambda row, col: (row // n) * n + col // n
        
        rows = [defaultdict(int) for i in range(N)]
        cols = [defaultdict(int) for i in range(N)]
        boxes = [defaultdict(int) for i in range(N)]
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    x = int(board[i][j])
                    place_number(x, i, j)
                    
        sudoku_solved = False
        backtrack()

        # do not need to return anything
        # but returned here for tests below
        return board


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.solveSudoku([
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]]),
            [
            ["5","3","4","6","7","8","9","1","2"],
            ["6","7","2","1","9","5","3","4","8"],
            ["1","9","8","3","4","2","5","6","7"],
            ["8","5","9","7","6","1","4","2","3"],
            ["4","2","6","8","5","3","7","9","1"],
            ["7","1","3","9","2","4","8","5","6"],
            ["9","6","1","5","3","7","2","8","4"],
            ["2","8","7","4","1","9","6","3","5"],
            ["3","4","5","2","8","6","1","7","9"]])


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Backtracking
###############################
# Time complexity is constant here since the board size is fixed and there is
# no N-parameter to measure. Though let's discuss the number of operations
# needed : (9!)^9. Let's consider one row, i.e. not more than 9 cells to fill.
# There are not more than 9 possibilities for the first number to put, not more
# than 9×8 for the second one, not more than 9×8×7 for the third one etc. In
# total that results in not more than 9! possibilities for a just one row, that
# means not more than (9!)^9 operations in total. Let's compare:
# - 9^(81) =
#   196627050475552913618075908526912116283103450944214766927315415537966391196809
#   for the brute force,
# - and (9!)^9 = 109110688415571316480344899355894085582848000000000(9!) for
#   the standard backtracking, i.e. the number of operations is reduced in
#   10^(27)!
 
# Space:
# - The board size is fixed, and the space is used to store board, rows, columns
#   and boxes structures, each contains 81 elements.

from collections import defaultdict
class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def could_place(d, row, col):
            """
            Check if one could place a number d in (row, col) cell
            """
            return not (d in rows[row] or d in columns[col] or \
                    d in boxes[box_index(row, col)])
        
        def place_number(d, row, col):
            """
            Place a number d in (row, col) cell
            """
            rows[row][d] += 1
            columns[col][d] += 1
            boxes[box_index(row, col)][d] += 1
            board[row][col] = str(d)
            
        def remove_number(d, row, col):
            """
            Remove a number which didn't lead 
            to a solution
            """
            del rows[row][d]
            del columns[col][d]
            del boxes[box_index(row, col)][d]
            board[row][col] = '.'    
            
        def place_next_numbers(row, col):
            """
            Call backtrack function in recursion
            to continue to place numbers
            till the moment we have a solution
            """
            # if we're in the last cell
            # that means we have the solution
            if col == N - 1 and row == N - 1:
                nonlocal sudoku_solved
                sudoku_solved = True
            #if not yet    
            else:
                # if we're in the end of the row
                # go to the next row
                if col == N - 1:
                    backtrack(row + 1, 0)
                # go to the next column
                else:
                    backtrack(row, col + 1)
                
                
        def backtrack(row = 0, col = 0):
            """
            Backtracking
            """
            # if the cell is empty
            if board[row][col] == '.':
                # iterate over all numbers from 1 to 9
                for d in range(1, 10):
                    if could_place(d, row, col):
                        place_number(d, row, col)
                        place_next_numbers(row, col)
                        # if sudoku is solved, there is no need to backtrack
                        # since the single unique solution is promised
                        if not sudoku_solved:
                            remove_number(d, row, col)
            else:
                place_next_numbers(row, col)
                    
        # box size
        n = 3
        # row size
        N = n * n
        # lambda function to compute box index
        box_index = lambda row, col: (row // n ) * n + col // n
        
        # init rows, columns and boxes
        rows = [defaultdict(int) for i in range(N)]
        columns = [defaultdict(int) for i in range(N)]
        boxes = [defaultdict(int) for i in range(N)]
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.': 
                    d = int(board[i][j])
                    place_number(d, i, j)
        
        sudoku_solved = False
        backtrack()


## Approach 2: 
##############################
# Time: 
# Space: 


## Approach 3: 
##############################
# Time: 
# Space: 


