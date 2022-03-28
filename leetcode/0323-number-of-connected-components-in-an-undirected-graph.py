##
#### 323. Number of Connected Components in an Undirected Graph (medium)
############################################################################


## attempt 1 - disjoint set (union find)
############################################
class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        uf = UnionFind(n)
        for x, y in edges:
            uf.union(x, y)

        for node in range(n):
            uf.find(node)

        return len(set(uf.root))


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
            return

        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = root_y
        else:
            self.root[root_y] = root_x
            self.rank[root_x] += 1


## attempt 1 - dfs recursive
################################
class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        seen = set()

        def dfs(node):
            if node in seen:
                return 0
            seen.add(node)
            for neighbor in adj_list[node]:
                dfs(neighbor)

            return 1

        count = i = 0
        while len(seen) < n:
            count += dfs(i)
            i += 1

        return count


## dfs recursive
##############################
class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
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

        count = 0
        for node in range(n):
            if node in seen:
                continue

            dfs(node)
            count += 1

        return count


## dfs iterative
##############################
class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        adj_list = {x: [] for x in range(n)}
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        count = 0
        for node in range(n):
            if node in adj_list:
                count += 1

            stack = [node]
            while stack:
                curr = stack.pop()
                if curr in adj_list:
                    stack += adj_list[curr]
                    del adj_list[curr]

        return count


class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        seen = set()
        count = 0

        for i in range(n):
            if i in seen:
                continue

            count += 1
            seen.add(i)
            stack = [i]

            while stack:
                node = stack.pop()
                for neighbor in adj_list[node]:
                    if neighbor in seen:
                        continue
                    seen.add(neighbor)
                    stack.append(neighbor)

        return count


## bfs iterative
##############################
class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        adj_list = {x: [] for x in range(n)}
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        count = 0
        for i in range(n):
            queue = [i]
            if i in adj_list:
                count += 1
            for j in queue:
                if j in adj_list:
                    queue += adj_list[j]
                    del adj_list[j]

        return count


## union find
##############################
class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        root = list(range(n))
        rank = [1] * n

        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if rank[root_x] < rank[root_y]:
                root[root_x] = root_y
            else:
                root[root_y] = root_x
                if rank[root_x] == rank[root_y]:
                    rank[root_x] += 1

        for x, y in edges:
            union(x, y)

        return len(set(map(find, root)))


class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        root = list(range(n))
        rank = [1] * n

        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]

        def union(xy):
            root_x, root_y = map(find, xy)

            if rank[root_x] < rank[root_y]:
                root[root_x] = root_y
            else:
                root[root_y] = root_x
                if rank[root_x] == rank[root_y]:
                    rank[root_x] += 1

        for edge in edges:
            union(edge)

        return len({find(node) for node in root})


class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        root = list(range(n))

        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]

        for x, y in edges:
            root[find(x)] = find(y)

        return len(set(map(find, root)))


class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        uf = UnionFind(n)
        for x, y in edges:
            uf.union(x, y)

        return len(set(map(uf.find, uf.root)))


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


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.countComponents(5, [[0, 1], [1, 2], [3, 4]]), 2)
        self.assertEqual(
            solution.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]), 1
        )


if __name__ == "__main__":
    unittest.main()
