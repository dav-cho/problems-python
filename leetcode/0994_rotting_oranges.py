##
#### 994. Rotting Oranges (medium)
########################################


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
