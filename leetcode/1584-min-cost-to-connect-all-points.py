##
#### Min Cost to Connect All Points (medium)
################################################

# You are given an array points representing integer coordinates of some points
# on a 2D-plane, where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan
# distance between them: |xi - xj| + |yi - yj|, where |val| denotes the
# absolute value of val.

# Return the minimum cost to make all points connected. All points
# are connected if there is exactly one simple path between any two points.

# Example 1:
# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
# Explanation:

# We can connect the points as shown above to get the minimum cost of 20.
# Notice that there is a unique path between every pair of points.

# Example 2:
# Input: points = [[3,12],[-2,5],[-4,1]]
# Output: 18

# Example 3:
# Input: points = [[0,0],[1,1],[,0],[-1,1]]
# Output: 4

# Example 4:
# Input: points = [[-1000000,-1000000],[1000000,1000000]]
# Output: 4000000

# Example 5:
# Input: points = [[0,0]]
# Output: 0
 
# Constraints:
# 1 <= points.length <= 1000
# -106 <= xi, yi <= 106
# All pairs (xi, yi) are distinct.

################################################################################

## kruskal's algorithm - min spanning tree / union find
###########################################################
import heapq

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        if not points or len(points) == 0:
            return 0
        
        size = len(points)
        pq = []     #pq = priority queue (heap)
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
        self.assertEqual(solution.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]), 20)
        self.assertEqual(solution.minCostConnectPoints([[3,12],[-2,5],[-4,1]]), 18)
        self.assertEqual(solution.minCostConnectPoints([[0,0],[1,1],[0],[-1,1]]), 4)
        self.assertEqual(solution.minCostConnectPoints([[-1000000,-1000000],[1000000,1000000]]), 4000000)
        self.assertEqual(solution.minCostConnectPoints([[0,0]]), 0)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## From Graphs Explore Card:
################################

## Approach 1: Kruskal's Algorithm - Minimum Spanning Tree
##############################################################
# Time: O(E logE) - Where E represents the number of edges.
# Space: O(V) - Where V represents the number of vertices
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points or len(points) == 0:
            return 0
        size = len(points)
        pq = []
        uf = UnionFind(size)

        for i in range(size):
            for j in range(i + 1, size):
                coordinate1 = points[i]
                coordinate2 = points[j]
                # Calculate the distance between two coordinates.
                cost = abs(coordinate1[0] -
                           coordinate2[0]) + abs(coordinate1[1] -
                                                 coordinate2[1])
                edge = Edge(i, j, cost)
                heapq.heappush(pq, edge)

        result = 0
        count = size - 1
        while pq and count > 0:
            e = heapq.heappop(pq)
            if not uf.connected(e.point1, e.point2):
                uf.union(e.point1, e.point2)
                result += e.cost
                count -= 1
        return result


class Edge:
    def __init__(self, point1, point2, cost):
        self.point1 = point1
        self.point2 = point2
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


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
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


## Approach 2: Prim's Algorithm - Minimum Spanning Tree
###########################################################
# Time: 
# Space: O(V) - Where V represents the number of vertices
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points or len(points) == 0:
            return 0
        size = len(points)
        pq = []
        visited = [False] * size
        result = 0
        count = size - 1
        # Add all edges from points[0] vertexs
        for j in range(1, size):
            # Calculate the distance between two coordinates.
            coordinate1 = points[0]
            coordinate2 = points[j]
            cost = abs(coordinate1[0] - coordinate2[0]) + abs(coordinate1[1] -
                                                              coordinate2[1])
            edge = Edge(0, j, cost)
            heapq.heappush(pq, edge)

        visited[0] = True
        while pq and count > 0:
            e = heapq.heappop(pq)
            point1 = e.point1
            point2 = e.point2
            cost = e.cost
            if not visited[point2]:
                result += cost
                visited[point2] = True
                for j in range(size):
                    if not visited[j]:
                        distance = abs(points[point2][0] -
                                       points[j][0]) + abs(points[point2][1] -
                                                           points[j][1])
                        heapq.heappush(pq, Edge(point2, j, distance))
                count -= 1
        return result


class Edge:
    def __init__(self, point1, point2, cost):
        self.point1 = point1
        self.point2 = point2
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


