##
#### 1136. Parallel Courses (medium)
########################################


## bfs (kahn's algorithm)
##############################
from __future__ import print_function
from tracemalloc import start


class Solution:
    def minimumSemesters(self, n: int, relations: list[list[int]]) -> int:
        graph = {node: [] for node in range(1, n + 1)}
        indegree = {node: 0 for node in range(1, n + 1)}
        for start, end in relations:
            graph[start].append(end)
            indegree[end] += 1

        queue = [node for node in graph if indegree[node] == 0]
        step = 0
        studied = 0
        while queue:
            step += 1
            next_queue = []
            for node in queue:
                studied += 1
                neighbors = graph[node]
                for neighbor in neighbors:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        next_queue.append(neighbor)
            queue = next_queue

        return step if studied == n else -1


class Solution:
    def minimumSemesters(self, n: int, relations: list[list[int]]) -> int:
        graph = {node: [] for node in range(1, n + 1)}
        indegree = {node: 0 for node in range(1, n + 1)}
        for start_node, end_node in relations:
            graph[start_node].append(end_node)
            indegree[end_node] += 1

        queue = [node for node in graph if indegree[node] == 0]
        step = 0
        studied_count = 0
        while queue:
            step += 1
            next_queue = []
            for node in queue:
                studied_count += 1
                end_nodes = graph[node]
                for end_node in end_nodes:
                    indegree[end_node] -= 1
                    if indegree[end_node] == 0:
                        next_queue.append(end_node)
            queue = next_queue

        return step if studied_count == n else -1


## dfs (check cycle / longest path combined)
################################################
class Solution:
    def minimumSemesters(self, n: int, relations: list[list[int]]) -> int:
        graph = {node: [] for node in range(1, n + 1)}
        for start, end in relations:
            graph[start].append(end)

        seen = {}

        def dfs(node):
            if node in seen:
                return seen[node]
            else:
                seen[node] = -1

            max_length = 1
            for neighbor in graph[node]:
                length = dfs(neighbor)
                if length == -1:
                    return -1
                else:
                    max_length = max(max_length, length + 1)

            seen[node] = max_length
            return max_length

        max_length = -1
        for node in graph.keys():
            length = dfs(node)
            if length == -1:
                return -1
            else:
                max_length = max(max_length, length)

        return max_length


class Solution:
    def minimumSemesters(self, n: int, relations: list[list[int]]) -> int:
        graph = {node: [] for node in range(1, n + 1)}
        for start_node, end_node in relations:
            graph[start_node].append(end_node)

        seen = {}

        def dfs(node):
            if node in seen:
                return seen[node]
            else:
                seen[node] = -1

            max_length = 1
            for end_node in graph[node]:
                length = dfs(end_node)
                if length == -1:
                    return -1
                else:
                    max_length = max(max_length, length + 1)

            seen[node] = max_length
            return max_length

        max_length = -1
        for node in graph.keys():
            length = dfs(node)
            if length == -1:
                return -1
            else:
                max_length = max(max_length, length)

        return max_length


## dfs (check for cycles - find longest path)
#################################################
class Solution:
    def minimumSemesters(self, n: int, relations: list[list[int]]) -> int:
        graph = {node: [] for node in range(1, n + 1)}
        for start, end in relations:
            graph[start].append(end)

        seen = {}

        def dfs_check_cycle(node):
            if node in seen:
                return seen[node]
            else:
                seen[node] = -1

            for end_node in graph[node]:
                if dfs_check_cycle(end_node):
                    return True

            seen[node] = False
            return False

        for node in graph.keys():
            if dfs_check_cycle(node):
                return -1

        seen_path = {}

        def dfs_max_path(node):
            if node in seen_path:
                return seen_path[node]

            max_length = 1
            for end in graph[node]:
                length = dfs_max_path(end)
                max_length = max(max_length, length + 1)

            seen_path[node] = max_length
            return max_length

        return max(dfs_max_path(node) for node in graph.keys())


class Solution:
    def minimumSemesters(self, n: int, relations: list[list[int]]) -> int:
        graph = {node: [] for node in range(1, n + 1)}
        for start_node, end_node in relations:
            graph[start_node].append(end_node)

        seen = {}

        def dfs_check_cycle(node):
            if node in seen:
                return seen[node]
            else:
                seen[node] = -1

            for end_node in graph[node]:
                if dfs_check_cycle(end_node):
                    return True

            seen[node] = False
            return False

        for node in graph.keys():
            if dfs_check_cycle(node):
                return -1

        seen_max_path = {}

        def dfs_max_path(node):
            if node in seen_max_path:
                return seen_max_path[node]

            max_length = 1
            for end_node in graph[node]:
                length = dfs_max_path(end_node)
                max_length = max(max_length, length + 1)

            seen_max_path[node] = max_length
            return max_length

        return max(dfs_max_path(node) for node in graph.keys())


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().minimumSemesters(3, [[1, 3], [2, 3]]), 2)
        self.assertEqual(Solution().minimumSemesters(3, [[1, 2], [2, 3], [3, 1]]), -1)


if __name__ == "__main__":
    unittest.main()
