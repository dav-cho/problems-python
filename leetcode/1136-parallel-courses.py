##
#### Parallel Courses (medium)
########################################

# You are given an integer n, which indicates that there are n courses labeled
# from 1 to n. You are also given an array relations where
# relations[i] = [prevCoursei, nextCoursei], representing a prerequisite
# relationship between course prevCoursei and course nextCoursei: course
# prevCoursei has to be taken before course nextCoursei.

# In one semester, you can take any number of courses as long as you have taken
# all the prerequisites in the previous semester for the courses you are taking.

# Return the minimum number of semesters needed to take all courses. If there
# is no way to take all the courses, return -1.

# Example 1:
# Input: n = 3, relations = [[1,3],[2,3]]
# Output: 2
# Explanation: The figure above represents the given graph.
# In the first semester, you can take courses 1 and 2.
# In the second semester, you can take course 3.

# Example 2:
# Input: n = 3, relations = [[1,2],[2,3],[3,1]]
# Output: -1
# Explanation: No course can be studied because they are prerequisites of each other.

# Constraints:
# 1 <= n <= 5000
# 1 <= relations.length <= 5000
# relations[i].length == 2
# 1 <= prevCoursei, nextCoursei <= n
# prevCoursei != nextCoursei
# All the pairs [prevCoursei, nextCoursei] are unique.

################################################################################


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


## LeetCode Solutions
#########################

## Approach 1: Breadth-First Search (Kahn's Algorithm)
##########################################################
# Let E be the length of relations. N is the number of courses, as explained in
# the problem description.

# Time: O(N+E) - For building the graph, we spend O(N) to initialize the graph,
#                and spend O(E) to add edges since we iterate relations once.
#                For BFS, we spend O(N+E) since we need to visit every node and
#                edge once in BFS in the worst case.
# Space: O(N+E) - For the graph, we spend O(N+E) since we have O(N) keys and
#                 O(E) values. For BFS, we spend O(N) since in the worst case,
#                 we need to add all nodes to the queue in the same time.
class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        graph = {i: [] for i in range(1, N + 1)}
        in_count = {i: 0 for i in range(1, N + 1)}  # or in-degree
        for start_node, end_node in relations:
            graph[start_node].append(end_node)
            in_count[end_node] += 1

        queue = []
        # we use list here since we are not
        # poping from front the this code
        for node in graph:
            if in_count[node] == 0:
                queue.append(node)

        step = 0
        studied_count = 0
        # start learning with BFS
        while queue:
            # start new semester
            step += 1
            next_queue = []
            for node in queue:
                studied_count += 1
                end_nodes = graph[node]
                for end_node in end_nodes:
                    in_count[end_node] -= 1
                    # if all prerequisite courses learned
                    if in_count[end_node] == 0:
                        next_queue.append(end_node)
            queue = next_queue

        return step if studied_count == N else -1


## Approach 2: Depth-First Search: Check for Cycles + Find Longest Path
###########################################################################
# Let E be the length of relations.

# Time: O(N+E) - For building the graph, we spend O(N) to initialize the graph,
#                and spend O(E) to add edges since we iterate relations once.
#                For DFS, we spend O(N+E) since we need to visit every node and
#                edge once in DFS in the worst case.
# Space: O(N+E) - For the graph, we spend O(N+E) since we have O(N) keys and
#                 O(E) values. For DFS, we spend O(N) since in the worst case,
#                 we need to add all nodes to the stack to recursively call DFS.
#                 Also, we run DFS twice.
class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        graph = {i: [] for i in range(1, N + 1)}
        for start_node, end_node in relations:
            graph[start_node].append(end_node)

        # check if the graph contains a cycle
        visited = {}

        def dfs_check_cycle(node: int) -> bool:
            # return True if graph has a cycle
            if node in visited:
                return visited[node]
            else:
                # mark as visiting
                visited[node] = -1
            for end_node in graph[node]:
                if dfs_check_cycle(end_node):
                    # we meet a cycle!
                    return True
            # mark as visited
            visited[node] = False
            return False

        # if has cycle, return -1
        for node in graph.keys():
            if dfs_check_cycle(node):
                return -1

        # if no cycle, return the longest path
        visited_length = {}

        def dfs_max_path(node: int) -> int:
            # return the longest path (inclusive)
            if node in visited_length:
                return visited_length[node]
            max_length = 1
            for end_node in graph[node]:
                length = dfs_max_path(end_node)
                max_length = max(length + 1, max_length)
            # store it
            visited_length[node] = max_length
            return max_length

        return max(dfs_max_path(node) for node in graph.keys())


## Approach 3: Depth-First Search: Combine
##############################################
# Let E be the length of relations.

# Time: O(N+E) - For building the graph, we spend O(N) to initialize the graph,
#                and spend O(E) to add egdes since we iterate relations once.
#                For DFS, we spend O(N+E) since we need to visit every node and
#                edge once in DFS in the worst case.
# Space: O(N+E) - For the graph, we spend O(N+E) since we have O(N) keys and
#                 O(E) values. For DFS, we spend O(N) since in the worst case,
#                 we need to add all nodes to the stack to recursively call DFS.
class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        graph = {i: [] for i in range(1, N + 1)}
        for start_node, end_node in relations:
            graph[start_node].append(end_node)

        visited = {}

        def dfs(node: int) -> int:
            # return the longest path (inclusive)
            if node in visited:
                return visited[node]
            else:
                # mark as visiting
                visited[node] = -1

            max_length = 1
            for end_node in graph[node]:
                length = dfs(end_node)
                # we meet a cycle!
                if length == -1:
                    return -1
                else:
                    max_length = max(length + 1, max_length)
            # mark as visited
            visited[node] = max_length
            return max_length

        max_length = -1
        for node in graph.keys():
            length = dfs(node)
            # we meet a cycle!
            if length == -1:
                return -1
            else:
                max_length = max(length, max_length)
        return max_length
