##
#### Shortest Path in Binary Matrix (medium)
################################################

# Given an n x n binary matrix grid, return the length of the shortest clear
# path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell
# (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they
# are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.

# Example 1:
# Input: grid = [[0,1],[1,0]]
# Output: 2

# Example 2:
# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4

# Example 3:
# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1
 
# Constraints:
# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] is 0 or 1

################################################################################

## bfs overwriting input
##############################
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        dirs = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (-1, -1), (1, -1), (-1, 1)
        ]
        
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
        dirs = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (-1, -1), (1, -1), (-1, 1)
        ]
        
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
        dirs = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (-1, -1), (1, -1), (-1, 1)
        ]
        
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
        dirs = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (-1, -1), (1, -1), (-1, 1)
        ]
        
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
        dirs = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (-1, -1), (1, -1), (-1, 1)
        ]
        
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
        dirs = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (-1, -1), (1, -1), (-1, 1)
        ]
        
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
        self.assertEqual(solution.shortestPathBinaryMatrix([[0,1],[1,0]]), 2)
        self.assertEqual(solution.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]), 4)
        self.assertEqual(solution.shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]]), -1)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Breadth-first Search (BFS), Overwriting Input
################################################################
# Time: O(N)
# - Each cell was guaranteed to be enqueued at most once. This is because a
#   condition for a cell to be enqueued was that it had a zero in the grid, and
#   when enqueuing, we also permanently changed the cell's grid value to be
#   non-zero.
# - The outer loop ran as long as there were still cells in the queue,
#   dequeuing one each time. Therefore, it ran at most N times, giving a time
#   complexity of O(N).
# - The inner loop iterated over the unvisited neighbors of the cell that was
#   dequeued by the outer loop. There were at most 88 neighbors. Identifying the
#   unvisited neighbors is an O(1) operation because we treat the 8 as a
#   constant.
# - Therefore, we have a time complexity of O(N).

# Space: O(N)
# - The only additional space we used was the queue. We determined above that
#   at most, we enqueued N cells. Therefore, an upper bound on the worst-case
#   space complexity is O(N).
# - Given that BFS will have nodes of at most two unique distances on the queue
#   at any one time, it would be reasonable to wonder if the worst-case space
#   complexity is actually lower. But actually, it turns out that there are
#   cases with massive grids where the number of cells at a single distance is
#   proportional to N. So even with cells of a single distance on the queue, in
#   the worst case, the space needed is O(N).

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        directions = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        # Helper function to find the neighbors of a given cell.
        def get_neighbours(row, col):
            for row_difference, col_difference in directions:
                new_row = row + row_difference
                new_col = col + col_difference
                if not(0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] != 0:
                    continue
                yield (new_row, new_col)
        
        # Check that the first and last cells are open. 
        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1
        
        # Set up the BFS.
        queue = deque()
        queue.append((0, 0))
        grid[0][0] = 1 
        
        # Carry out the BFS.
        while queue:
            row, col = queue.popleft()
            distance = grid[row][col]
            if (row, col) == (max_row, max_col):
                return distance
            for neighbour_row, neighbour_col in get_neighbours(row, col):
                grid[neighbour_row][neighbour_col] = distance + 1
                queue.append((neighbour_row, neighbour_col))
        
        # There was no path.
        return -1


## Approach 2: Breadth-first Search (Without Overwriting the Input)
#######################################################################
# Time: O(N)
# - Same as approach 1. Processing a cell is O(1), and each of the N cells is
#   processed at most once, giving a total of O(N).

# Space: O(N)
# - Same as approach 1. The visisted set also required O(N) space; in the worst
#   case, it will hold the row and column of each of the N cells.

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        directions = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        # Helper function to find the neighbors of a given cell.
        def get_neighbours(row, col):
            for row_difference, col_difference in directions:
                new_row = row + row_difference
                new_col = col + col_difference
                if not(0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] != 0:
                    continue
                yield (new_row, new_col)
        
        # Check that the first and last cells are open. 
        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1
        
        # Set up the BFS.
        queue = deque([(0, 0, 1)])
        visited = {(0, 0)}
        
        # Do the BFS.
        while queue:
            row, col, distance = queue.popleft()
            if (row, col) == (max_row, max_col):
                return distance
            for neighbour in get_neighbours(row, col):
                if neighbour in visited:
                    continue
                visited.add(neighbour)
                # Note that the * splits neighbour into its values.
                queue.append((*neighbour, distance + 1))
                
        # There was no path.
        return -1


## Starting a new collection for each distance
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        directions = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        # Helper function to find the neighbors of a given cell.
        def get_neighbours(row, col):
            for row_difference, col_difference in directions:
                new_row = row + row_difference
                new_col = col + col_difference
                if not(0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] != 0:
                    continue
                yield (new_row, new_col)
        
        # Check that the first and last cells are open. 
        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1
        
        # Set up the BFS.
        current_layer = [(0, 0)]
        next_layer = []
        visited = {(0, 0)}
        current_distance = 1
        
        while current_layer:
            
            # Process the current layer.
            for row, col in current_layer:
                if (row, col) == (max_row, max_col):
                    return current_distance
                for neighbour in get_neighbours(row, col):
                    if neighbour in visited:
                        continue
                    visited.add(neighbour)
                    next_layer.append(neighbour)
            
            # Set up for processing the next layer.
            current_distance += 1
            current_layer = next_layer
            next_layer = []
                
        # There was no path.
        return -1


## Keeping track of how many cells at each distance are on the queue
class Solution:
    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:  
        
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        directions = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        # Helper function to find the neighbors of a given cell.
        def get_neighbours(row, col):
            for row_difference, col_difference in directions:
                new_row = row + row_difference
                new_col = col + col_difference
                if not(0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] != 0:
                    continue
                yield (new_row, new_col)
        
        # Check that the first and last cells are open. 
        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1
        
        # Set up the BFS.
        queue = deque([(0, 0)])
        visited = {(0, 0)}
        current_distance = 1
        
        # Do the BFS.
        while queue:
            # Process all nodes at current_distance from the top-left cell.
            nodes_of_current_distance = len(queue)
            for _ in range(nodes_of_current_distance):
                row, col = queue.popleft()
                if (row, col) == (max_row, max_col):
                    return current_distance
                for neighbour in get_neighbours(row, col):
                    if neighbour in visited:
                        continue
                    visited.add(neighbour)
                    queue.append(neighbour)
            # We'll now be processing all nodes at current_distance + 1
            current_distance += 1
                    
        # There was no path.
        return -1


## Approach 3: A* (Advanced)
################################
# Time: O(N logN)
# - The difference between this approach and the previous is that adding and
#   removing items from a priority queue is O(logN), as opposed to O(1). Given
#   that we are adding/removing O(N) items, this gives a time complexity of
#   O(N logN).

# Space: O(N)
# - Same as previous approaches.

# Interestingly, there are ways to reduce the time complexity back down to O(N).
# The simplest is to recognize that there will be at most 3 unique estimates on
# the priority queue at any one time, and so to maintain 3 lists instead of a
# priority queue. Adding and removing from lists is O(1), bringing the total
# time complexity back down to O(N).

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        directions = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        # Helper function to find the neighbors of a given cell.
        def get_neighbours(row, col):
            for row_difference, col_difference in directions:
                new_row = row + row_difference
                new_col = col + col_difference
                if not(0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] != 0:
                    continue
                yield (new_row, new_col)
        
        # Helper function for the A* heuristic.
        def best_case_estimate(row, col):
            return max(max_row - row, max_col - col)
            
        # Check that the first and last cells are open. 
        if grid[0][0] or grid[max_row][max_col]:
            return -1
        
        # Set up the A* search.
        visited = set()
        # Entries on the priority queue are of the form
        # (total distance estimate, distance so far, (cell row, cell col))
        priority_queue = [(1 + best_case_estimate(0, 0), 1, (0, 0))]
        while priority_queue:
            estimate, distance, cell = heapq.heappop(priority_queue)
            if cell in visited:
                continue
            if cell == (max_row, max_col):
                return distance
            visited.add(cell)
            for neighbour in get_neighbours(*cell):
                # The check here isn't necessary for correctness, but it
                # leads to a substantial performance gain.
                if neighbour in visited:
                    continue
                estimate = best_case_estimate(*neighbour) + distance + 1
                entry = (estimate, distance + 1, neighbour)
                heapq.heappush(priority_queue, entry)
        
        # There was no path.
        return -1


