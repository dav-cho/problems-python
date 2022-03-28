##
#### 1584. Min Cost to Connect All Points (medium)
######################################################


## kruskal's algorithm - min spanning tree / union find
###########################################################
import heapq


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        if not points or len(points) == 0:
            return 0

        size = len(points)
        pq = []  # pq = priority queue (heap)
        uf = UnionFind(size)

        for i in range(size):
            for j in range(i + 1, size):
                x1, y1 = points[i]
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)
                edge = Edge(i, j, cost)
                heapq.heappush(pq, edge)

        res = 0
        count = size - 1

        while pq and count > 0:
            e = heapq.heappop(pq)
            if not uf.connected(e.point1, e.point2):
                uf.union(e.point1, e.point2)
                res += e.cost
                count -= 1

        return res


class Edge:
    def __init__(self, point1, point2, cost):
        self.point1 = point1
        self.point2 = point2
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


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

    def connected(self, x, y):
        return self.find(x) == self.find(y)


## prim's algorithm
##############################
class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        if not points or len(points) == 0:
            return 0

        size = len(points)
        pq = []

        for i in range(1, size):
            x1, y1 = points[0]
            x2, y2 = points[i]
            cost = abs(x1 - x2) + abs(y1 - y2)
            edge = Edge(0, i, cost)
            heapq.heappush(pq, edge)

        seen = {0}
        res = 0
        count = size - 1

        while pq and count > 0:
            e = heapq.heappop(pq)
            if e.point2 in seen:
                continue

            res += e.cost
            seen.add(e.point2)

            for j in range(size):
                if j in seen:
                    continue

                x1, y1 = points[e.point2]
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)
                edge = Edge(e.point2, j, cost)
                heapq.heappush(pq, edge)

            count -= 1

        return res


class Edge:
    def __init__(self, point1, point2, cost):
        self.point1 = point1
        self.point2 = point2
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(
            solution.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]), 20
        )
        self.assertEqual(solution.minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]), 18)
        self.assertEqual(
            solution.minCostConnectPoints([[0, 0], [1, 1], [0], [-1, 1]]), 4
        )
        self.assertEqual(
            solution.minCostConnectPoints([[-1000000, -1000000], [1000000, 1000000]]),
            4000000,
        )
        self.assertEqual(solution.minCostConnectPoints([[0, 0]]), 0)


if __name__ == "__main__":
    unittest.main()
