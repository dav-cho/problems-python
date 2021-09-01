##
#### Number of Provinces (medium)
#####################################

# There are n cities. Some of them are connected, while some are not. If city
# a is connected directly with city b, and city b is connected directly with
# city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other
# cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the
# ith city and the jth city are directly connected, and isConnected[i][j] = 0
# otherwise.

# Return the total number of provinces.

# Example 1:
# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2

# Example 2:
# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]

# Output: 3
 
# Constraints:
# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][] is 1 or 0.
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]j

################################################################################

## first attempt
##############################
class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        N = len(isConnected)
        uf = UnionFind(N)
        for i in range(N):
            for j in range(N):
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
            for j in range(N):
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
        self.assertEqual(solution.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]), 2)
        self.assertEqual(solution.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]), 3)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Using Depth First Search[Accepted]
#####################################################
# Time: O(n^2) - The complete matrix of size n^2 is traversed.
# Space: O(n) - Visited array of size n is used.

## Java

#public class Solution {
#    public void dfs(int[][] M, int[] visited, int i) {
#        for (int j = 0; j < M.length; j++) {
#            if (M[i][j] == 1 && visited[j] == 0) {
#                visited[j] = 1;
#                dfs(M, visited, j);
#            }
#        }
#    }
#    public int findCircleNum(int[][] M) {
#        int[] visited = new int[M.length];
#        int count = 0;
#        for (int i = 0; i < M.length; i++) {
#            if (visited[i] == 0) {
#                dfs(M, visited, i);
#                count++;
#            }
#        }
#        return count;
#    }
#}


## Approach 2: Using Breadth First Search[Accepted]
#######################################################
# Time: O(n^2) - The complete matrix of size n^2 is traversed.
# Space: O(n) - A queue and visited array of size n is used.

## Java
#public class Solution {
#    public int findCircleNum(int[][] M) {
#        int[] visited = new int[M.length];
#        int count = 0;
#        Queue < Integer > queue = new LinkedList < > ();
#        for (int i = 0; i < M.length; i++) {
#            if (visited[i] == 0) {
#                queue.add(i);
#                while (!queue.isEmpty()) {
#                    int s = queue.remove();
#                    visited[s] = 1;
#                    for (int j = 0; j < M.length; j++) {
#                        if (M[s][j] == 1 && visited[j] == 0)
#                            queue.add(j);
#                    }
#                }
#                count++;
#            }
#        }
#        return count;
#    }
#}


## Approach 3: Using Union-Find Method[Accepted]
####################################################
# Time: O(n^3) - We traverse over the complete matrix once. Union and find
#                operations take O(n) time in the worst case.
# Space: O(n) -  parentparent array of size n is used.

## Java
#public class Solution {
#    int find(int parent[], int i) {
#        if (parent[i] == -1)
#            return i;
#        return find(parent, parent[i]);
#    }
#
#    void union(int parent[], int x, int y) {
#        int xset = find(parent, x);
#        int yset = find(parent, y);
#        if (xset != yset)
#            parent[xset] = yset;
#    }
#    public int findCircleNum(int[][] M) {
#        int[] parent = new int[M.length];
#        Arrays.fill(parent, -1);
#        for (int i = 0; i < M.length; i++) {
#            for (int j = 0; j < M.length; j++) {
#                if (M[i][j] == 1 && i != j) {
#                    union(parent, i, j);
#                }
#            }
#        }
#        int count = 0;
#        for (int i = 0; i < parent.length; i++) {
#            if (parent[i] == -1)
#                count++;
#        }
#        return count;
#    }
#}


## Disjoint Set from Explore/Learn/Graphs Card
##################################################
# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        # Use a rank array to record the height of each vertex, i.e., the "rank" of each vertex.
        # The initial "rank" of each vertex is 1, because each of them is
        # a standalone vertex with no connection to other vertices.
        self.rank = [1] * size
        self.count = size

    # The find function here is the same as that in the disjoint set with path compression.
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # The union function with union by rank
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
            self.count -= 1

    def getCount(self):
        return self.count


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected or len(isConnected) == 0:
            return 0
        n = len(isConnected)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    uf.union(i, j)
        return uf.getCount()


