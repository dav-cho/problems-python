##
#### 1168. Optimize Water Distribution in a Village (hard)
##############################################################


import heapq
from collections import defaultdict


## prim's algorithm w/ heap
###############################
class Solution:
    def minCostToSupplyWater(
        self, n: int, wells: list[int], pipes: list[list[int]]
    ) -> int:
        graph = defaultdict(list)
        for i, cost in enumerate(wells):
            graph[0].append((cost, i + 1))

        for house_a, house_b, cost in pipes:
            graph[house_a].append((cost, house_b))
            graph[house_b].append((cost, house_a))

        seen = set([0])
        heapq.heapify(graph[0])
        edges = graph[0]

        total_cost = 0
        while len(seen) < n + 1:
            cost, next_house = heapq.heappop(edges)
            if next_house not in seen:
                seen.add(next_house)
                total_cost += cost
                for new_cost, neighbor in graph[next_house]:
                    if neighbor not in seen:
                        heapq.heappush(edges, (new_cost, neighbor))

        return total_cost


class Solution:
    def minCostToSupplyWater(
        self, n: int, wells: list[int], pipes: list[list[int]]
    ) -> int:
        graph = defaultdict(list)
        for idx, cost in enumerate(wells):
            graph[0].append((cost, idx + 1))

        for house_1, house_2, cost in pipes:
            graph[house_1].append((cost, house_2))
            graph[house_2].append((cost, house_1))

        mst_set = set([0])
        heapq.heapify(graph[0])
        edges_heap = graph[0]
        total_cost = 0

        while len(mst_set) < n + 1:
            cost, next_house = heapq.heappop(edges_heap)
            if next_house not in mst_set:
                mst_set.add(next_house)
                total_cost += cost
                for new_cost, neighbor in graph[next_house]:
                    if neighbor not in mst_set:
                        heapq.heappush(edges_heap, (new_cost, neighbor))

        return total_cost


class Solution:
    def minCostToSupplyWater(
        self, n: int, wells: list[int], pipes: list[list[int]]
    ) -> int:
        graph = defaultdict(list)
        for i, cost in enumerate(wells):
            graph[0].append((cost, i + 1))

        for house_a, house_b, cost in pipes:
            graph[house_a].append((cost, house_b))
            graph[house_b].append((cost, house_a))

        seen = set([0])
        heapq.heapify(graph[0])
        total_cost = 0
        while len(seen) < n + 1:
            cost, next_house = heapq.heappop(graph[0])
            if next_house not in seen:
                seen.add(next_house)
                total_cost += cost
                for new_cost, neighbor in graph[next_house]:
                    if neighbor not in seen:
                        heapq.heappush(graph[0], (new_cost, neighbor))

        return total_cost


## kruskal's algorithm w/ union find
########################################
class Solution:
    def minCostToSupplyWater(
        self, n: int, wells: list[int], pipes: list[list[int]]
    ) -> int:
        edges = []
        for i, cost in enumerate(wells):
            edges.append((cost, 0, i + 1))

        for house_a, house_b, cost in pipes:
            edges.append((cost, house_a, house_b))

        edges.sort(key=lambda x: x[0])
        uf = UnionFind(n)
        total_cost = 0
        for cost, house_a, house_b in edges:
            if uf.union(house_a, house_b):
                total_cost += cost

        return total_cost


class UnionFind:
    def __init__(self, size):
        # add one to size because of 1-indexing
        self.root = list(range(size + 1))
        self.rank = [1] * (size + 1)

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])

        return self.root[x]

    def union(self, x, y):
        root_x, root_y = map(self.find, (x, y))
        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        else:
            self.root[root_y] = root_x
            self.rank[root_x] += 1

        return True


class Solution:
    def minCostToSupplyWater(
        self, n: int, wells: list[int], pipes: list[list[int]]
    ) -> int:
        edges = []
        for i, weight in enumerate(wells):
            edges.append((weight, 0, i + 1))

        for house_a, house_b, weight in pipes:
            edges.append((weight, house_a, house_b))

        edges.sort(key=lambda x: x[0])
        uf = UnionFind(n)
        total_cost = 0
        for cost, house_a, house_b in edges:
            if uf.union(house_a, house_b):
                total_cost += cost

        return total_cost


class UnionFind:
    def __init__(self, size):
        # add one to size because of 1-indexing
        self.root = list(range(size + 1))
        self.rank = [1] * (size + 1)

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])

        return self.root[x]

    def union(self, x, y):
        root_x, root_y = map(self.find, (x, y))
        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = root_y
        else:
            self.root[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1

        return True


class Solution:
    def minCostToSupplyWater(
        self, n: int, wells: list[int], pipes: list[list[int]]
    ) -> int:
        edges = []
        for i, weight in enumerate(wells):
            edges.append((weight, 0, i + 1))

        for house_a, house_b, cost in pipes:
            edges.append((cost, house_a, house_b))

        edges.sort(key=lambda x: x[0])
        uf = UnionFind(n)
        total_cost = 0
        for cost, house_a, house_b in edges:
            if uf.union(house_a, house_b):
                total_cost += cost

        return total_cost


class UnionFind:
    def __init__(self, size):
        # add one to size because of 1-indexing
        self.root = list(range(size + 1))
        self.rank = [1] * (size + 1)

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])

        return self.root[x]

    def union(self, x, y):
        root_x, root_y = map(self.find, (x, y))
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


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(
            solution.minCostToSupplyWater(3, [1, 2, 2], [[1, 2, 1], [2, 3, 1]]), 3
        )
        self.assertEqual(solution.minCostToSupplyWater(2, [1, 1], [[1, 2, 1]]), 2)


if __name__ == "__main__":
    unittest.main()
