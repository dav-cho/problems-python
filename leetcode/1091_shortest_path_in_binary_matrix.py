##
#### 1091. Shortest Path in Binary Matrix (medium)
######################################################


## bfs overwriting input
##############################
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        def get_neighbors(row, col):
            for y, x in dirs:
                r = row + y
                c = col + x

                if not (0 <= r < M and 0 <= c < N):
                    continue
                if grid[r][c] != 0:
                    continue

                yield (r, c)

        if grid[0][0] != 0 or grid[M - 1][N - 1] != 0:
            return -1

        queue = deque([(0, 0)])
        grid[0][0] = 1

        while queue:
            row, col = queue.popleft()
            distance = grid[row][col]
            if (row, col) == (M - 1, N - 1):
                return distance

            for r, c in get_neighbors(row, col):
                grid[r][c] = distance + 1
                queue.append((r, c))

        return -1


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        def get_neighbors(row, col):
            for y, x in dirs:
                r = row + y
                c = col + x

                if not (0 <= r < N and 0 <= c < M):
                    continue
                if grid[r][c] != 0:
                    continue

                yield (r, c)

        if grid[0][0] != 0 or grid[N - 1][M - 1] != 0:
            return -1

        queue = deque([(0, 0)])
        grid[0][0] = 1

        while queue:
            row, col = queue.popleft()
            distance = grid[row][col]
            if (row, col) == (N - 1, M - 1):
                return distance

            for r, c in get_neighbors(row, col):
                grid[r][c] = distance + 1
                queue.append((r, c))

        return -1


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        def get_neighbors(row, col):
            for y, x in dirs:
                r = row + y
                c = col + x
                if not (0 <= r < N and 0 <= c < M):
                    continue
                if grid[r][c] != 0:
                    continue

                yield (r, c)

        if grid[0][0] != 0 or grid[N - 1][M - 1] != 0:
            return -1

        queue = deque([(0, 0)])
        grid[0][0] = 1

        while queue:
            row, col = queue.popleft()
            distance = grid[row][col]
            if (row, col) == (N - 1, M - 1):
                return distance

            for neighbor_row, neighbor_col in get_neighbors(row, col):
                grid[neighbor_row][neighbor_col] = distance + 1
                queue.append((neighbor_row, neighbor_col))

        return -1


## bfs without overwriting input
##############################

## keep track of distance in queue
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        def get_neighbors(row, col):
            for y, x in dirs:
                r = row + y
                c = col + x

                if not (0 <= r < N and 0 <= c < M):
                    continue
                if grid[r][c] != 0:
                    continue

                yield (r, c)

        if grid[0][0] != 0 or grid[N - 1][M - 1] != 0:
            return -1

        queue = deque([(0, 0, 1)])
        visited = {(0, 0)}

        while queue:
            row, col, dist = queue.popleft()
            if (row, col) == (N - 1, M - 1):
                return dist

            for neighbor in get_neighbors(row, col):
                if neighbor not in visited:
                    queue.append((*neighbor, dist + 1))
                    visited.add(neighbor)

        return -1


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        def get_neighbors(row, col):
            for y, x in dirs:
                r = row + y
                c = col + x

                if not (0 <= r < N and 0 <= c < M):
                    continue
                if grid[r][c] != 0:
                    continue

                yield (r, c)

        if grid[0][0] != 0 or grid[N - 1][M - 1] != 0:
            return -1

        queue = deque([(0, 0, 1)])
        visited = {(0, 0)}

        while queue:
            row, col, dist = queue.popleft()
            if (row, col) == (N - 1, M - 1):
                return dist

            for r, c in get_neighbors(row, col):
                if (r, c) not in visited:
                    queue.append((r, c, dist + 1))
                    visited.add((r, c))

        return -1


## start a new collection for each distance
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        def get_neighbors(row, col):
            for y, x in dirs:
                r = row + y
                c = col + x

                if not (0 <= r < N and 0 <= c < M):
                    continue
                if grid[r][c] != 0:
                    continue

                yield (r, c)

        if grid[0][0] != 0 or grid[N - 1][M - 1] != 0:
            return -1

        curr_level = [(0, 0)]
        next_level = []
        visited = {(0, 0)}
        curr_dist = 1

        while curr_level:
            for row, col in curr_level:
                if (row, col) == (N - 1, M - 1):
                    return curr_dist

                for neighbor in get_neighbors(row, col):
                    if neighbor not in visited:
                        next_level.append(neighbor)
                        visited.add(neighbor)

            curr_dist += 1
            curr_level = next_level
            next_level = []

        return -1


## keeping track of how many cells at each distance are in the queue
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        def get_neighbors(row, col):
            for y, x in dirs:
                r = row + y
                c = col + x

                if not (0 <= r < N and 0 <= c < M):
                    continue
                if grid[r][c] != 0:
                    continue

                yield (r, c)

        if grid[0][0] != 0 or grid[N - 1][M - 1] != 0:
            return -1

        queue = deque([(0, 0)])
        visited = {(0, 0)}
        curr_dist = 1

        while queue:
            nodes_of_curr_dist = len(queue)
            for _ in range(nodes_of_curr_dist):
                row, col = queue.popleft()
                if (row, col) == (N - 1, M - 1):
                    return curr_dist

                for neighbor in get_neighbors(row, col):
                    if neighbor in visited:
                        continue

                    queue.append(neighbor)
                    visited.add(neighbor)

            curr_dist += 1

        return -1


##
####################################
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        pass


## A*
##############################
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.shortestPathBinaryMatrix([[0, 1], [1, 0]]), 2)
        self.assertEqual(
            solution.shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]), 4
        )
        self.assertEqual(
            solution.shortestPathBinaryMatrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]), -1
        )


if __name__ == "__main__":
    unittest.main()
