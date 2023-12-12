##
#### 797. All Paths From Source to Target (medium)
######################################################


## bfs
##############################
class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
                res = []
        if not graph or len(graph) == 0:
            return res
        
        path = [0]
        queue = deque([path])
        
        while queue:
            curr_path = queue.popleft()
            node = curr_path[-1]
            for neighbor in graph[node]:
                temp_path = curr_path.copy()
                temp_path.append(neighbor)
                
                if neighbor == len(graph) - 1:
                    res.append(temp_path)
                else:
                    queue.append(temp_path)
                    
        return res


class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        res = []
        if not graph or len(graph) == 0:
            return res

        path = [0]
        queue = deque([path])
        
        while queue:
            curr_path = queue.popleft()
            node = curr_path[-1]
            for neighbor in graph[node]:
                temp_path = list(curr_path)
                temp_path.append(neighbor)
                
                if neighbor == len(graph) - 1:
                    res.append(temp_path)
                else:
                    queue.append(temp_path)
                    
        return res


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
