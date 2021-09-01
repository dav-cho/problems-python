##
#### Number of Connected Components in an Undirected Graph (medium)
#######################################################################

# You have a graph of n nodes. You are given an integer n and an array edges
# where edges[i] = [a_i, b_i] indicates that there is an edge between a_i and
# b_i in the graph.

# Return the number of connected components in the graph.

# Example 1:
# Input: n = 5, edges = [[0,1],[1,2],[3,4]]
# Output: 2

# Example 2:
# Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
# Output: 1
 
# Constraints:
# 1 <= n <= 2000
# 1 <= edges.length <= 5000
# edges[i].length == 2
# 0 <= ai <= bi < n
# ai != bi
# There are no repeated edges.

################################################################################

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
                    rank[root_x]  += 1
                    
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
        self.assertEqual(solution.countComponents(5, [[0,1],[1,2],[3,4]]), 2)
        self.assertEqual(solution.countComponents(5, [[0,1],[1,2],[2,3],[3,4]]), 1)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Depth-First Search (DFS)
###########################################
# Time: O(E+V)
# - Building the adjacency list will take O(E) operations, as we iterate over
#   the list of edges once, and insert each edge into two lists.
# - During the DFS traversal, each vertex will only be visited once. This is
#   because we mark each vertex as visited as soon as we see it, and then we
#   only visit vertices that are not marked as visited. In addition, when we
#   iterate over the edge list of each vertex, we look at each edge once. This
#   has a total cost of {O}(E + V)O(E+V).

# Space: O(E+V)
# - Building the adjacency list will take O(E) space. To keep track of visited
#   vertices, an array of size O(V) is required. Also, the run-time stack for
#   DFS will use O(V) space.

# Here E = Number of edges, V = Number of vertices.

## C++
#class Solution {
#public:
#    void dfs(vector<int> adjList[], vector<int> &visited, int src) {
#        visited[src] = 1;
#        
#        for (int i = 0; i < adjList[src].size(); i++) {
#            if (visited[adjList[src][i]] == 0) {
#                dfs(adjList, visited, adjList[src][i]);
#            }
#        }
#    }
#    
#    int countComponents(int n, vector<vector<int>>& edges) {
#        if (n == 0) return 0;
#      
#        int components = 0;
#        vector<int> visited(n, 0);
#        vector<int> adjList[n];
#    
#        for (int i = 0; i < edges.size(); i++) {
#            adjList[edges[i][0]].push_back(edges[i][1]);
#            adjList[edges[i][1]].push_back(edges[i][0]);
#        }
#        
#        for (int i = 0; i < n; i++) {
#            if (visited[i] == 0) {
#                components++;
#                dfs(adjList, visited, i);
#            }
#        }
#        return components;
#    }
#};

## Java
#class Solution {
#    
#     private void dfs(List<Integer>[] adjList, int[] visited, int startNode) {
#        visited[startNode] = 1;
#         
#        for (int i = 0; i < adjList[startNode].size(); i++) {
#            if (visited[adjList[startNode].get(i)] == 0) {
#                dfs(adjList, visited, adjList[startNode].get(i));
#            }
#        }
#    }
#    
#    public int countComponents(int n, int[][] edges) {
#        int components = 0;
#        int[] visited = new int[n];
#        
#        List<Integer>[] adjList = new ArrayList[n]; 
#        for (int i = 0; i < n; i++) {
#            adjList[i] = new ArrayList<Integer>();
#        }
#        
#        for (int i = 0; i < edges.length; i++) {
#            adjList[edges[i][0]].add(edges[i][1]);
#           adjList[edges[i][1]].add(edges[i][0]);
#        }
#        
#        for (int i = 0; i < n; i++) {
#            if (visited[i] == 0) {
#                components++;
#                dfs(adjList, visited, i);
#            }
#        }
#        return components;
#    }
#} 

## Approach 2: Disjoint Set Union (DSU)
###########################################
# Time: O(E⋅α(n))
# - Iterating over every edge requires O(E) operations, and for every operation,
#   we are performing the combine method which is O(α(n)), where α(n) is the
#   inverse Ackermann function.

# Space: O(V)
# - Storing the representative/immediate-parent of each vertex takes O(V) space.
#   Furthermore, storing the size of components also takes O(V) space.

# Here E = Number of edges, V = Number of vertices.

## C++
#class Solution {
#public:
#    int find(vector<int> &representative, int vertex) {
#        if (vertex == representative[vertex]) {
#            return vertex;
#        }
#        
#        return representative[vertex] = find(representative, representative[vertex]);
#    }
#    
#    int combine(vector<int> &representative, vector<int> &size, int vertex1, int vertex2) {
#        vertex1 = find(representative, vertex1);
#        vertex2 = find(representative, vertex2);
#        
#        if (vertex1 == vertex2) {
#            return 0;
#        } else {
#            
#            if (size[vertex1] > size[vertex2]) {
#                size[vertex1] += size[vertex2];
#                representative[vertex2] = vertex1;
#            } else {
#                size[vertex2] += sie[vertex1];
#                representative[vertex1] = vertex2;
#            }
#            return 1;
#        }
#    }
#
#    int countComponents(int n, vector<vector<int>>& edges) {
#        vector<int> representative(n), size(n);
#        
#        for (int i = 0; i < n; i++) {
#            representative[i] = i;
#            size[i] = 1;
#        }
#        
#        int components = n;
#        for (int i = 0; i < edges.size(); i++) {
#            components -= combine(representative, size, edges[i][0], edges[i][1]);
#        }
#
#        return components;
#    }
#};

## Java
#public class Solution {
#
#    private int find(int[] representative, int vertex) {
#        if (vertex == representative[vertex]) {
#            return vertex;
#        }
#        
#        return representative[vertex] = find(representative, representative[vertex]);
#    }
#    
#    private int combine(int[] representative, int[] size, int vertex1, int vertex2) {
#        vertex1 = find(representative, vertex1);
#        vertex2 = find(representative, vertex2);
#        
#        if (vertex1 == vertex2) {
#            return 0;
#        } else {
#            if (size[vertex1] > size[vertex2]) {
#                size[vertex1] += size[vertex2];
#                representative[vertex2] = vertex1;
#            } else {
#                size[vertex2] += size[vertex1];
#               representative[vertex1] = vertex2;
#            }
#            return 1;
#        }
#    }
#
#    public int countComponents(int n, int[][] edges) {
#        int[] representative = new int[n];
#        int[] size = new int[n];
#        
#        for (int i = 0; i < n; i++) {
#            representative[i] = i;
#            size[i] = 1;
#        }
#        
#        int components = n;
#        for (int i = 0; i < edges.length; i++) { 
#            components -= combine(representative, size, edges[i][0], edges[i][1]);
#        }
#
#        return components;
#    }
#} 


