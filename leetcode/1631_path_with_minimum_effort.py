##
#### 1631. Path With Minimum Effort (medium)
################################################


import heapq


## dijkstra's algorithm
##############################
class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        seen = [[None] * cols for _ in range(rows)]
        diffs = [[float("inf")] * cols for _ in range(rows)]
        diffs[0][0] = 0
        pq = [(0, 0, 0)]

        while pq:
            diff, row, col = heapq.heappop(pq)
            seen[row][col] = True

            for y, x in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                r = row + y
                c = col + x

                if not (0 <= r < rows and 0 <= c < cols) or seen[r][c]:
                    continue

                curr_diff = abs(heights[row][col] - heights[r][c])
                max_diff = max(curr_diff, diffs[row][col])

                if diffs[r][c] > max_diff:
                    diffs[r][c] = max_diff
                    heapq.heappush(pq, (max_diff, r, c))

        return diffs[-1][-1]


class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        diffs = [[float("inf")] * cols for _ in range(rows)]
        diffs[0][0] = 0
        seen = [[False] * cols for _ in range(rows)]
        pq = [(0, 0, 0)]

        while pq:
            diff, row, col = heapq.heappop(pq)
            seen[row][col] = True

            for y, x in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                r = row + y
                c = col + x

                if 0 <= r < rows and 0 <= c < cols and not seen[r][c]:
                    curr_diff = abs(heights[row][col] - heights[r][c])
                    max_diff = max(curr_diff, diffs[row][col])

                    if diffs[r][c] > max_diff:
                        diffs[r][c] = max_diff
                        heapq.heappush(pq, (max_diff, r, c))

        return diffs[-1][-1]


class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        diff_matrix = [[float("inf")] * cols for _ in range(rows)]
        diff_matrix[0][0] = 0
        seen = [[False] * cols for _ in range(rows)]
        queue = [(0, 0, 0)]

        while queue:
            diff, row, col = heapq.heappop(queue)
            seen[row][col] = True

            for y, x in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                r = row + y
                c = col + x

                if not 0 <= r < rows or not 0 <= c < cols or seen[r][c]:
                    continue

                curr_diff = abs(heights[r][c] - heights[row][col])
                max_diff = max(curr_diff, diff_matrix[row][col])

                if max_diff < diff_matrix[r][c]:
                    diff_matrix[r][c] = max_diff
                    heapq.heappush(queue, (max_diff, r, c))

        return diff_matrix[-1][-1]


## union find - disjoint set
##############################
class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])

        if rows == 1 and cols == 1:
            return 0

        edges = []

        for row in range(rows):
            for col in range(cols):
                if row > 0:
                    diff = abs(heights[row][col] - heights[row - 1][col])
                    edges.append((diff, row * cols + col, (row - 1) * cols + col))
                if col > 0:
                    diff = abs(heights[row][col] - heights[row][col - 1])
                    edges.append((diff, row * cols + col, row * cols + col - 1))

        edges.sort()
        uf = UnionFind(rows * cols)

        for diff, y, x in edges:
            uf.union(x, y)

            if uf.find(0) == uf.find(rows * cols - 1):
                return diff

        return -1


class UnionFind:
    def __init__(self, size):
        self.root = list(range(size))
        self.rank = [1] * size

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])

        return self.root[x]

    def union(self, x, y):
        root_x, root_y = map(self.find, (x, y))

        if root_x == root_y:
            return

        if self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = root_y
        else:
            self.root[root_y] = root_x

            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1


## binary search bfs
##############################
from collections import deque


class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])

        def can_reach(mid):
            seen = [[False] * cols for _ in range(rows)]
            queue = deque([(0, 0)])

            while queue:
                row, col = queue.popleft()

                if row == rows - 1 and col == cols - 1:
                    return True

                seen[row][col] = True

                for y, x in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    r = row + y
                    c = col + x

                    if not (0 <= r < rows and 0 <= c < cols) or seen[r][c]:
                        continue

                    diff = abs(heights[row][col] - heights[r][c])

                    if diff <= mid:
                        queue.append((r, c))
                        seen[r][c] = True

            return False

        left = 0
        right = 10**6

        while left < right:
            mid = (left + right) // 2

            if can_reach(mid):
                right = mid
            else:
                left = mid + 1

        return left


class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])

        def can_reach(mid):
            seen = [[False] * cols for _ in range(rows)]
            queue = deque([(0, 0)])

            while queue:
                row, col = queue.popleft()

                if row == rows - 1 and col == cols - 1:
                    return True

                seen[row][col] = True

                for y, x in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    r = row + y
                    c = col + x

                    if not (0 <= r < rows and 0 <= c < cols) or seen[r][c]:
                        continue

                    curr_diff = abs(heights[row][col] - heights[r][c])

                    if curr_diff <= mid:
                        seen[r][c] = True
                        queue.append((r, c))

        left = 0
        right = 10**6

        while left < right:
            mid = (left + right) // 2

            if can_reach(mid):
                right = mid
            else:
                left = mid + 1

        return left


class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])

        def can_reach(mid):
            seen = [[False] * cols for _ in range(rows)]
            queue = deque([(0, 0)])

            while queue:
                row, col = queue.popleft()

                if row == rows - 1 and col == cols - 1:
                    return True

                seen[row][col] = True

                for y, x in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    r = row + y
                    c = col + x

                    if not (0 <= r < rows and 0 <= c < cols) or seen[r][c]:
                        continue

                    curr_diff = abs(heights[r][c] - heights[row][col])

                    if curr_diff <= mid:
                        seen[r][c] = True
                        queue.append((r, c))

        left = 0
        right = 10**6

        while left < right:
            mid = (left + right) // 2

            if can_reach(mid):
                right = mid
            else:
                left = mid + 1

        return left


## binary search dfs
##############################
class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])

        def can_reach(row, col, mid):
            if row == rows - 1 and col == cols - 1:
                return True

            seen[row][col] = True

            for y, x in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                r = row + y
                c = col + x

                if not (0 <= r < rows and 0 <= c < cols) or seen[r][c]:
                    continue

                diff = abs(heights[row][col] - heights[r][c])

                if diff <= mid:
                    seen[r][c] = True

                    if can_reach(r, c, mid):
                        return True

            return False

        left = 0
        right = 10**6

        while left < right:
            seen = [[False] * cols for _ in range(rows)]
            mid = (left + right) // 2

            if can_reach(0, 0, mid):
                right = mid
            else:
                left = mid + 1

        return left


## dynamic programming (TLE)
################################
class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        M = len(heights)
        N = len(heights[0])
        self.max_so_far = float("inf")

        def dfs(x, y, max_difference):
            if x == M - 1 and y == N - 1:
                self.max_so_far = min(self.max_so_far, max_difference)

                return max_difference

            curr_height = heights[x][y]
            heights[x][y] = 0
            min_effort = float("inf")

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                adjacent_x = x + dx
                adjacent_y = y + dy

                if (
                    0 <= adjacent_x < M
                    and 0 <= adjacent_y < N
                    and heights[adjacent_x][adjacent_y] != 0
                ):
                    curr_difference = abs(heights[adjacent_x][adjacent_y] - curr_height)
                    max_curr_difference = max(max_difference, curr_difference)

                    if max_curr_difference < self.max_so_far:
                        result = dfs(adjacent_x, adjacent_y, max_curr_difference)

                        min_effort = min(min_effort, result)

            heights[x][y] = curr_height

            return min_effort

        return dfs(0, 0, 0)


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(
            solution.minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]), 2
        )
        # self.assertEqual(solution.minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]]), 1)
        # self.assertEqual(solution.minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]), 0)


if __name__ == "__main__":
    unittest.main()
