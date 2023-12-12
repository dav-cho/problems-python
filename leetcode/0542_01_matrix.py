##
#### 542. 01 Matrix (medium)
################################


import collections


## TODO: recursive
##############################
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        rows = len(mat)
        cols = len(mat[0])

        result = [[float("inf")] * cols for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    result[row][col] = 0
                else:
                    for r in range(rows):
                        for c in range(cols):
                            if mat[r][c] == 0:
                                dist_01 = abs(r - row) + abs(c - col)
                                result[r][c] = min(result[r][c], dist_01)

        return result


## bfs
##############################
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        rows = len(mat)
        cols = len(mat[0])

        queue = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append(((r, c), 0))

        seen = {x for x, _ in queue}
        res = [[0] * cols for _ in mat]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            (r, c), depth = queue.popleft()
            res[r][c] = depth

            for x, y in directions:
                row = r + x
                col = c + y
                if not 0 <= row < rows or not 0 <= col < cols:
                    continue

                if (row, col) not in seen:
                    seen.add((row, col))
                    queue.append(((row, col), depth + 1))

        return res


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        rows = len(mat)
        cols = len(mat[0])

        def neighbors(r, c):
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for x, y in directions:
                row = r + x
                col = c + y
                if 0 <= row < rows and 0 <= col < cols:
                    yield row, col

        queue = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append(((r, c), 0))

        seen = {x for x, _ in queue}
        res = [[0] * cols for _ in mat]
        while queue:
            (r, c), depth = queue.popleft()
            res[r][c] = depth
            for neighbor in neighbors(r, c):
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, depth + 1))

        return res


## dynamic programming
##############################
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        rows = len(mat)
        cols = len(mat[0])
        res = [[float("inf")] * cols for _ in mat]

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    res[r][c] = 0
                else:
                    if r > 0:
                        row = res[r - 1][c] + 1
                        res[r][c] = min(res[r][c], row)
                    if c > 0:
                        col = res[r][c - 1] + 1
                        res[r][c] = min(res[r][c], col)

        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if r < rows - 1:
                    row = res[r + 1][c] + 1
                    res[r][c] = min(res[r][c], row)
                if c < cols - 1:
                    col = res[r][c + 1] + 1
                    res[r][c] = min(res[r][c], col)

        return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(
            solution.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
            [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
        )
        self.assertEqual(
            solution.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]),
            [[0, 0, 0], [0, 1, 0], [1, 2, 1]],
        )


if __name__ == "__main__":
    unittest.main()
