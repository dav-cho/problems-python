##
#### 1971. Find if Path Exists in Graph (easy)
##################################################


## best - bfs
##############################
class Solution:
    def validPath(
        self, n: int, edges: list[list[int]], source: int, destination: int
    ) -> bool:
        pass
        # adj_list = [[] for _ in range(n)]
        # for x, y in edges:
        #    adj_list[x].append(y)
        #    adj_list[y].append(x)
        #
        # seen = {start}
        # queue = deque([start])
        #
        # while queue:
        #    node = queue.popleft()
        #    if node == end:
        #        return True
        #
        #    for neighbor in adj_list[node]:
        #        if neighbor not in seen:
        #            queue.append(neighbor)
        #            seen.add(neighbor)
        #
        # return False


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
    def validPath(
        self, n: int, edges: list[list[int]], source: int, destination: int
    ) -> bool:
        adj_list = [[] for _ in range(n)]
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        seen = {source}
        stack = [source]
        while stack:
            node = stack.pop()
            if node == destination:
                return True

            for neighbor in adj_list[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)

        return False


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
    def validPath(
        self, n: int, edges: list[list[int]], source: int, destination: int
    ) -> bool:
        adj_list = [[] for _ in range(n)]
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        seen = {source}
        queue = deque([source])
        while queue:
            node = queue.popleft()
            if node == destination:
                return True

            for neighbor in adj_list[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)

        return False


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
    def validPath(
        self, n: int, edges: list[list[int]], source: int, destination: int
    ) -> bool:
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

        return find(source) == find(destination)


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
        self.assertEqual(solution.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2), True)
        self.assertEqual(
            solution.validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5), False
        )


if __name__ == "__main__":
    unittest.main()
