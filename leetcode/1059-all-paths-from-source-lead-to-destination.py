##
#### All Paths from Source Lead to Destination (medium)
###########################################################

# Given the edges of a directed graph where edges[i] = [ai, bi] indicates there
# is an edge between nodes ai and bi, and two nodes source and destination of
# this graph, determine whether or not all paths starting from source
# eventually, end at destination, that is:

# At least one path exists from the source node to the destination node
# If a path exists from the source node to a node with no outgoing edges, then
# that node is equal to destination.
# The number of possible paths from source to destination is a finite number.
# Return true if and only if all roads from source lead to destination.

# Example 1:
# Input: n = 3, edges = [[0,1],[0,2]], source = 0, destination = 2
# Output: false
# Explanation: It is possible to reach and get stuck on both node 1 and node 2.

# Example 2:
# Input: n = 4, edges = [[0,1],[0,3],[1,2],[2,1]], source = 0, destination = 3
# Output: false
# Explanation: We have two possibilities: to end at node 3, or to loop over
# node 1 and node 2 indefinitely.

# Example 3:
# Input: n = 4, edges = [[0,1],[0,2],[1,3],[2,3]], source = 0, destination = 3
# Output: true

# Example 4:
# Input: n = 3, edges = [[0,1],[1,1],[1,2]], source = 0, destination = 2
# Output: false
# Explanation: All paths from the source node end at the destination node, but
# there are an infinite number of paths, such as
# 0-1-2, 0-1-1-2, 0-1-1-1-2, 0-1-1-1-1-2, and so on.

# Example 5:
# Input: n = 2, edges = [[0,1],[1,1]], source = 0, destination = 1
# Output: false
# Explanation: There is infinite self-loop at destination node.
 
# Constraints:
# 1 <= n <= 104
# 0 <= edges.length <= 104
# edges.length == 2
# 0 <= ai, bi <= n - 1
# 0 <= source <= n - 1
# 0 <= destination <= n - 1
# The given graph may have self-loops and parallel edges.

################################################################################

## dfs
##############################
class Solution:
    GRAY = 1
    BLACK = 2

    def leadsToDestination(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph = self.build_digraph(n, edges)
        return self.leads_to_dest(graph, source, destination, [None] * n)
    
    def leads_to_dest(self, graph, node, dest, states):
        if states[node] != None:
            return states[node] == Solution.BLACK
        
        if len(graph[node]) == 0:
            return node == dest
        
        states[node] = Solution.GRAY
        
        for next_node in graph[node]:
            if not self.leads_to_dest(graph, next_node, dest, states):
                return False
            
        states[node] = Solution.BLACK
        
        return True
    
    def build_digraph(self, n, edges):
        graph = [[] for _ in range(n)]
        for x, y in edges:
            graph[x].append(y)
        
        return graph


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.leadsToDestination(3, [[0,1],[0,2]], 0, 2), False)
        self.assertEqual(solution.leadsToDestination(4, [[0,1],[0,3],[1,2],[2,1]], 0, 3), False)
        self.assertEqual(solution.leadsToDestination(4, [[0,1],[0,2],[1,3],[2,3]], 0, 3), True)
        self.assertEqual(solution.leadsToDestination(3, [[0,1],[1,1],[1,2]], 0, 2), False)
        self.assertEqual(solution.leadsToDestination(2, [[0,1],[1,1]], 0, 1), False)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Depth First Search
#####################################
# Time: O(V)
# - Typically for an entire DFS over an input graph, it takes O(V + E) where V
#   represents the number of vertices in the graph and likewise, E represents
#   the number of edges in the graph. In the worst case E can be O(V^2) in case
#   each vertex is connected to every other vertex in the graph. However even
#   in the worst case, we will end up discovering a cycle very early on and
#   prune the recursion tree. If we were to traverse the entire graph, then the
#   complexity would be O(V^2) as the O(E) part would dominate. However, due to
#   pruning and backtracking in case of cycle detection, we end up with an
#   overall time complexity of O(V).
# Space: O(V + E)
# - Where O(E) is occupied by the adjacency list and O(V) is occupied by the
#   recursion stack and the color states.

class Solution:
    
    # We don't use the state WHITE as such anywhere. Instead, the "null" value in the states array below is a substitute for WHITE.
    GRAY = 1
    BLACK = 2

    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = self.buildDigraph(n, edges)
        return self.leadsToDest(graph, source, destination, [None] * n)
        
    def leadsToDest(self, graph, node, dest, states):
        
        # If the state is GRAY, this is a backward edge and hence, it creates a Loop.
        if states[node] != None:
            return states[node] == Solution.BLACK
        
        # If this is a leaf node, it should be equal to the destination.
        if len(graph[node]) == 0:
            return node == dest
        
        # Now, we are processing this node. So we mark it as GRAY.
        states[node] = Solution.GRAY
        
        for next_node in graph[node]:
            
            # If we get a `false` from any recursive call on the neighbors, we short circuit and return from there.
            if not self.leadsToDest(graph, next_node, dest, states):
                return False;
        
        # Recursive processing done for the node. We mark it BLACK.
        states[node] = Solution.BLACK
        return True
        
    def buildDigraph(self, n, edges):
        graph = [[] for _ in range(n)]
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            
        return graph


## Approach 2: 
##############################
# Time: 
# Space: 


## Approach 3: 
##############################
# Time: 
# Space: 


