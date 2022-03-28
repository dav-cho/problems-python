##
#### 498. Diagonal Traverse (medium)
########################################


## diagonals and reverse
############################
class Solution:
    def find_diagonal_order(self, mat: list[list[int]]) -> list[int]:
        if not mat or not mat[0]:
            return []

        N = len(mat)
        M = len(mat[0])

        result, intermediate = [], []

        for d in range(N + M - 1):
            intermediate.clear()

            r = 0 if d < M else d - M + 1
            c = d if d < M else M - 1

            while r < N and c > -1:
                intermediate.append(mat[r][c])
                r += 1
                c -= 1

            if d % 2 == 0:
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)

        return result


## sum of indices
#####################
class Solution:
    def find_diagonal_order(self, mat: list[list[int]]) -> list[int]:
        idx_sums = {}

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i + j not in idx_sums:
                    idx_sums[i + j] = [mat[i][j]]
                else:
                    idx_sums[i + j].append(mat[i][j])

        result = []

        for sum in idx_sums.items():
            if sum[0] % 2 == 0:
                result.extend(sum[1][::-1])
            else:
                result.extend(sum[1])

        return result


## TODO: walking
##############
class Solution:
    def find_diagonal_order(self, mat: list[list[int]]) -> list[int]:
        # next up = [row - 1][col + 1]
        # next down = [row + 1][col - 1]

        N, M = len(mat), len(mat[0])
        row = col = 0
        up = True
        result = []

        while row < N and col < M:
            result.append(mat[row][col])

            next_row = row + (-1 if up else 1)
            next_col = col + (1 if up else -1)

            if next_row < 0 or next_row == N or next_col < 0 or next_col == M:
                if up:
                    row += col == M - 1
                    col += col < M - 1
                else:
                    col += row == N - 1
                    row += row < N - 1

                up = not (up)

            else:
                row = next_row
                col = next_col

        return result


class Solution:
    def find_diagonal_order(self, mat: list[list[int]]) -> list[int]:
        # next up   = [row - 1][col + 1]
        # next down = [row + 1][col - 1]

        pass


## Tests
############

test1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
test2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

solution = Solution()
print(solution.find_diagonal_order(test1))
# [1, 2, 4, 7, 5, 3, 6, 8, 9]
# print(solution.find_diagonal_order(test2))
