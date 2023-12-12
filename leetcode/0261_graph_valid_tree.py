##
#### 261. Graph Valid Tree (medium)
#######################################


## advanced dfs iterative
##############################
class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj_list = [[] for _ in range(n)]
        for x, y in edges:
            adj_list[x] = y
            adj_list[y] = x

        seen = {0}
        stack = [0]
        while stack:
            node = stack.pop()
            for neighbor in adj_list[node]:
                if neighbor in seen:
                    continue
                seen.add(neighbor)
                stack.apend(neighbor)

        return len(seen) == n


## advanced bfs iterative (fastest)
#######################################
import collections


class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj_list = [[] for _ in range(n)]
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        seen = {0}
        queue = collections.deque([0])
        while queue:
            node = queue.popleft()
            for neighbor in adj_list[node]:
                if neighbor in seen:
                    continue
                seen.add(neighbor)
                queue.append(neighbor)

        return len(seen) == n


## advanced dfs recursive
##############################
class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj_list = [[] for _ in range(n)]
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        seen = set()

        def dfs(node):
            if node in seen:
                return
            seen.add(node)

            for neighbor in adj_list[node]:
                dfs(neighbor)

        dfs(0)
        return len(seen) == n


## union find (disjoint set) - optimized (2nd fastest)
##########################################################
class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        uf = UnionFind(n)
        for x, y in edges:
            if not uf.union(x, y):
                return False

        return True


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x

        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False

        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = root_y
        else:
            self.root[root_y] = root_x
            self.rank[root_x] += 1

        return True


class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        uf = UnionFind(n)
        for x, y in edges:
            if not uf.union(x, y):
                return False

        return True


class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.size = [1] * size

    def find(self, x):
        root = x
        while root != self.parent[root]:
            root = self.parent[root]

        while x != root:
            old_root = self.parent[x]
            self.parent[x] = root
            x = old_root
        return root

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False

        if self.size[root_x] < self.size[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]

        return True


## union find (disjoint set) - naive
########################################
class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        uf = UnionFind(n)
        for x, y in edges:
            if not uf.union(x, y):
                return False

        return True


class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]

    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False

        self.parent[root_y] = root_x
        return True


## dfs iterative
##############################
class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj_list = [[] for _ in range(n)]
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        parents = {0: -1}
        stack = [0]
        while stack:
            node = stack.pop()
            for neighbor in adj_list[node]:
                if neighbor == parents[node]:
                    continue
                if neighbor in parents:
                    return False
                parents[neighbor] = node
                stack.append(neighbor)

        return len(parents) == n


## dfs recursive
##############################
class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adjacency_list = [[] for _ in range(n)]
        for x, y in edges:
            adjacency_list[x].append(y)
            adjacency_list[y].append(x)

        seen = set()

        def dfs(node, parent):
            if node in seen:
                return

            seen.add(node)
            for neighbor in adjacency_list[node]:
                if neighbor == parent:
                    continue
                if neighbor in seen:
                    return False
                result = dfs(neighbor, node)
                if not result:
                    return False

            return True

        return dfs(0, -1) and len(seen) == n


## bfs iterative
##############################
import collections


class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj_list = [[] for _ in range(n)]
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        parents = {0: -1}
        queue = collections.deque([0])
        while queue:
            node = queue.popleft()
            for neighbor in adj_list[node]:
                if neighbor == parents[node]:
                    continue
                if neighbor in parents:
                    return False
                parents[neighbor] = node
                queue.append(neighbor)

        return len(parents) == n


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]), True)
        self.assertEqual(
            solution.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]), False
        )


if __name__ == "__main__":
    unittest.main()
