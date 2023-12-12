##
#### 36. Valid Sudoku (easy)
########################################


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
                if board[row][col] == ".":
                    continue

                num = int(board[row][col]) - 1
                sub = row // 3 * 3 + col // 3
                check_rows = rows[row] & (1 << num)
                check_cols = cols[col] & (1 << num)
                check_subs = subs[sub] & (1 << num)

                if check_rows or check_cols or check_subs:
                    return False

                rows[row] |= 1 << num
                cols[col] |= 1 << num
                subs[sub] |= 1 << num

        return True


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        N = 9
        rows = [0] * N
        cols = [0] * N
        subs = [0] * N

        for row in range(N):
            for col in range(N):
                if board[row][col] == ".":
                    continue

                num = int(board[row][col]) - 1

                if rows[row] & (1 << num):
                    return False
                rows[row] |= 1 << num

                if cols[col] & (1 << num):
                    return False
                cols[col] |= 1 << num

                sub = row // 3 * 3 + col // 3
                if subs[sub] & (1 << num):
                    return False
                subs[sub] |= 1 << num

        return True


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        N = 9
        rows = [0] * N
        cols = [0] * N
        subs = [0] * N

        for row in range(N):
            for col in range(N):
                if board[row][col] == ".":
                    continue

                num = int(board[row][col])
                sub = row // 3 * 3 + col // 3

                check_rows = rows[row] & (1 << num - 1)
                check_cols = cols[col] & (1 << num - 1)
                check_subs = subs[sub] & (1 << num - 1)

                if check_rows or check_cols or check_subs:
                    return False

                rows[row] |= 1 << num - 1
                cols[col] |= 1 << num - 1
                subs[sub] |= 1 << num - 1

        return True


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        N = 9
        rows = [0] * N
        cols = [0] * N
        subs = [0] * N

        for row in range(N):
            for col in range(N):
                if board[row][col] == ".":
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
                if board[row][col] == ".":
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

                if num != ".":
                    if num in rows[row] or num in cols[col] or num in subs[sub]:
                        return False

                    rows[row].add(num)
                    cols[col].add(num)
                    subs[sub].add(num)

        return True


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(
            solution.isValidSudoku(
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
            True,
        )
        self.assertEqual(
            solution.isValidSudoku(
                [
                    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
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
            False,
        )


if __name__ == "__main__":
    unittest.main()
