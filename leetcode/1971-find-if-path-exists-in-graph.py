##
#### Find if Path Exists in Graph (easy)
############################################

# There is a bi-directional graph with n vertices, where each vertex is labeled
# from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D
# integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional
# edge between vertex ui and vertex vi. Every vertex pair is connected by at
# most one edge, and no vertex has an edge to itself.

# You want to determine if there is a valid path that exists from vertex start
# to vertex end.

# Given edges and the integers n, start, and end, return true if there is a
# valid path from start to end, or false otherwise.

# Example 1:
# Input: n = 3, edges = [[0,1],[1,2],[2,0]], start = 0, end = 2
# Output: true
# Explanation: There are two paths from vertex 0 to vertex 2:
# - 0 → 1 → 2
# - 0 → 2

# Example 2:
# nput: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], start = 0, end = 5
# Output: false
# Explanation: There is no path from vertex 0 to vertex 5.
 
# Constraints:
# 1 <= n <= 2 * 105
# 0 <= edges.length <= 2 * 105
# edges[i].length == 2
# 0 <= ui, vi <= n - 1
# ui != vi
# 0 <= start, end <= n - 1
# There are no duplicate edges.
# There are no self edges.

################################################################################

## best - bfs
##############################
class Solution:
    def validPath(self, n: int, edges: list[list[int]], start: int, end: int) -> bool:
        adj_list = [[] for _ in range(n)]
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)
            
        seen = {start}
        queue = deque([start])
        
        while queue:
            node = queue.popleft()
            if node == end:
                return True
            
            for neighbor in adj_list[node]:
                if neighbor not in seen:
                    queue.append(neighbor)
                    seen.add(neighbor)
                
        return False


## dfs
##############################
class Solution:
    def validPath(self, n: int, edges: list[list[int]], start: int, end: int) -> bool:
        adj_list = [[] for _ in range(n)]
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        seen = {start}
        stack = [start]
        while stack:
            node = stack.pop()
            if node == end:
                return True

            for neighbor in adj_list[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)

        return False


## bfs
##############################
from collections import deque

class Solution:
    def validPath(self, n: int, edges: list[list[int]], start: int, end: int) -> bool:
        adj_list = [[] for _ in range(n)]
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        seen = {start}
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if node == end:
                return True

            for neighbor in adj_list[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)

        return False


## union find (disjoint set)
##############################
class Solution:
    def validPath(self, n: int, edges: list[list[int]], start: int, end: int) -> bool:
        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]
        
        def union(edge):
            root_x, root_y = map(find, edge)
            if root_x == root_y:
                return
                
            if rank[root_x] < rank[root_y]:
                root[root_x] = root_y
            else:
                root[root_y] = root_x
                if rank[root_x] == rank[root_y]:
                    rank[root_x] += 1
                    
        root = list(range(n))
        rank = [1] * n
        for edge in edges:
            union(edge)
        
        return find(start) == find(end)


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.validPath(3, [[0,1],[1,2],[2,0]], 0, 2), True)
        self.assertEqual(solution.validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5), False)


if __name__ == "__main__":
    unittest.main()


