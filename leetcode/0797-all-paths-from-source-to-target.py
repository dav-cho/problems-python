##
#### All Paths From Source to Target (medium)
#################################################

# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find
# all possible paths from node 0 to node n - 1 and return them in any order.

# The graph is given as follows: graph[i] is a list of all nodes you can visit
# from node i (i.e., there is a directed edge from node i to node graph[i][j]).

# Example 1:
# Input: graph = [[1,2],[3],[3],[]]
# Output: [[0,1,3],[0,2,3]]
# Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

# Example 2:
# Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
# Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

# Example 3:
# Input: graph = [[1],[]]
# Output: [[0,1]]

# Example 4:
# Input: graph = [[1,2,3],[2],[3],[]]
# Output: [[0,1,2,3],[0,2,3],[0,3]]

# Example 5:
# Input: graph = [[1,3],[2],[3],[]]
# Output: [[0,1,2,3],[03]]
 
# Constraints:
# n == graph.length
# 2 <= n <= 15
# 0 <= graph[i][j] < n
# graph[i][j] != i (i.e., there will be no self-loops).
# All the elements of graph[i] are unique.
# The input graph is guaranteed to be a DAG.

################################################################################

## dfs
##############################
class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        def dfs(curr_node, path):
            path.append(curr_node)
            if curr_node == len(graph) - 1:
                res.append(list(path))
                
            for neighbor in graph[curr_node]:
                backtrack(neighbor, path)
                path.pop()
                
        res = []
        backtrack(0, [])
        
        return res


## backtracking
##############################
class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        def backtrack(curr_node, path):
            if curr_node == len(graph) - 1:
                res.append(list(path))
                
            for neighbor in graph[curr_node]:
                path.append(neighbor)
                backtrack(neighbor, path)
                path.pop()
                
        res = []
        backtrack(0, [0])
        
        return res


class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        def backtrack(curr_node, path):
            if curr_node == target:
                res.append(list(path))
                
            for neighbor in graph[curr_node]:
                path.append(neighbor)
                backtrack(neighbor, path)
                path.pop()
                
        target = len(graph) - 1
        res = []
        backtrack(0, [0])
        
        return res


class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        def backtrack(curr_node, path):
            if curr_node == target:
                res.append(list(path))
                return
            
            for neighbor in graph[curr_node]:
                path.append(neighbor)
                backtrack(neighbor, path)
                path.pop()
            
        target = len(graph) - 1
        res = []
        path = [0]
        backtrack(0, path)
        
        return res


from collections import deque

class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        target = len(graph) - 1
        res = []
        
        def backtrack(curr_node, path):
            if curr_node == target:
                res.append(list(path))
                return
            
            for neighbor in graph[curr_node]:
                path.append(neighbor)
                backtrack(neighbor, path)
                path.pop()
            
        path = deque([0])
        backtrack(0, path)
        
        return res


class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        target = len(graph) - 1
        res = []

        def backtrack(curr_node, path):
            if curr_node == target:
                res.append(list(path))
                return

            for neighbor in graph[curr_node]:
                path.append(neighbor)
                backtrack(neighbor, path)
                path.pop()

        path = [0]
        backtrack(0, path)

        return res


## top-down dynamic programming
###################################
from functools import lru_cache

class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        target = len(graph) - 1
        
        @lru_cache(maxsize=None)
        def all_paths_to_target(curr_node):
            if curr_node == target:
                return [[target]]
            
            res = []
            for next_node in graph[curr_node]:
                for path in all_paths_to_target(next_node):
                    res.append([curr_node] + path)
                    
            return res
        
        return all_paths_to_target(0)


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.allPathsSourceTarget([[1,2],[3],[3],[]]), [[0,1,3],[0,2,3]])
        self.assertEqual(solution.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]), [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]])
        self.assertEqual(solution.allPathsSourceTarget([[1],[]]), [[0,1]])
        self.assertEqual(solution.allPathsSourceTarget([[1,2,3],[2],[3],[]]), [[0,1,2,3],[0,2,3],[0,3]])
        self.assertEqual(solution.allPathsSourceTarget([[1,3],[2],[3],[]]), [[0,1,2,3],[0,3]])


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Backtracking
###############################
# Time: O(2^N * N)
# - As we calculate shortly before, there could be at most 2^(N−1) − 1 possible
#   paths in the graph.
# - For each path, there could be at most N−2 intermediate nodes, i.e. it takes
#   O(N) time to build a path.
# - To sum up, a loose upper-bound on the time complexity of the algorithm would
#   be (2^(N−1)−1)⋅O(N)=O(2^N⋅N), where we consider it takes O(N) efforts to
#   build each path.
# - It is a loose uppper bound, since we could have overlapping among the paths,
#   therefore the efforts to build certain paths could benefit others.

# Space: O(2^N * N)
# - Similarly, since at most we could have 2^(N-1)-1 paths as the results and
#   each path can contain up to N nodes, the space we need to store the results
#   would be O(2^N ⋅N).
# - Since we also applied recursion in the algorithm, the recursion could incur
#   additional memory consumption in the function call stack. The stack can grow
#   up to N consecutive calls. Meanwhile, along with the recursive call, we also
#   keep the state of the current path, which could take another O(N) space.
#   Therefore, in total, the recursion would require additional O(N) space.
# - To sum up, the space complexity of the algorithm is
#   O(2 N ⋅N)+O(N)=O(2 N ⋅N).

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        target = len(graph) - 1
        results = []

        def backtrack(currNode, path):
            # if we reach the target, no need to explore further.
            if currNode == target:
                results.append(list(path))
                return
            # explore the neighbor nodes one after another.
            for nextNode in graph[currNode]:
                path.append(nextNode)
                backtrack(nextNode, path)
                path.pop()
        # kick of the backtracking, starting from the source node (0).
        path = deque([0])
        backtrack(0, path)

        return results


## Approach 2: Top-Down Dynamic Programming
###############################################
# Time: O(2 N ⋅N).
# - To estimate the overall time complexity, let us start from the last step
#   when we prepend the starting node to each of the paths returned from the
#   target function. Since we have to copy each path in order to create new
#   paths, it would take up to NN steps for each final path. Therefore, for this
#   last step, it could take us O(2 N−1 ⋅N) time.
# - Right before the last step, when the maximal length of the path is N−1, we
#   should have 2^N−2 number of paths at this moment.
# - Deducing from the above two steps, again a loose upper-bound of the time
#   complexity would be O(∑(N / i=1) 2^(i−1) ⋅i)=O(2^N ⋅N)
# - The two approach might have the same asymptotic time complexity. However, in
#   practice the DP approach is slower than the backtracking approach, since we
#   copy the intermediate paths over and over.
# - Note that, the performance would be degraded further, if we did not adopt
#   the memoization technique here.

# Space: O(2 N ⋅N)
# - Similarly, since at most we could have 2^(N−1) −1 paths as the results and
#   each path can contain up to N nodes, the space we need to store the results
#   would be O(2^N ⋅N).
# - Since we also applied recursion in the algorithm, it could incur additional
#   memory consumption in the function call stack. The stack can grow up to N
#   consecutive calls. Therefore, the recursion would require additional O(N)
#   space.
# - To sum up, the space complexity of the algorithm is
#   O(2^N ⋅N)+O(N)=O(2^N ⋅N).

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        target = len(graph) - 1

        # apply the memoization
        @lru_cache(maxsize=None)
        def allPathsToTarget(currNode):
            if currNode == target:
                return [[target]]

            results = []
            for nextNode in graph[currNode]:
                for path in allPathsToTarget(nextNode):
                    results.append([currNode] + path)

            return results

        return allPathsToTarget(0)


