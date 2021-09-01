##
#### Graph Valid Tree (medium)
##################################

# You have a graph of n nodes labeled from 0 to n - 1. You are given an integer
# n and a list of edges where edges[i] = [ai, bi] indicates that there is an
# undirected edge between nodes ai and bi in the graph.

# Return true if the edges of the given graph make up a valid tree, and false
# otherwise.

# Example 1:
# Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
# Output: true

# Example 2:
# Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
# Output: false
 
# Constraints:
# 1 <= 2000 <= n
# 0 <= edges.length <= 5000
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# There are no self-loops or repeated edges.

################################################################################

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

        return len(seen) ==n


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
        self.assertEqual(solution.validTree(5, [[0,1],[0,2],[0,3],[1,4]]), True)
        self.assertEqual(solution.validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]]), False)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Graph Theory + Iterative Depth-First Search
##############################################################
# Time: O(N + E)
# - Creating the adjacency list requires initialising a list of length N, with
#   a cost of O(N), and then iterating over and inserting E edges, for a cost
#   of O(E). This gives us O(E) + O(N) = O(N + E).
# - Each node is added to the data structure once. This means that the outer
#   loop will run N times. For each of the N nodes, its adjacent edges is
#   iterated over once. In total, this means that all E edges are iterated over
#   once by the inner loop. This, therefore, gives a total time complexity of O(N + E).
# - Because both parts are the same, we get a final time complexity of O(N + E).

# Space: O(N + E)
# - The adjacency list is a list of length N, with inner lists with lengths that
#   add to a total of E. This gives a total of O(N + E) space.
# - In the worst case, the stack/ queue will have all N nodes on it at the same
#   time, giving a total of O(N) space.
# - In total, this gives us O(E + N) space.

# Let E be the number of edges, and N be the number of nodes.

# Recall that a graph, G, is a tree iff the following two conditions are met:
# - G is fully connected. In other words, for every pair of nodes in G, there is
#   a path between them.
# - G contains no cycles. In other words, there is exactly one path between each
#   pair of nodes in G.

## DFS
####################
def validTree(self, n: int, edges: List[List[int]]) -> bool:
    
    if len(edges) != n - 1: return False
    
    adj_list = [[] for _ in range(n)]
    for A, B in edges:
        adj_list[A].append(B)
        adj_list[B].append(A)
    
    seen = set()
    
    def dfs(node, parent):
        if node in seen: return;
        seen.add(node)
        for neighbour in adj_list[node]:
            if neighbour == parent:
                continue
            if neighbour in seen:
                return False
            result = dfs(neighbour, node)
            if not result: return False
        return True
    
    # We return true iff no cycles were detected,
    # AND the entire graph has been reached.
    return dfs(0, -1) and len(seen) == n

#class Solution {
#    
#    private List<List<Integer>> adjacencyList = new ArrayList<>();
#    private Set<Integer> seen = new HashSet<>();
#    
#    
#    public boolean validTree(int n, int[][] edges) {
#        
#        if (edges.length != n - 1) return false;
#        
#        for (int i = 0; i < n; i++) {
#            adjacencyList.add(new ArrayList<>());
#        }
#        for (int[] edge : edges) {
#            adjacencyList.get(edge[0]).add(edge[1]);
#            adjacencyList.get(edge[1]).add(edge[0]);
#        }
#        
#        // We return true iff no cycles were detected,
#        // AND the entire graph has been reached.
#        return dfs(0, -1) && seen.size() == n;   
#    }
#    
#    public boolean dfs(int node, int parent) {
#        if (seen.contains(node)) return false;
#        seen.add(node);
#        for (int neighbour : adjacencyList.get(node)) {
#            if (parent != neighbour) {
#                boolean result = dfs(neighbour, node);
#                if (!result) return false;
#            }
#        }
#        return true;
#    }
#}

## BFS
####################
def validTree(self, n: int, edges: List[List[int]]) -> bool:
    
    if len(edges) != n - 1: return False
    
    adj_list = [[] for _ in range(n)]
    for A, B in edges:
        adj_list[A].append(B)
        adj_list[B].append(A)
    
    parent = {0: -1}
    queue = collections.deque([0])
    
    while queue:
        node = queue.popleft()
        for neighbour in adj_list[node]:
            if neighbour == parent[node]:
                continue
            if neighbour in parent:
                return False
            parent[neighbour] = node
            queue.append(neighbour)
    
    return len(parent) == n

## Java
#public boolean validTree(int n, int[][] edges) {
#            
#    List<List<Integer>> adjacencyList = new ArrayList<>();
#    for (int i = 0; i < n; i++) {
#        adjacencyList.add(new ArrayList<>());
#    }
#    for (int[] edge : edges) {
#        adjacencyList.get(edge[0]).add(edge[1]);
#        adjacencyList.get(edge[1]).add(edge[0]);
#    }
#    
#    Map<Integer, Integer> parent = new HashMap<>();
#    parent.put(0, -1);
#    Queue<Integer> queue = new LinkedList<>();
#    queue.offer(0);
#
#    while (!queue.isEmpty()) {
#        int node = queue.poll();
#        for (int neighbour : adjacencyList.get(node)) {
#            if (parent.get(node) == neighbour) {
#                continue;
#            }
#            if (parent.containsKey(neighbour)) {
#               return false;
#            }
#            queue.offer(neighbour);
#            parent.put(neighbour, node);
#        }
#    }
#    
#    return parent.size() == n;   
#} 


## Approach 2: Advanced Graph Theory + Iterative Depth-First Search
#######################################################################
# Time: O(N)
# - When E ≠ N - 1, we simply return false. Therefore, the worst case is when
#   E = N - 1. Because E is proportional to N, we'll say E = N to simplify the
#   analysis.
# - As said above, creating an adjacency list has a time complexity of O(N + E).
#   Because E is now bounded by N, we can reduce this slightly to
#   O(N + N) = O(N).
# - The iterative breadth-first search and depth-first search are almost
#   identical. Each node is put onto the queue/stack once, ensured by the seen
#   set. Therefore, the inner "neighbour" loop runs once for each node. Across
#   all nodes, the number of cycles this loop does is the same as the number of
#   edges, which is simply N. Therefore, these two algorithms have a time
#   complexity of O(N).
# - The recursive depth-first search's "neighbour" loop runs only once for each
#   node. Therefore, in total, the function is called once for each edge. So it
#   is called E = N times, and N of those times, it actually enters the
#   "neighbour" loop. Collectively, the total number of iterations of the
#   "neighbour" loop is E = N. So we get O(N), as these all simply add.

# Space: O(N + E)
# - Previously, we determined that the adjacency list took O(E + N) space. We
#   now know this is simply O(N).
# - In the worst case, the search algorithms will require an additional O(N)
#   space; this is if all nodes were on the stack/queue at the same time.
# - So again we get a total of O(N).

# Let E be the number of edges, and N be the number of nodes.

# For the graph to be a valid tree, it must have exactly n - 1 edges. Any less,
# and it can't possibly be fully connected. Any more, and it has to contain
# cycles. Additionally, if the graph is fully connected and contains exactly
# n - 1 edges, it can't possibly contain a cycle, and therefore must be a tree!

# Going by this definition, our algorithm needs to do the following:
# - Check whether or not there are n - 1 edges. If there's not, then return
#   false.
# - Check whether or not the graph is fully connected. Return true if it is,
#   false if otherwise.

## Iterative DFS
####################
def validTree(self, n: int, edges: List[List[int]]) -> bool:
    
    if len(edges) != n - 1: return False
    
    # Create an adjacency list.
    adj_list = [[] for _ in range(n)]
    for A, B in edges:
        adj_list[A].append(B)
        adj_list[B].append(A)
    
    # We still need a seen set to prevent our code from infinite
    # looping if there *is* cycles (and on the trivial cycles!)
    seen = {0}
    stack = [0]
    
    while stack:
        node = stack.pop()
        for neighbour in adj_list[node]:
            if neighbour in seen:
                continue
            seen.add(neighbour)
            stack.append(neighbour)
    
    return len(seen) == n

## Java
#public boolean validTree(int n, int[][] edges) {
#        
#    if (edges.length != n - 1) return false;
#    
#    // Make the adjacency list.
#    List<List<Integer>> adjacencyList = new ArrayList<>();
#    for (int i = 0; i < n; i++) {
#        adjacencyList.add(new ArrayList<>());
#    }
#    for (int[] edge : edges) {
#        adjacencyList.get(edge[0]).add(edge[1]);
#        adjacencyList.get(edge[1]).add(edge[0]);
#    }
#    
#    Stack<Integer> stack = new Stack<>();
#    Set<Integer> seen = new HashSet<>();
#    stack.push(0);
#    seen.add(0);
#    
#    while (!stack.isEmpty()) {
#        int node = stack.pop();
#        for (int neighbour : adjacencyList.get(node)) {
#            if (seen.contains(neighbour)) continue;
#            seen.add(neighbour);
#           stack.push(neighbour);
#        }
#    }
#    
#    return seen.size() == n;   
#} 

## Recursive DFS
####################
def validTree(self, n: int, edges: List[List[int]]) -> bool:
    
    if len(edges) != n - 1: return False
    
    # Create an adjacency list.
    adj_list = [[] for _ in range(n)]
    for A, B in edges:
        adj_list[A].append(B)
        adj_list[B].append(A)
    
    # We still need a seen set to prevent our code from infinite
    # looping if there *is* cycles (and on the trivial cycles!)
    seen = set()

    def dfs(node):
        if node in seen: return
        seen.add(node)
        for neighbour in adj_list[node]:
            dfs(neighbour)

    dfs(0)
    return len(seen) == n

## Java
#class Solution {
#    
#    private List<List<Integer>> adjacencyList = new ArrayList<>();
#    private Set<Integer> seen = new HashSet<>();
#    
#    
#    public boolean validTree(int n, int[][] edges) {
#        
#        if (edges.length != n - 1) return false;
#        
#        // Make the adjacency list.
#        for (int i = 0; i < n; i++) {
#            adjacencyList.add(new ArrayList<>());
#        }
#        for (int[] edge : edges) {
#            adjacencyList.get(edge[0]).add(edge[1]);
#            adjacencyList.get(edge[1]).add(edge[0]);
#        }
#        
#        // Carry out depth first search.
#        dfs(0);
#        // Inspect result and return the verdict.
#        return seen.size() == n;   
#    }
#    
#    public void dfs(int node) {
#        if (sen.contains(node)) return;
#        seen.add(node);
#        for (int neighbour : adjacencyList.get(node)) {
#            dfs(neighbour);
#        }
#    }
#}

## Iterative BFS
####################
def validTree(self, n: int, edges: List[List[int]]) -> bool:
    
    if len(edges) != n - 1: return False
    
    # Create an adjacency list.
    adj_list = [[] for _ in range(n)]
    for A, B in edges:
        adj_list[A].append(B)
        adj_list[B].append(A)
    
    # We still need a seen set to prevent our code from infinite
    # looping if there *is* cycles (and on the trivial cycles!)
    seen = {0}
    queue = collections.deque([0])
    
    while queue:
        node = queue.popleft()
        for neighbour in adj_list[node]:
            if neighbour in seen:
                continue
            seen.add(neighbour)
            queue.append(neighbour)
    
    return len(seen) == n

## Java
#public boolean validTree(int n, int[][] edges) {
#    
#    if (edges.length != n - 1) return false;
#    
#    // Make the adjacency list.
#    List<List<Integer>> adjacencyList = new ArrayList<>();
#    for (int i = 0; i < n; i++) {
#        adjacencyList.add(new ArrayList<>());
#    }
#    for (int[] edge : edges) {
#        adjacencyList.get(edge[0]).add(edge[1]);
#        adjacencyList.get(edge[1]).add(edge[0]);
#    }
#    
#    Queue<Integer> queue = new LinkedList<>();
#    Set<Integer> seen = new HashSet<>();
#    queue.offer(0);
#    seen.add(0);
#    
#    while (!queue.isEmpty()) {
#        int node = queue.poll();
#        for (int neighbour : adjacencyList.get(node)) {
#            if (seen.contains(neighbour)) continue;
#            seen.add(neighbour);
#           queue.offer(neighbour);
#        }
#    }
#    
#    return seen.size() == n;   
#} 


## Approach 3: Advanced Graph Theory + Union Find
#####################################################
# Time: O(N⋅α(N))
# - When E ≠ N - 1, we simply return false. Therefore, the worst case is when
#   E = N - 1. Because E is proportional to N, we'll say E = N to simplify the
#   analysis.
# - We are putting each of the N edges into the UnionFind data structure, using
#   the union(...) method. The union(...) method itself has no loops or
#   recursion, so the entire cost of calling it is dependent on the cost of the
#   find(...) method that it calls.
# - find(...)'s cost is dependent on how far the node it was searching for is
#   from the root. Using the naïve implementation of union find, this depth
#   could be N. If this was the case for all of the calls, we'd have a final
#   cost of O(N^2).
# - However, remember those optimizations we did? Those keep the tree depths
#   very sallow. It turns out that find(...) amortizes to O(α(N)), where α is
#   the Inverse Ackermann Function. The incredible thing about this function is
#   that it grows so slowly that N will never go higher than 4 in the universe
#   as we know it! So while in "practice" it is effectively O(1), in "theory"
#   it is not.
# - Actually proving this upper bound on the depth is a very advanced proof,
#   which I'd certainly hope you'd never need to do in an interview! If you're
#   interested though, I recommend looking in a good algorithm's text book or
#   paper.
# - Anyway, this gives us a total of N⋅O(α(N))=O(N⋅α(N)).

# Space: 
# - The UnionFind data structure requires O(N) space to the store the arrays it
#   uses.

# Let E be the number of edges, and N be the number of nodes.
# α(N) is the Inverse Ackermann Function.
# https://en.wikipedia.org/wiki/Ackermann_function#Inverse

# So, why is this better than Approach 2?
# - Complexity analysis ignores constants. For example, O(10⋅N)=O(N). Even
#   O(10000⋅N)=O(N). Sometimes the constants we're ignoring in the analysis are
#   still having a big impact on the run-time in practice.
# - Approach 2 had a lot of overhead in needing to create an adjacency list
#   with the edges before it could even begin the depth-first search. This is
#   all treated as a constant, as it ultimately had the same time complexity as
#   the depth-first search itself.
# - Approach 3 doesn't need to change the input format, it can just get straight
#   to determining whether or not there is a cycle. Additionally the bit that
#   stops it being constant, the α(N), will never have a value larger than 4.
#   So in practice, it behaves as a constant too—and a far smaller one at that!
# - When weighing up the pros and cons of different algorithms for solving
#   problems, it's best to treat union find's operations as O(1) to get a fair
#   and accurate comparison.

## without optmizations
#########################
class UnionFind:
    
    # For efficiency, we aren't using makeset, but instead initialising
    # all the sets at the same time in the constructor.
    def __init__(self, n):
        self.parent = [node for node in range(n)]
        
    # The find method, without any optimizations. It traces up the parent
    # links until it finds the root node for A, and returns that root.
    def find(self, A):
        while A != self.parent[A]:
            A = self.parent[A]
        return A
        
    # The union method, without any optimizations. It returns True if a
    # merge happened, False if otherwise.
    def union(self, A, B):
        # Find the roots for A and B.
        root_A = self.find(A)
        root_B = self.find(B)
        # Check if A and B are already in the same set.
        if root_A == root_B:
            return False
        # Merge the sets containing A and B.
        self.parent[root_A] = root_B
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Condition 1: The graph must contain n - 1 edges.
        if len(edges) != n - 1: return False
        
        # Condition 2: The graph must contain a single connected component.
        # Create a new UnionFind object with n nodes. 
        unionFind = UnionFind(n)
        # Add each edge. Check if a merge happened, because if it 
        # didn't, there must be a cycle.
        for A, B in edges:
            if not unionFind.union(A, B):
                return False
        # If we got this far, there's no cycles!
        return True
        

## Java
#class UnionFind {
#    
#    private int[] parent;
#    
#    // For efficiency, we aren't using makeset, but instead initialising
#    // all the sets at the same time in the constructor.
#    public UnionFind(int n) {
#        parent = new int[n];
#        for (int node = 0; node < n; node++) {
#            parent[node] = node;
#        }
#    }
#    
#    // The find method, without any optimizations. It traces up the parent
#    // links until it finds the root node for A, and returns that root.
#    public int find(int A) {
#        while (parent[A] != A) {
#            A = parent[A];
#        }
#        return A;
#    }
#
#    // The union method, without any optimizations. It returns True if a
#    // merge happened, False if otherwise.
#    public boolean union(int A, int B) {
#        // Find the roots for A and B.
#        int rootA = find(A);
#        int rootB = find(B);
#        // Check if A and B are already in the same set.
#        if (rootA == rootB) {
#            return false;
#        }
#        // Merge the sets containing A and B.
#        parent[rootA] = rootB;
#        return true;
#    } 
#}
#
#class Solution {
#    
#    public boolean validTree(int n, int[][] edges) {
#        
#        // Condition 1: The graph must contain n - 1 edges.
#        if (edges.length != n - 1) return false;
#        
#        // Condition 2: The graph must contain a single connected component.
#        // Create a new UnionFind object with n nodes. 
#        UnionFind unionFind = new UnionFind(n);
#        // Add each edge. Check if a merge happened, because if it 
#        // didn't, there must be a cycle.
#        for (int[] edge : edges) {
#            int A = edge[0];
#            int B = edge[1];
#            if (!unionFind.union(A, B)) {
#                return false;
#            }
#        }
#        
#        // If we got this far, there's no cycles!
#        return true;
#    }
#    
#}


## optimized with path compression and union by size
########################################################
class UnionFind:
    
    # For efficiency, we aren't using makeset, but instead initialising
    # all the sets at the same time in the constructor.
    def __init__(self, n):
        self.parent = [node for node in range(n)]
        # We use this to keep track of the size of each set.
        self.size = [1] * n
        
    # The find method, with path compression. There are ways of implementing
    # this elegantly with recursion, but the iterative version is easier for
    # most people to understand!
    def find(self, A):
        # Step 1: Find the root.
        root = A
        while root != self.parent[root]:
            root = self.parent[root]
        # Step 2: Do a second traversal, this time setting each node to point
        # directly at A as we go.
        while A != root:
            old_root = self.parent[A]
            self.parent[A] = root
            A = old_root
        return root
        
    # The union method, with optimization union by size. It returns True if a
    # merge happened, False if otherwise.
    def union(self, A, B):
        # Find the roots for A and B.
        root_A = self.find(A)
        root_B = self.find(B)
        # Check if A and B are already in the same set.
        if root_A == root_B:
            return False
        # We want to ensure the larger set remains the root.
        if self.size[root_A] < self.size[root_B]:
            # Make root_B the overall root.
            self.parent[root_A] = root_B
            # The size of the set rooted at B is the sum of the 2.
            self.size[root_B] += self.size[root_A]
        else:
            # Make root_A the overall root.
            self.parent[root_B] = root_A
            # The size of the set rooted at A is the sum of the 2.
            self.size[root_A] += self.size[root_B]
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Condition 1: The graph must contain n - 1 edges.
        if len(edges) != n - 1: return False
        
        # Create a new UnionFind object with n nodes. 
        unionFind = UnionFind(n)
        
        # Add each edge. Check if a merge happened, because if it 
        # didn't, there must be a cycle.
        for A, B in edges:
            if not unionFind.union(A, B):
                return False
        
        # If we got this far, there's no cycles!
        return True


## Java
#class UnionFind {
#    
#    private int[] parent;
#    private int[] size; // We use this to keep track of the size of each set.
#    
#    // For efficiency, we aren't using makeset, but instead initialising
#    // all the sets at the same time in the constructor.
#    public UnionFind(int n) {
#        parent = new int[n];
#        size = new int[n];
#        for (int node = 0; node < n; node++) {
#            parent[node] = node;
#            size[node] = 1;
#        }
#    }
#    
#    // The find method, with path compression. There are ways of implementing
#    // this elegantly with recursion, but the iterative version is easier for
#    // most people to understand!
#    public int find(int A) {
#        // Step 1: Find the root.
#        int root = A;
#        wile (parent[root] != root) {
#            root = parent[root];
#        }
#        // Step 2: Do a second traversal, this time setting each node to point
#        // directly at A as we go.
#        while (A != root) {
#            int oldRoot = parent[A];
#            parent[A] = root;
#            A = oldRoot;
#        }
#        return root;
#    }
#
#    // The union method, with optimization union by size. It returns True if a
#    // merge happened, False if otherwise.
#    public boolean union(int A, int B) {
#        // Find the roots for A and B.
#        int rootA = find(A);
#        int rootB = find(B);
#        // Check if A and B are already in the same set.
#        if (rootA == rootB) {
#            return false;
#        }
#        // We want to ensure the larger set remains the root.
#        if (size[rootA] < size[rootB]) {
#            // Make rootB the overall root.
#            parent[rootA] = rootB;
#            // The size of the set rooted at B is the sum of the 2.
#            size[rootB] += size[rootA];
#        }
#        else {
#            // Make rootA the overall root.
#            parent[rootB] = rootA;
#            // The size of the set rooted at A is the sum of the 2.
#            size[rootA] += size[rootB];
#        }
#        return true;
#    } 
#}
#
#class Solution {
#    
#    public boolean validTree(int n, int[][] edges) {
#        
#        // Condition 1: The graph must contain n - 1 edges.
#        if (edges.length != n - 1) return false;
#        
#        // Condition 2: The graph must contain a single connected component.
#        // Create a new UnionFind object with n nodes. 
#        UnionFind unionFind = new UnionFind(n);
#        // Add each edge. Check if a merge happened, because if it 
#        // didn't, there must be a cycle.
#        for (int[] edge : edges) {
#            int A = edge[0];
#            int B = edge[1];
#            if (!unionFind.union(A, B)) {
#                return false;
#            }
#        }
#        
#        // If we got this far, there's no cycles!
#        return true;
#    }
#    
#}

