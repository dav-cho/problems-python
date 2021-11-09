##
#### Minimum Height Trees (medium)
########################################

# A tree is an undirected graph in which any two vertices are connected by
# exactly one path. In other words, any connected graph without simple cycles
# is a tree.

# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges
# where edges[i] = [ai, bi] indicates that there is an undirected edge between
# the two nodes ai and bi in the tree, you can choose any node of the tree as
# the root. When you select a node x as the root, the result tree has height h.
# Among all possible rooted trees, those with minimum height (i.e. min(h)) are
# called minimum height trees (MHTs).

# Return a list of all MHTs' root labels. You can return the answer in any
# order.

# The height of a rooted tree is the number of edges on the longest downward
# path between the root and a leaf.

# Example 1:
# Input: n = 4, edges = [[1,0],[1,2],[1,3]]
# Output: [1]
# Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.

# Example 2:
# Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
# Output: [3,4]

# Example 3:
# Input: n = 1, edges = []
# Output: [0]

# Example 4:
# Input: n = 2, edges = [[0,1]]
# Output: [0,1]
 
# Constraints:
# 1 <= n <= 2 * 104
# edges.length == n - 1
# 0 <= ai, bi < n
# ai != bi
# All the pairs (ai, bi) are distinct.
# The given input is guaranteed to be a tree and there will be no repeated edges.

################################################################################


## topological sorting (kahn's algorithm)
#############################################
class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n <= 2:
            return list(range(n))
        
        adj_list = [set() for _ in range(n)]
        for start, end in edges:
            adj_list[start].add(end)
            adj_list[end].add(start)
            
        queue = [node for node in range(n) if len(adj_list[node]) == 1]
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(queue)
            new_queue = []
            while queue:
                leaf = queue.pop()
                neighbor = adj_list[leaf].pop()
                adj_list[neighbor].remove(leaf)
                if len(adj_list[neighbor]) == 1:
                    new_queue.append(neighbor)
            queue = new_queue
            
        return queue


class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n <= 2:
            return list(range(n))
        
        adj_list = [set() for _ in range(n)]
        for start, end in edges:
            adj_list[start].add(end)
            adj_list[end].add(start)
            
        queue = []
        for node in range(n):
            if len(adj_list[node]) == 1:
                queue.append(node)
                
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(queue)
            new_queue = []
            while queue:
                leaf = queue.pop()
                neighbor = adj_list[leaf].pop()
                adj_list[neighbor].remove(leaf)
                if len(adj_list[neighbor]) == 1:
                    new_queue.append(neighbor)
            queue = new_queue
                    
        return queue


class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n <= 2:
            return [i for i in range(n)]
        
        neighbors = [set() for i in range(n)]
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)
            
        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)
                
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            while leaves:
                leaf = leaves.pop()
                neighbor = neighbors[leaf].pop()
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)
                    
            leaves = new_leaves
            
        return leaves


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertCountEqual(Solution().findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]), [3,4])
        self.assertCountEqual(Solution().findMinHeightTrees(1, []), [0])
        self.assertCountEqual(Solution().findMinHeightTrees(2, [[0,1]]), [0,1])


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Topological Sorting
######################################
# Let |V| be the number of nodes in the graph, then the number of edges would
# be |V| - 1 as specified in the problem.

# Time: O(|V|)
# - First, it takes |V|-1 iterations for us to construct a graph, given the
#   edges.
# - With the constructed graph, we retrieve the initial leaf nodes, which takes
#   |V| steps.
# - During the BFS trimming process, we will trim out almost all the nodes
#   (|V|) and edges (|V|-1) from the edges. Therefore, it would take us around
#   |V| + |V| - 1 operations to reach the centroids.
# - To sum up, the overall time complexity of the algorithm is O(|V|).

# Space: O(|V|)
# - We construct the graph with adjacency list, which has |V| nodes and |V|-1
#   edges. Therefore, we would need |V| + |V|-1 space for the representation of
#   the graph.
# - In addition, we use a queue to keep track of the leaf nodes. In the worst
#   case, the nodes form a star shape, with one centroid and the rest of the
#   nodes as leaf nodes. In this case, we would need |V|-1 space for the queue.
# - To sum up, the overall space complexity of the algorithm is also O(|V|).

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        # base cases
        if n <= 2:
            return [i for i in range(n)]

        # Build the graph with the adjacency list
        neighbors = [set() for i in range(n)]
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)

        # Initialize the first layer of leaves
        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)

        # Trim the leaves until reaching the centroids
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            # remove the current leaves along with the edges
            while leaves:
                leaf = leaves.pop()
                # the only neighbor left for the leaf node
                neighbor = neighbors[leaf].pop()
                # remove the only edge left
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)

            # prepare for the next round
            leaves = new_leaves

        # The remaining nodes are the centroids of the graph
        return leaves


