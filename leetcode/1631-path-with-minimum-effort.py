##
#### Path With Minimum Effort (medium)
##########################################

# You are a hiker preparing for an upcoming hike. You are given heights, a 2D
# array of size rows x columns, where heights[row][col] represents the height of
# cell (row, col). You are situated in the top-left cell, (0, 0), and you hope
# to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You
# can move up, down, left, or right, and you wish to find a route that requires
# the minimum effort.

# A route's effort is the maximum absolute difference in heights between two
# consecutive cells of the route.

# Return the minimum effort required to travel from the top-left cell to the
# bottom-right cell.

# Example 1:
# Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
# Output: 2
# Explanation:
# - The route of [1,3,5,3,5] has a maximum absolute difference of 2
#   in consecutive cells.
# - This is better than the route of [1,2,2,2,5], where the maximum absolute
#   difference is 3.

# Example 2:
# Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
# Output: 1
# Explanation:
# - The route of [1,2,3,4,5] has a maximum absolute difference of 1 in
#   consecutive cells, which is better than route [1,3,5,3,5].

# Example 3:
# Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
# Output: 0
# Explanation: This route does not require any effort.
 
# Constraints:
# rows == heights.length
# columns == heights[i].length
# 1 <= rows, columns <= 100
# 1 <= heights[i][j] <= 106

################################################################################

import heapq


## dijkstra's algorithm
##############################
class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        seen = [[None] * cols for _ in range(rows)]
        diffs = [[float('inf')] * cols for _ in range(rows)]
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
        diffs = [[float('inf')] * cols for _ in range(rows)]
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
        diff_matrix = [[float('inf')] * cols for _ in range(rows)]
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
        right = 10 ** 6
        
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
        right = 10 ** 6
        
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
        right = 10 ** 6
        
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
        right = 10 ** 6
        
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
        self.max_so_far = float('inf')
        
        def dfs(x, y, max_difference):
            if x == M - 1 and y == N - 1:
                self.max_so_far = min(self.max_so_far, max_difference)
                
                return max_difference
            
            curr_height = heights[x][y]
            heights[x][y] = 0
            min_effort = float('inf')
            
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                adjacent_x = x + dx
                adjacent_y = y + dy
                
                if 0 <= adjacent_x < M and 0 <= adjacent_y < N and heights[adjacent_x][adjacent_y] != 0:
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
        self.assertEqual(solution.minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]), 2)
        #self.assertEqual(solution.minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]]), 1)
        #self.assertEqual(solution.minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]), 0)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Brute Force using Backtracking
#################################################
# Time: O(3^m⋅n) - Let m be the number of rows and n be the number of columns
#                  in the matrix heights.
# - The total number of cells in the matrix is given by m⋅n. For the
#   backtracking, there are at most 4 possible directions to explore, but
#   further, the choices are reduced to 3 (since we won't go back to where we
#   come from). Thus, considering 3 possibilities for every cell in the matrix
#   the time complexity would be O(3^m⋅n).
# - The time complexity is exponential, hence this approach is exhaustive and
#   results in Time Limit Exceeded (TLE).

# Space: O(m⋅n)
# - This space will be used to store the recursion stack. As we recursively move
#   to the adjacent cells, in the worst case there could be m⋅n cells in the
#   recursive call stack.

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])
        self.max_so_far = math.inf

        def dfs(x, y, max_difference):
            if x == row-1 and y == col-1:
                self.max_so_far = min(self.max_so_far, max_difference)
                return max_difference
            current_height = heights[x][y]
            heights[x][y] = 0
            min_effort = math.inf
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                adjacent_x = x + dx
                adjacent_y = y + dy
                if 0 <= adjacent_x < row and 0 <= adjacent_y < col and heights[
                        adjacent_x][adjacent_y] != 0:
                    current_difference = abs(
                        heights[adjacent_x][adjacent_y]-current_height)
                    max_current_difference = max(
                        max_difference, current_difference)
                    if max_current_difference < self.max_so_far:
                        result = dfs(adjacent_x, adjacent_y,
                                     max_current_difference)
                        min_effort = min(min_effort, result)
            heights[x][y] = current_height
            return min_effort

        return dfs(0, 0, 0)


## Approach 2: Variations of Dijkstra's Algorithm
#####################################################
# Time: O(m⋅nlog(m⋅n)) - Where m is the number of rows and n is the number of
#                        columns in matrix heights.
# - It will take O(m⋅n) time to visit every cell in the matrix. The priority
#   queue will contain at most m⋅n cells, so it will take O(log(m⋅n)) time to
#   re-sort the queue after every adjacent cell is added to the queue. This
#   given as total time complexiy as O(m⋅nlog(m⋅n)).

# Space: O(m⋅n) - Where m is the number of rows and n is the number of columns
#                 in matrix heights.
# - The maximum queue size is equal to the total number of cells in the matrix
#   height which is given by m⋅n. Also, we use a difference matrix of size m⋅n.
#   This gives as time complexity as O(m⋅n+m⋅n) = O(m⋅n)

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])
        difference_matrix = [[math.inf]*col for _ in range(row)]
        difference_matrix[0][0] = 0
        visited = [[False]*col for _ in range(row)]
        queue = [(0, 0, 0)]  # difference, x, y
        while queue:
            difference, x, y = heapq.heappop(queue)
            visited[x][y] = True
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                adjacent_x = x + dx
                adjacent_y = y + dy
                if 0 <= adjacent_x < row and 0 <= adjacent_y < col and not visited[
                        adjacent_x][adjacent_y]:
                    current_difference = abs(
                        heights[adjacent_x][adjacent_y]-heights[x][y])
                    max_difference = max(
                        current_difference, difference_matrix[x][y])
                    if difference_matrix[adjacent_x][adjacent_y] > max_difference:
                        difference_matrix[adjacent_x][adjacent_y] = max_difference
                        heapq.heappush(
                            queue, (max_difference, adjacent_x, adjacent_y))
        return difference_matrix[-1][-1]


## Approach 3: Union Find - Disjoint Set
############################################
# Time: O(m⋅n(log(m⋅n))) - Let m be the number of rows and n be the number of
#                          columns of the matrix height.
# - We iterate each edge in the matrix. From the above example, it is evident
#   that for a matrix of size 3⋅3, the total number of edges are 12. Thus, for
#   a m⋅n matrix, the total number of edges could be given by
#   (m⋅n⋅2)−(m+n) (3*3*2) - (3+3)), which is roughly equivalent to m⋅n.
# - For every edge, we find the parent of each cell and perform the union
#   (Union Find). For n elements, the time complexity of Union Find is logn.
#   (Refer Proof Of Time Complexity Of Union Find). Thus for m⋅n cells, the time
#   taken to perform Union Find would be logm⋅n. This gives us total time
#   complexity as, O(m⋅n(log(m⋅n))).

# Space: O(m⋅n)
# - We use arrays edgeList, parent, and rank of size m⋅n.

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        class UnionFind:
            def __init__(self, size):
                self.parent = [x for x in range(size)]
                self.rank = [0]*(size)

            def find(self, i):
                if self.parent[i] != i:
                    self.parent[i] = self.find(self.parent[i])
                return self.parent[i]

            def union(self, x, y):
                parent_x = self.find(x)
                parent_y = self.find(y)
                if parent_x != parent_y:
                    if self.rank[parent_x] > self.rank[parent_y]:
                        self.parent[parent_y] = parent_x
                    elif self.rank[parent_x] < self.rank[parent_y]:
                        self.parent[parent_x] = parent_y
                    else:
                        self.parent[parent_y] = parent_x
                        self.rank[parent_x] += 1

        row = len(heights)
        col = len(heights[0])
        if row == 1 and col == 1:
            return 0

        edge_list = []
        for current_row in range(row):
            for current_col in range(col):
                if current_row > 0:
                    difference = abs(
                        heights[current_row][current_col] -
                        heights[current_row - 1][current_col])
                    edge_list.append(
                        (difference, current_row * col + current_col,
                         (current_row - 1) * col + current_col))
                if current_col > 0:
                    difference = abs(
                        heights[current_row][current_col] -
                        heights[current_row][current_col - 1])
                    edge_list.append(
                        (difference, current_row * col + current_col, current_row
                         * col + current_col - 1))
        edge_list.sort()
        union_find = UnionFind(row*col)

        for difference, x, y in edge_list:
            union_find.union(x, y)
            if union_find.find(0) == union_find.find(row*col-1):
                return difference
        return -1


## Approach 4: Binary Search Using BFS
##########################################
# Time: O(m⋅n) - Let m be the number of rows and n be the number of columns for the matrix \text{height}height.
# - We do a binary search to calculate the mid values and then do Breadth First
#   Search on the matrix for each of those values.
# - Binary Search:To perform Binary search on numbers in range (0..10^6), the
#   time taken would be O(log10^6).
# - Breath First Search: The time complexity for the Breadth First Search for
#   vertices V and edges E is O(V+E) (See our Explore Card on BFS) Thus, in the
#   matrix of size m⋅n, with m⋅n vertices and m⋅n edges (Refer time complexity
#   of Approach 3), the time complexity to perform Breath First Search would be
#   O(m⋅n+m⋅n) = O(m⋅n).
# - This gives us total time complexity as O(log10^6 ⋅(m⋅n)) which is equivalent
#   to O(m⋅n).

# Space Complexity: O(m⋅n)
# - As we use a queue and visited array of size m⋅n.

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])

        def canReachDestinaton(mid):
            visited = [[False]*col for _ in range(row)]
            queue = [(0, 0)]  # x, y
            while queue:
                x, y = queue.pop(0)
                if x == row-1 and y == col-1:
                    return True
                visited[x][y] = True
                for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    adjacent_x = x + dx
                    adjacent_y = y + dy
                    if 0 <= adjacent_x < row and 0 <= adjacent_y < col and not visited[adjacent_x][adjacent_y]:
                        current_difference = abs(
                            heights[adjacent_x][adjacent_y]-heights[x][y])
                        if current_difference <= mid:
                            visited[adjacent_x][adjacent_y] = True
                            queue.append((adjacent_x, adjacent_y))

        left = 0
        right = 10000000
        while left < right:
            mid = (left + right)//2
            if canReachDestinaton(mid):
                right = mid
            else:
                left = mid + 1
        return left


## Approach 5: Binary Search Using DFS
##########################################
# Time: O(m⋅n) - As in Approach 4. The only difference is that we are using
#                Depth First Search instead of Breadth First Search and have
#                similar time complexity.
# Space: O(m⋅n) - As in Approach 4. In Depth First Search, we use the internal
#                 call stack (instead of the queue in Breadth First Search).

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])

        def canReachDestinaton(x, y, mid):
            if x == row-1 and y == col-1:
                return True
            visited[x][y] = True
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                adjacent_x = x + dx
                adjacent_y = y + dy
                if 0 <= adjacent_x < row and 0 <= adjacent_y < col and not visited[
                        adjacent_x][adjacent_y]:
                    current_difference = abs(
                        heights[adjacent_x][adjacent_y]-heights[x][y])
                    if current_difference <= mid:
                        visited[adjacent_x][adjacent_y] = True
                        if canReachDestinaton(adjacent_x, adjacent_y, mid):
                            return True
        left = 0
        right = 10000000
        while left < right:
            mid = (left + right)//2
            visited = [[False]*col for _ in range(row)]
            if canReachDestinaton(0, 0, mid):
                right = mid
            else:
                left = mid + 1
        return left


