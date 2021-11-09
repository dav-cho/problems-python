##
#### Optimize Water Distribution in a Village (hard)
########################################################

# There are n houses in a village. We want to supply water for all the houses
# by building wells and laying pipes.

# For each house i, we can either build a well inside it directly with cost
# wells[i - 1] (note the -1 due to 0-indexing), or pipe in water from another
# well to it. The costs to lay pipes between houses are given by the array
# pipes, where each pipes[j] = [house1j, house2j, costj] represents the cost to
# connect house1j and house2j together using a pipe. Connections are
# bidirectional.

# Return the minimum total cost to supply water to all houses.

# Example 1:
# Input: n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]
# Output: 3
# Explanation: 
# The image shows the costs of connecting houses using pipes.
# The best strategy is to build a well in the frst house with cost 1 and connect the other houses to it with cost 2 so the total cost is 3.

# Example 2:
# Input: n = 2, wells = [1,1], pipes = [[1,2,1]]
# Output: 2
 
# Constraints:
# 2 <= n <= 104
# wells.length == n
# 0 <= wells[i] <= 105
# 1 <= pipes.length <= 104
# pipes[j].length == 3
# 1 <= house1_j, house2_j <= n
# 0 <= costj <= 105
# house1_j != house2_j

################################################################################

import heapq
from collections import defaultdict


## prim's algorithm w/ heap
###############################
class Solution:
    def minCostToSupplyWater(self, n: int, wells: list[int], pipes: list[list[int]]) -> int:
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
    def minCostToSupplyWater(self, n: int, wells: list[int], pipes: list[list[int]]) -> int:
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
    def minCostToSupplyWater(self, n: int, wells: list[int], pipes: list[list[int]]) -> int:
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
    def minCostToSupplyWater(self, n: int, wells: list[int], pipes: list[list[int]]) -> int:
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
    def minCostToSupplyWater(self, n: int, wells: list[int], pipes: list[list[int]]) -> int:
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
    def minCostToSupplyWater(self, n: int, wells: list[int], pipes: list[list[int]]) -> int:
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


## 
##############################
class Solution:
    def minCostToSupplyWater(self, n: int, wells: list[int], pipes: list[list[int]]) -> int:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.minCostToSupplyWater(3, [1,2,2], [[1,2,1],[2,3,1]]), 3)
        self.assertEqual(solution.minCostToSupplyWater(2, [1,1], [[1,2,1]]), 2)

if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Prim's Algorithm with Heap
#############################################
# Time: O((N+M)⋅log(N+M))
# - To build the graph, we iterate through the houses and pipes in the input,
#   which takes O(N+M) time.
# - While building the MST, we might need to iterate through all the edges in
#   the graph in the worst case, which amounts to N+M in total. For each edge,
#   it would enter and exit the heap data structure at most once. The enter of
#   edge into heap (i.e. push operation) takes log(N+M) time, while the exit of
#   edge (i.e. pop operation) takes a constant time. Therefore, the time
#   complexity of the MST construction process is O((N+M)⋅log(N+M)).
# - To sum up, the overall time complexity of the algorithm is O\big( (N+M) \cdot \log(N+M) \big)O((N+M)⋅log(N+M)).

# Space: O(N+M)O(N+M)
# - We break down the analysis accordingly into the three major data structures
#   that we used in the algorithm.
# - The graph that we built consists of N+1 vertices and 2⋅M edges (i.e. pipes
#   are bidirectional). Therefore, the space complexity of graph is
#   O(N+1+2⋅M)=O(N+M).
# - The space complexity of the set that is used to hold the vertices in MST is
#   O(N).
# - Finally, in the worst case, the heap we used might hold all the edges in the
#   graph which is (N+M).
# - To summarize, the overall space complexity of the algorithm is O(N+M).

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:

        # bidirectional graph represented in adjacency list
        graph = defaultdict(list)

        # add a virtual vertex indexed with 0.
        #   then add an edge to each of the house weighted by the cost
        for index, cost in enumerate(wells):
            graph[0].append((cost, index + 1))

        # add the bidirectional edges to the graph
        for house_1, house_2, cost in pipes:
            graph[house_1].append((cost, house_2))
            graph[house_2].append((cost, house_1))

        # A set to maintain all the vertex that has been added to
        #   the final MST (Minimum Spanning Tree),
        #   starting from the vertex 0.
        mst_set = set([0])

        # heap to maitain the order of edges to be visited,
        #   starting from the edges originated from the vertex 0.
        # Note: we can start arbitrarily from any node.
        heapq.heapify(graph[0])
        edges_heap = graph[0]

        total_cost = 0
        while len(mst_set) < n + 1:
            cost, next_house = heapq.heappop(edges_heap)
            if next_house not in mst_set:
                # adding the new vertex into the set
                mst_set.add(next_house)
                total_cost += cost
                # expanding the candidates of edge to choose from
                #   in the next round
                for new_cost, neighbor_house in graph[next_house]:
                    if neighbor_house not in mst_set:
                        heapq.heappush(edges_heap, (new_cost, neighbor_house))

        return total_cost


## Approach 2: Kruskal's Algorithm with Union-Find
######################################################
# Time: O((N+M)⋅log(N+M))
# - First, we build a list of edges, which takes O(N+M) time.
# - We then sort the list of edges, which takes O((N+M)⋅log(N+M)) time.
# - At the end, we iterate through the sorted edges. For each iteration, we
#   invoke a Union-Find operation. Hence, the time complexity for iteration is
#   O((N+M)∗log ∗ (N)).
# - To sum up, the overall time complexity of the algorithm is O((N+M)⋅log(N+M))
#   which is dominated by the sorting step.

# Space: O(N+M)
# - The space complexity of our Union-Find data structure is O(N).
# - The space required by the list of edges is O(N+M).
# - Finally, the space complexity of the sorting algorithm depends on the
#   implementation of each programming language. For instance, the list.sort()
#   function in Python is implemented with the Timsort algorithm whose space
#   complexity is O(n) where n is the number of the elements. While in Java, the
#   Collections.sort() is implemented as a variant of quicksort algorithm whose
#   space complexity is O(logn).
# - To sum up, the overall space complexity of the algorithm is O(N+M) which is
#   dominated by the list of edges.

# Let N be the number of houses, and M be the number of pipes from the input.

# If K operations, either Union or Find, are applied to L elements, the total
# run time is O(K⋅log* L), where log* is the iterated logarithm.

# One can refer to the proof of Union-Find complexity and the tutorial from
# Princeton University for more details.

class UnionFind:
    """
        Implementation of UnionFind without load-balancing.
    """
    def __init__(self, size) -> None:
        """
        container to hold the group id for each member
        Note: the index of member starts from 1,
            thus we add one more element to the container.
        """
        self.group = [i for i in range(size + 1)]
        # the rank of each node for later rebalancing
        self.rank = [0] * (size + 1)

    def find(self, person: int) -> int:
        """
            return the group id that the person belongs to
        """
        if self.group[person] != person:
            self.group[person] = self.find(self.group[person])
        return self.group[person]

    def union(self, person_1: int, person_2: int) -> bool:
        """
            Join the groups together.
            return:
                false when the two persons belong to the same group already,
                otherwise true
        """
        group_1 = self.find(person_1)
        group_2 = self.find(person_2)
        if group_1 == group_2:
            return False

        # attach the group of lower rank to the group with higher rank
        if self.rank[group_1] > self.rank[group_2]:
            self.group[group_2] = group_1
        elif self.rank[group_1] < self.rank[group_2]:
            self.group[group_1] = group_2
        else:
            self.group[group_1] = group_2
            self.rank[group_2] += 1

        return True


class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        ordered_edges = []
        # add the virtual vertex (index with 0) along with the new edges.
        for index, weight in enumerate(wells):
            ordered_edges.append((weight, 0, index+1))

        # add the existing edges
        for house_1, house_2, weight in pipes:
            ordered_edges.append((weight, house_1, house_2))

        # sort the entire edges by their weights
        ordered_edges.sort(key=lambda x: x[0])

        # iterate through the ordered edges
        uf = UnionFind(n)
        total_cost = 0
        for cost, house_1, house_2 in ordered_edges:
            # determine if we should add the new edge to the final MST
            if uf.union(house_1, house_2):
                total_cost += cost

        return total_cost


