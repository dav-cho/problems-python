##
#### Valid Sudoku (easy)
########################################

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
# validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9
# without repetition.

# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
 
# Example 1:
# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

# Example 2:
# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 
# Constraints:
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.

################################################################################

## bitmasking
##############################
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        N = 9
        rows = [0] * N
        cols = [0] * N
        subs = [0] * N
        
        for row in range(N):
            for col in range(N):
                if board[row][col] == '.':
                    continue
                    
                num = int(board[row][col])
                sub = row // 3 * 3 + col // 3
                
                check_rows = rows[row] & (1 << num - 1)
                check_cols = cols[col] & (1 << num - 1)
                check_subs = subs[sub] & (1 << num - 1)
                
                if check_rows or check_cols or check_subs:
                    return False
                
                rows[row] |= 1 << num - 1
                cols[col] = cols[col] | (1 << num - 1)
                subs[sub] |= 1 << num - 1
                
        return True


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        N = len(board)
        rows = [0] * N
        cols = [0] * N
        subs = [0] * N
        
        for row in range(N):
            for col in range(N):
                if board[row][col] == '.':
                    continue
                    
                left_shift = 1 << (int(board[row][col]) - 1)
                sub = row // 3 * 3 + col // 3
                
                check_rows = rows[row] & left_shift
                check_cols = cols[col] & left_shift
                check_subs = subs[sub] & left_shift
                
                if check_rows or check_cols or check_subs:
                    return False
                
                rows[row] |= left_shift
                cols[col] |= left_shift
                subs[sub] |= left_shift
                
        return True


## hash set
##############################
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        N = 9
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        subs = [set() for _ in range(N)]
        
        for row in range(N):
            for col in range(N):
                num = board[row][col]
                sub = row // 3 * 3 + col // 3
                
                if num != '.':
                    if num in rows[row] or num in cols[col] or num in subs[sub]:
                        return False;
                    
                    rows[row].add(num)
                    cols[col].add(num)
                    subs[sub].add(num)
                
        return True


## first attempt
##############################
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subs = [set() for _ in range(9)]
        
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if not num.isdigit():
                    continue
                
                if num in rows[row]:
                    return False
                rows[row].add(num)

                if num in cols[col]:
                    return False
                cols[col].add(num)
                
                r = (row // 3) * 3
                c = col // 3
                if num in subs[r + c]:
                    return False
                subs[r + c].add(num)
                    
        return True


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subs = [set() for _ in range(9)]
        
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if not num.isdigit():
                    continue
                
                if num in rows[row]:
                    return False
                else:
                    rows[row].add(num)

                if num in cols[col]:
                    return False
                else:
                    cols[col].add(num)
                
                r = (row // 3) * 3
                c = col // 3
                if num in subs[r + c]:
                    return False
                else:
                    subs[r + c].add(num)
                    
        return True


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        subs = [[] for _ in range(9)]
        
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if not num.isdigit():
                    continue
                
                rows[row].append(num)
                cols[col].append(num)
                
                r = (row // 3) * 3
                c = col // 3
                subs[r + c].append(num)
                    
        for row in rows:
            if len(set(row)) != len(row):
                return False
        for col in cols:
            if len(set(col)) != len(col):
                return False
        for sub in subs:
            if len(set(sub)) != len(sub):
                return False
            
        return True


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.isValidSudoku(
            [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]), True)
        self.assertEqual(solution.isValidSudoku(
            [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]), False)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Hash Set
##############################
# Time: O(N^2) - Because we need to traverse every position in the board, and
#                each of the four check steps in an O(1) operation.
# Space: O(N^2) - because in the worst-case scenario, if the board is full, we
#                 need a hash set each with size N to store all seen numbers for
#                 each of the N rows, N columns, and N boxes, respectively.

# Let N be the board length, which is 9 in this question. Note that since the
# value of N is fixed, the time and space complexity of this algorithm can be
# interpreted as O(1). However, to better compare each of the presented
# approaches, we will treat N as an arbitrary value in the complexity analysis.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9

        # Use hash set to record the status
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                val = board[r][c]
                # Check if the position is filled with number
                if val == ".":
                    continue

                # Check the row
                if val in rows[r]:
                    return False
                rows[r].add(val)

                # Check the column
                if val in cols[c]:
                    return False
                cols[c].add(val)

                # Check the box
                idx = (r // 3) * 3 + c // 3
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)

        return True


## Approach 2: Array of Fixed Length
########################################
# Time: O(N^2) - Because we need to traverse every position in the board, and
#                each of the four check steps is an O(1) operation.
# Space: O(N^2) - Because we need to create 3N arrays each with size N to store
#                 all previously seen numbers for all rows, columns, and boxes.

# Let N be the board length, which is 9 in this question. Note that since the
# value of N is fixed, the time and space complexity of this algorithm can be
# interpreted as O(1). However, to better compare each of the presented
# approaches, we will treat N as an arbitrary value in the complexity analysis.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9

        # Use an array to record the status
        rows = [[0] * N for _ in range(N)]
        cols = [[0] * N for _ in range(N)]
        boxes = [[0] * N for _ in range(N)]

        for r in range(N):
            for c in range(N):
                # Check if the position is filled with number
                if board[r][c] == ".":
                    continue

                pos = int(board[r][c]) - 1

                # Check the row
                if rows[r][pos] == 1:
                    return False
                rows[r][pos] = 1

                # Check the column
                if cols[c][pos] == 1:
                    return False
                cols[c][pos] = 1

                # Check the box
                idx = (r // 3) * 3 + c // 3
                if boxes[idx][pos] == 1:
                    return False
                boxes[idx][pos] = 1

        return True


## Approach 3: 
##############################
# Time: 
# Space: 


