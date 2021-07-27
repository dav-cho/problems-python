##
#### Spiral matrix (medium)
###############################

# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

################################################################################


# east =    [col + 1]
# south =   [row + 1]
# west =    [col - 1]
# north =   [row - 1]
## simulation
#################
class Solution:
    def spiral_order(self, matrix: list[list[int]]) -> list[int]:
        if not matrix:
            return []

        N, M = len(matrix), len(matrix[0])
        seen = [[False] * M for _ in matrix]
        result = []
        dir_row = [0, 1, 0, -1]
        dir_col = [1, 0, -1, 0]
        row = col = dir_i = 0

        for _ in range(N * M):
            result.append(matrix[row][col])
            seen[row][col] = True

            next_row = row + dir_row[dir_i]
            next_col = col + dir_col[dir_i]

            if (0 <= next_row < N and
                    0 <= next_col < M and
                    not seen[next_row][next_col]):
                row, col = next_row, next_col
            else:
                dir_i = (dir_i + 1) % 4
                row, col = row + dir_row[dir_i], col + dir_col[dir_i]

        return result


## layer by layer
#####################
class Solution:
    def spiral_order(self, matrix: list[list[int]]) -> list[int]:
        left = top = 0
        right, bottom = len(matrix) - 1, len(matrix[0]) - 1
        result = []
        seen = [[None] * (bottom + 1) for row in matrix]

        while left <= right and top <= bottom:
            row = top
            for col in range(right + 1):
                if not seen[row][col]:
                    result.append(matrix[row][col])
                    seen[row][col] = True
            top += 1
            print('top', top)
            print(result)

            col = right
            for row in range(top, bottom + 1):
                if not seen[row][col]:
                    result.append(matrix[row][col])
                    seen[row][col] = True
            right -= 1
            print('right', right)
            print(result)

            row = bottom
            for col in range(right, left - 1, -1):
                if not seen[row][col]:
                    result.append(matrix[row][col])
                    seen[row][col] = True
            bottom -= 1
            print('bottom', bottom)
            print(result)

            col = left
            for row in range(bottom, top):
                if not seen[row][col]:
                    result.append(matrix[row][col])
                    seen[row][col] = True
            left += 1
            print('left', left)
            print(result)

        return result


## Tests
############

test1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
test2 = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12]
]

solution = Solution()
print(solution.spiral_order(test1))
# Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

print(solution.spiral_order(test2))
# Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]


## LeetCode Solutions
#########################

## Approach 1: Simulation
#############################
# time: O(n) - where n is total number of elements in the input matrix
# space: O(n) - information stored in seen and in ans
class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix: return []
        R, C = len(matrix), len(matrix[0])
        seen = [[False] * C for _ in matrix]
        ans = []
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for _ in range(R * C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return ans


## Approach 2: Layer-by-Layer
#################################
# time: O(n) - where n is total number of elements in the input matrix.
# space: O(1) - without considering the output array.
#        O(n) - if the output array is taken into account.
class Solution(object):
    def spiralOrder(self, matrix):
        def spiral_coords(r1, c1, r2, c2):
            for c in range(c1, c2 + 1):
                yield r1, c
            for r in range(r1 + 1, r2 + 1):
                yield r, c2
            if r1 < r2 and c1 < c2:
                for c in range(c2 - 1, c1, -1):
                    yield r2, c
                for r in range(r2, r1, -1):
                    yield r, c1

        if not matrix: return []
        ans = []
        r1, r2 = 0, len(matrix) - 1
        c1, c2 = 0, len(matrix[0]) - 1
        while r1 <= r2 and c1 <= c2:
            for r, c in spiral_coords(r1, c1, r2, c2):
                ans.append(matrix[r][c])
            r1 += 1; r2 -= 1
            c1 += 1; c2 -= 1
        return ans

