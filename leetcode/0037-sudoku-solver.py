##
#### 37. Sudoku Solver (hard)
#################################


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
            return not (
                x in rows[row] or x in cols[col] or x in boxes[box_idx(row, col)]
            )

        def place(x, row, col):
            rows[row][x] += 1
            cols[col][x] += 1
            boxes[box_idx(row, col)][x] += 1
            board[row][col] = str(x)

        def remove(x, row, col):
            del rows[row][x]
            del cols[col][x]
            del boxes[box_idx(row, col)][x]
            board[row][col] = "."

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
            if board[row][col] == ".":
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
                if board[i][j] != ".":
                    x = int(board[i][j])
                    place(x, i, j)

        solved = False
        backtrack()


class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        def could_place(x, row, col):
            return not (
                x in rows[row] or x in cols[col] or x in boxes[box_idx(row, col)]
            )

        def place_number(x, row, col):
            rows[row][x] += 1
            cols[col][x] += 1
            boxes[box_idx(row, col)][x] += 1
            board[row][col] = str(x)

        def remove_number(x, row, col):
            del rows[row][x]
            del cols[col][x]
            del boxes[box_idx(row, col)][x]
            board[row][col] = "."

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
            if board[row][col] == ".":
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
                if board[i][j] != ".":
                    x = int(board[i][j])
                    place_number(x, i, j)

        sudoku_solved = False
        backtrack()


class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        def could_place(x, row, col):
            return not (
                x in rows[row] or x in cols[col] or x in boxes[box_idx(row, col)]
            )

        def place_number(x, row, col):
            rows[row][x] += 1
            cols[col][x] += 1
            boxes[box_idx(row, col)][x] += 1
            board[row][col] = str(x)

        def remove_number(x, row, col):
            del rows[row][x]
            del cols[col][x]
            del boxes[box_idx(row, col)][x]
            board[row][col] = "."

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
            if board[row][col] == ".":
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
                if board[i][j] != ".":
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
        self.assertEqual(
            solution.solveSudoku(
                [
                    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                    [".", "9", "8", ".", ".", ".", ".", "6", "."],
                    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                    [".", "6", ".", ".", ".", ".", "2", "8", "."],
                    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
                ]
            ),
            [
                ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
                ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
                ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
                ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
                ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
                ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
                ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
                ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
                ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
            ],
        )


if __name__ == "__main__":
    unittest.main()
