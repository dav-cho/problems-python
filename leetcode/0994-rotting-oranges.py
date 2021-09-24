##
#### Rotting Oranges
########################################

# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten
# orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a
# fresh orange. If this is impossible, return -1.

# Example 1:
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4

# Example 2:
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never
#              rotten, because rotting only happens 4-directionally.

# Example 3:
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer
#              is just 0.
 
# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.

################################################################################

## bfs
##############################
from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        fresh_oranges = 0
        queue = deque()
        
        for row in range(N):
            for col in range(M):
                if grid[row][col] == 1:
                    fresh_oranges += 1
                if grid[row][col] == 2:
                    queue.append((row, col))
                    
        queue.append((None, None))
        minutes = -1
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            row, col = queue.popleft()
            if row == None:
                minutes += 1
                if queue:
                    queue.append((None, None))
            else:
                for y, x in dirs:
                    r = row + y
                    c = col + x
                    if not (0 <= r < N and 0 <= c < M):
                        continue

                    if grid[r][c] == 1:
                        grid[r][c] = 2
                        fresh_oranges -= 1
                        queue.append((r, c))
                        
        return minutes if fresh_oranges == 0 else -1


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
                N = len(grid)
        M = len(grid[0])
        fresh_oranges = 0
        queue = deque()
        
        for row in range(N):
            for col in range(M):
                if grid[row][col] == 1:
                    fresh_oranges += 1
                if grid[row][col] == 2:
                    queue.append((row, col))
                    
        queue.append((None, None))
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minutes = -1
        
        while queue:
            row, col = queue.popleft()
            if row == None:
                minutes += 1
                if queue:
                    queue.append((None, None))
                continue
                
            for y, x in dirs:
                r = row + y
                c = col + x
                if not (0 <= r < N and 0 <= c < M):
                    continue
                    
                if grid[r][c] == 1:
                    grid[r][c] = 2
                    fresh_oranges -= 1
                    queue.append((r, c))
                    
        return minutes if fresh_oranges == 0 else -1


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        queue = deque()
        fresh_oranges = 0
        
        for row in range(N):
            for col in range(M):
                if grid[row][col] == 2:
                    queue.append((row, col))
                if grid[row][col] == 1:
                    fresh_oranges += 1
                    
        queue.append((-1, -1))
        minutes = -1
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            minutes += 1
            for _ in range(len(queue)):
                row, col = queue.popleft()
            
                for y, x in dirs:
                    r = row + y
                    c = col + x
                    if not (0 <= r < N and 0 <= c < M):
                        continue

                    if grid[r][c] == 1:
                        grid[r][c] = 2
                        fresh_oranges -= 1
                        queue.append((r, c))
                        
        return minutes if fresh_oranges == 0 else -1


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        queue = deque()
        fresh_oranges = 0

        for row in range(N):
            for col in range(M):
                if grid[row][col] == 2:
                    queue.append((row, col))
                if grid[row][col] == 1:
                    fresh_oranges += 1

        queue.append((-1, -1))

        minutes = -1
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            row, col = queue.popleft()

            if row == -1:
                minutes += 1
                if queue:
                    queue.append((-1, -1))
            else:
                for y, x in dirs:
                    r = row + y
                    c = col + x
                    if not (0 <= r < N and 0 <= c < M):
                        continue

                    if grid[r][c] == 1:
                        grid[r][c] = 2
                        fresh_oranges -= 1
                        queue.append((r, c))

        return minutes if fresh_oranges == 0 else -1


## bfs in-place
##############################
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]), 4)
        self.assertEqual(solution.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]), -1)
        self.assertEqual(solution.orangesRotting([[0,2]]), 0)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Breadth-First Search (BFS)
#############################################
# Time: O(N) - Where N is the size of the grid.
# - First, we scan the grid to find the initial values for the queue, which
#   would take O(N) time.
# - Then we run the BFS process on the queue, which in the worst case would
#   enumerate all the cells in the grid once and only once. Therefore, it takes
#   O(N) time.
# - Thus combining the above two steps, the overall time complexity would be
#   O(N) + O(N) = O(N)

# Space: O(N) - Where N is the size of the grid.
# - In the worst case, the grid is filled with rotten oranges. As a result, the
#   queue would be initialized with all the cells in the grid.
# - By the way, normally for BFS, the main space complexity lies in the process
#   rather than the initialization. For instance, for a BFS traversal in a tree,
#   at any given moment, the queue would hold no more than 2 levels of tree
#   nodes. Therefore, the space complexity of BFS traversal in a tree would
#   depend on the width of the input tree.

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()

        # Step 1). build the initial set of rotten oranges
        fresh_oranges = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        # Mark the round / level, _i.e_ the ticker of timestamp
        queue.append((-1, -1))

        # Step 2). start the rotting process via BFS
        minutes_elapsed = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue:
            row, col = queue.popleft()
            if row == -1:
                # We finish one round of processing
                minutes_elapsed += 1
                if queue:  # to avoid the endless loop
                    queue.append((-1, -1))
            else:
                # this is a rotten orange
                # then it would contaminate its neighbors
                for d in directions:
                    neighbor_row, neighbor_col = row + d[0], col + d[1]
                    if ROWS > neighbor_row >= 0 and COLS > neighbor_col >= 0:
                        if grid[neighbor_row][neighbor_col] == 1:
                            # this orange would be contaminated
                            grid[neighbor_row][neighbor_col] = 2
                            fresh_oranges -= 1
                            # this orange would then contaminate other oranges
                            queue.append((neighbor_row, neighbor_col))

        # return elapsed minutes if no fresh orange left
        return minutes_elapsed if fresh_oranges == 0 else -1


## Approach 2: In-place BFS
##############################
# Time: O(N^2) - Where N is the size of the input grid.
# - In the in-place BFS traversal, for each round of BFS, we would have to
#   iterate through the entire grid.
# - The contamination propagates in 4 different directions. If the orange is
#   well adjacent to each other, the chain of propagation would continue until
#   all the oranges turn rotten.
# - In the worst case, the rotten and the fresh oranges might be arranged in a
#   way that we would have to run the BFS loop over and over again, which could
#   amount to N/2 times which is the longest propagation chain that we might
#   have, i.e. the zigzag walk in a 2D grid as shown in the following graph.
# - As a result, the overall time complexity of the in-place BFS algorithm is
#   O(N⋅(N/2)) = O(N^2).

# Space: O(1)
# - the memory usage is constant regardless the size of the input. This is the
#   very point of applying in-place algorithm. Here we trade the time complexity
#   with the space complexity, which is a common scenario in many algorithms.

class Solution(object):
    def orangesRotting(self, grid):
        ROWS, COLS = len(grid), len(grid[0])

        # run the rotting process, by marking the rotten oranges with the timestamp
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        def runRottingProcess(timestamp):
            # flag to indicate if the rotting process should be continued
            to_be_continued = False
            for row in range(ROWS):
                for col in range(COLS):
                    if grid[row][col] == timestamp:
                        # current contaminated cell
                        for d in directions:
                            n_row, n_col = row + d[0], col + d[1]
                            if ROWS > n_row >= 0 and COLS > n_col >= 0:
                                if grid[n_row][n_col] == 1:
                                    # this fresh orange would be contaminated next
                                    grid[n_row][n_col] = timestamp + 1
                                    to_be_continued = True
            return to_be_continued

        timestamp = 2
        while runRottingProcess(timestamp):
            timestamp += 1
        # end of process, to check if there are still fresh oranges left
        for row in grid:
            for cell in row:
                if cell == 1:  # still got a fresh orange left
                    return -1
        # return elapsed minutes if no fresh orange left
        return timestamp - 2


