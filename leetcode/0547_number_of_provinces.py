##
#### 547. Number of Provinces (medium)
##########################################


## first attempt
##############################
class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        N = len(isConnected)
        uf = UnionFind(N)
        for i in range(N):
            for j in range(i + 1, N):
                if isConnected[i][j] == 1:
                    uf.union(i, j)

        roots = set()
        for k in range(len(uf.root)):
            roots.add(uf.find(k))

        return len(roots)


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

    def connected(self, x, y):
        return self.find(x) == self.find(y)


## disjoint set
##############################
class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        N = len(isConnected)
        uf = UnionFind(N)
        for i in range(N):
            for j in range(i + 1, N):
                if isConnected[i][j] == 1:
                    uf.union(i, j)

        return uf.get_count()


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.count = size

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
        elif self.rank[root_x] > self.rank[root_y]:
            self.root[root_x] = root_y
        else:
            self.root[root_y] = root_x
            self.rank[root_x] += 1
        self.count -= 1

    def get_count(self):
        return self.count


## dfs
##############################
class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        N = len(isConnected)
        seen = set()

        def dfs(i):
            for j in range(N):
                if isConnected[i][j] == 1 and j not in seen:
                    seen.add(j)
                    dfs(j)

        count = 0
        for i in range(N):
            if i not in seen:
                dfs(i)
                count += 1

        return count


class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        N = len(isConnected)
        seen = set()

        def dfs(node):
            for j, x in enumerate(isConnected[node]):
                if x and j not in seen:
                    seen.add(j)
                    dfs(j)

        count = 0
        for i in range(N):
            if i not in seen:
                dfs(i)
                count += 1

        return count


## bfs
##############################
class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        N = len(isConnected)
        seen = set()
        count = 0
        stack = []
        for i in range(N):
            if i in seen:
                continue

            stack.append(i)
            while stack:
                s = stack.pop()
                seen.add(s)
                for j in range(N):
                    if isConnected[s][j] == 1 and j not in seen:
                        stack.append(j)
            count += 1

        return count


import collections


class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        N = len(isConnected)
        seen = set()
        count = 0
        queue = collections.deque()
        for i in range(N):
            if i in seen:
                continue

            queue.append(i)
            while queue:
                s = queue.popleft()
                seen.add(s)
                for j in range(N):
                    if isConnected[s][j] == 1 and j not in seen:
                        queue.append(j)
            count += 1

        return count


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]), 2)
        self.assertEqual(solution.findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), 3)


if __name__ == "__main__":
    unittest.main()
