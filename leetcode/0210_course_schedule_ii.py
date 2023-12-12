##
#### 210. Course Schedule II (medium)
#########################################


from collections import defaultdict, deque


## indegree
##############################
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj_list = defaultdict(list)
        indegree = {}
        for dst, src in prerequisites:
            adj_list[src].append(dst)
            indegree[dst] = indegree.get(dst, 0) + 1

        res = []
        queue = deque([x for x in range(numCourses) if x not in indegree])
        while queue:
            vertex = queue.popleft()
            res.append(vertex)
            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)

        return res if len(res) == numCourses else []


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj_list = defaultdict(list)
        indegree = defaultdict(int)
        for dst, src in prerequisites:
            adj_list[src].append(dst)
            indegree[dst] += 1

        res = []
        queue = deque([node for node in range(numCourses) if node not in indegree])
        while queue:
            vertex = queue.popleft()
            res.append(vertex)
            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)

        return res if len(res) == numCourses else []


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj_list = defaultdict(list)
        indegree = {}
        for dest, src in prerequisites:
            adj_list[src].append(dest)
            indegree[dest] = indegree.get(dest, 0) + 1

        queue = deque([k for k in range(numCourses) if k not in indegree])
        res = []
        while queue:
            vertex = queue.popleft()
            res.append(vertex)
            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)

        return res if len(res) == numCourses else []


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj_list = defaultdict(list)
        indegree = {}
        for dest, src in prerequisites:
            adj_list[src].append(dest)
            indegree[dest] = indegree.get(dest, 0) + 1

        zero_indegree_queue = deque([k for k in range(numCourses) if k not in indegree])
        topological_sorted_order = []
        while zero_indegree_queue:
            vertex = zero_indegree_queue.popleft()
            topological_sorted_order.append(vertex)
            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        zero_indegree_queue.append(neighbor)

        return (
            topological_sorted_order
            if len(topological_sorted_order) == numCourses
            else []
        )


## dfs
##############################
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        res = []
        is_possible = True
        color = {k: 1 for k in range(numCourses)}
        adj_list = defaultdict(list)
        for dest, src in prerequisites:
            adj_list[src].append(dest)

        def dfs(node):
            nonlocal is_possible
            if not is_possible:
                return

            color[node] = 2

            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == 1:
                        dfs(neighbor)
                    elif color[neighbor] == 2:
                        is_possible = False

            color[node] = 3
            res.append(node)

        for vertex in range(numCourses):
            if color[vertex] == 1:
                dfs(vertex)

        return res[::-1] if is_possible else []


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        WHITE = 1
        GRAY = 2
        BLACK = 3

        topological_sorted_order = []
        is_possible = True
        color = {k: WHITE for k in range(numCourses)}
        adj_list = defaultdict(list)
        for dest, src in prerequisites:
            adj_list[src].append(dest)

        def dfs(node):
            nonlocal is_possible
            if not is_possible:
                return

            color[node] = GRAY

            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == WHITE:
                        dfs(neighbor)
                    elif color[neighbor] == GRAY:
                        is_possible = False

            color[node] = BLACK
            topological_sorted_order.append(node)

        for vertex in range(numCourses):
            if color[vertex] == WHITE:
                dfs(vertex)

        return topological_sorted_order[::-1] if is_possible else []


class Solution:
    WHITE = 1
    GRAY = 2
    BLACK = 3

    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj_list = defaultdict(list)
        for dest, src in prerequisites:
            adj_list[src].append(dest)

        topological_sorted_order = []
        is_possible = True
        color = {k: Solution.WHITE for k in range(numCourses)}

        def dfs(node):
            nonlocal is_possible
            if not is_possible:
                return

            color[node] = Solution.GRAY

            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == Solution.WHITE:
                        dfs(neighbor)
                    elif color[neighbor] == Solution.GRAY:
                        is_possible = False

            color[node] = Solution.BLACK
            topological_sorted_order.append(node)

        for vertex in range(numCourses):
            if color[vertex] == Solution.WHITE:
                dfs(vertex)

        return topological_sorted_order[::-1] if is_possible else []


## kahn's algorithm
##############################
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        res = [0] * numCourses
        if numCourses == 0:
            return res

        if not prerequisites:
            res = [i for i in range(numCourses)]
            return res

        indegree = [0] * numCourses
        zero_degree = deque()
        for pre in prerequisites:
            indegree[pre[0]] += 1
        for i in range(len(indegree)):
            if indegree[i] == 0:
                zero_degree.append(i)
        if not zero_degree:
            return []

        i = 0
        while zero_degree:
            course = zero_degree.popleft()
            res[i] = course
            i += 1
            for pre in prerequisites:
                if pre[1] == course:
                    indegree[pre[0]] -= 1
                    if indegree[pre[0]] == 0:
                        zero_degree.append(pre[0])

        if any(i for i in indegree):
            return []

        return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertCountEqual(Solution().findOrder(2, [[1, 0]]), [0, 1])
        self.assertCountEqual(
            Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]), [0, 2, 1, 3]
        )
        self.assertCountEqual(Solution().findOrder(1, []), [0])


if __name__ == "__main__":
    unittest.main()
