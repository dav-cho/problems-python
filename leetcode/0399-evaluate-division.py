##
#### Evaluate Division (medium)
###################################

# You are given an array of variable pairs equations and an array of real
# numbers values, where equations[i] = [Ai, Bi] and values[i] represent the
# equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a
# single variable.

# You are also given some queries, where queries[j] = [Cj, Dj] represents the
# jth query where you must find the answer for Cj / Dj = ?.

# Return the answers to all queries. If a single answer cannot be determined,
# return -1.0.

# Note: The input is always valid. You may assume that evaluating the queries
# will not result in division by zero and that there is no contradiction.

# Example 1:
# Input: equations = [["a","b"],["b","c"]],
#        values = [2.0,3.0],
#        queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [600000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation: 
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

# Example 2:
# Input: equations = [["a","b"],["b","c"],["bc","cd"]],
#        values = [1.5,2.5,5.0],
#        queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# Output: [3.75000,0.40000,5.00000,0.20000]

# Example 3:
# Input: equations = [["a","b"]],
#        values = [0.5],
#        queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
# Output: [0.50000,2.00000,-1.00000,-1.00000]
 
# Constraints:
# 1 <= equations.length <= 20
# equations[i].length == 2
# 1 <= Ai.length, Bi.length <= 5
# values.length == equations.length
# 0.0 < values[i] <= 20.0
# 1 <= queries.length <= 20
# queries[i].length == 2
# 1 <= Cj.length, Dj.length <= 5
# Ai, Bi, Cj, Dj consist of lower case English letters and digits.

################################################################################

## path search graph
##############################
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        graph = defaultdict(defaultdict)
        
        def backtrack(curr_node, target_node, acc_product, seen):
            seen.add(curr_node)
            ret = -1
            neighbors = graph[curr_node]
            if target_node in neighbors:
                ret = acc_product * neighbors[target_node]
            else:
                for neighbor, val in neighbors.items():
                    if neighbor in seen:
                        continue
                    ret = backtrack(neighbor, target_node, acc_product * val, seen)
                    if ret != -1:
                        break
                        
            seen.remove(curr_node)
            return ret
        
        for (dividend, divisor), val in zip(equations, values):
            graph[dividend][divisor] = val
            graph[divisor][dividend] = 1 / val
            
        results = []
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                ret = -1
            elif dividend == divisor:
                ret = 1
            else:
                seen = set()
                ret = backtrack(dividend, divisor, 1, seen)
            results.append(ret)
        
        return results


## union find (disjoing set)
##############################
class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        gid_weight = {}
        
        def find(node_id):
            if node_id not in gid_weight:
                gid_weight[node_id] = (node_id, 1)
            group_id, node_weight = gid_weight[node_id]
            
            if group_id != node_id:
                new_group_id, group_weight = find(group_id)
                gid_weight[node_id] = \
                    (new_group_id, node_weight * group_weight)
                
            return gid_weight[node_id]
        
        def union(dividend, divisor, val):
            dividend_gid, dividend_weight = find(dividend)
            divisor_gid, divisor_weight = find(divisor)
            if dividend_gid != divisor_gid:
                gid_weight[dividend_gid] = \
                    (divisor_gid, divisor_weight * val / dividend_weight)
        
        for (dividend, divisor), val in zip(equations, values):
            union(dividend, divisor, val)
            
        res = []
        for dividend, divisor in queries:
            if dividend not in gid_weight or divisor not in gid_weight:
                res.append(-1)
            else:
                dividend_gid, dividend_weight = find(dividend)
                divisor_gid, divisor_weight = find(divisor)
                if dividend_gid != divisor_gid:
                    res.append(-1)
                else:
                    res.append(dividend_weight / divisor_weight)
                    
        return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]), [6.00000,0.50000,-1.00000,1.00000,-1.00000])
        self.assertEqual(solution.calcEquation([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]), [3.75000,0.40000,5.00000,0.20000])
        self.assertEqual(solution.calcEquation([["a","b"]], [0.5], [["a","b"],["b","a"],["a","c"],["x","y"]]), [0.50000,2.00000,-1.00000,-1.00000])


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Path Search in Graph
#######################################
# Time: O(M⋅N)
# - First of all, we iterate through the equations to build a graph. Each
#   equation takes O(1) time to process. Therefore, this step will take O(N)
#   time in total.
# - For each query, we need to traverse the graph. In the worst case, we might
#   need to traverse the entire graph, which could take O(N). Hence, in total,
#   the evaluation of queries could take M \cdot \mathcal{O}(N) = \mathcal{O}(M \cdot N)M⋅O(N)=O(M⋅N).
# - To sum up, the overall time complexity of the algorithm is
#   O(N)+O(M⋅N)=O(M⋅N)

# Space: O(N)
# - We build a graph out the equations. In the worst case where there is no
#   overlapping among the equations, we would have N edges and 2N nodes in the
#   graph. Therefore, the sapce complexity of the graph is O(N+2N)=O(3N)=O(N).
# - Since we employ the recursion in the backtracking, we would consume
#   additional memory in the function call stack, which could amount to O(N)
#   space.
# - In addition, we used a set visited to keep track of the nodes we visited
#   during the backtracking. The space complexity of the visited set would be
#   O(N).
# - To sum up, the overall space complexity of the algorithm is
#   O(N)+O(N)+O(N)=O(N).
# - Not that we did not take into account the space needed to hold the results.
#   Otherwise, the total space complexity would be O(N+M).

# Let N be the number of input equations and M be the number of queries.

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(defaultdict)

        def backtrack_evaluate(curr_node, target_node, acc_product, visited):
            visited.add(curr_node)
            ret = -1.0
            neighbors = graph[curr_node]
            if target_node in neighbors:
                ret = acc_product * neighbors[target_node]
            else:
                for neighbor, value in neighbors.items():
                    if neighbor in visited:
                        continue
                    ret = backtrack_evaluate(
                        neighbor, target_node, acc_product * value, visited)
                    if ret != -1.0:
                        break
            visited.remove(curr_node)
            return ret

        # Step 1). build the graph from the equations
        for (dividend, divisor), value in zip(equations, values):
            # add nodes and two edges into the graph
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value

        # Step 2). Evaluate each query via backtracking (DFS)
        #  by verifying if there exists a path from dividend to divisor
        results = []
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                # case 1): either node does not exist
                ret = -1.0
            elif dividend == divisor:
                # case 2): origin and destination are the same node
                ret = 1.0
            else:
                visited = set()
                ret = backtrack_evaluate(dividend, divisor, 1, visited)
            results.append(ret)

        return results


## Approach 2: Union-Find with Weights
##########################################
# *If M operations, either Union or Find, are applied to N elements, the total
#  run time is O(M⋅log ∗ N), where log ∗ is the iterated logarithm.

# One can refer to the proof of Union-Find complexity for more details.

# In our case, the maximum number of elements in the Union-Find data structure
# is equal to twice of the number of equations, i.e. each equation introduces
# two new variables.

# Time: O((M+N)⋅log ∗ N)
# - First of all, we iterate through each input equation and invoke union()
#   upon it. As a result, the overall time complexity of this step is
#   O(N⋅log ∗ N).
# - As the second step, we then evaluate the query one by one. For each
#   evaluation, we invoke the find() function at most twice. Therefore, the
#   overall time complexity of this step is O(M⋅log ∗ N).
# - To sum up, the total time complexity of the algorithm is O((M+N)⋅log ∗ N).
# - Note, as compared to the DFS/BFS search approach, Union-Find data structure
#   is more efficient for the repetitive/redundant query scenario. Once we
#   evaluate a query with Union-Find, all the subsequent repetitive queries or
#   any query that has the overlapping with the previous query in terms of
#   variable group could be evaluated in constant time. For instance, in the
#   above example, once the query of a/c is evaluated, if later we want to
#   evaluate a/b, we could instantly obtain the states of variables a and b
#   without triggering the chain update again. While for DFS/BFS approaches, the
#   cost of evaluating each query is independent for each other.

# Space: O(N)
# - The space complexity of our Union-Find data structure is O(N) where we
#   maintain a state for each variable.
# - Since the find() function is implemented with recursion, there would be some
#   additional memory consumption in function call stack, which could amount to
#   O(N).
# - To sum up, the total space complexity of the algorithm is O(N)+O(N)=O(N).
# - Again, we did not take into account the space needed to hold the results.
#   Otherwise, the total space complexity would be O(N+M).

# Let N be the number of input equations and M be the number of queries.

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        gid_weight = {}

        def find(node_id):
            if node_id not in gid_weight:
                gid_weight[node_id] = (node_id, 1)
            group_id, node_weight = gid_weight[node_id]
            # The above statements are equivalent to the following one
            #group_id, node_weight = gid_weight.setdefault(node_id, (node_id, 1))

            if group_id != node_id:
                # found inconsistency, trigger chain update
                new_group_id, group_weight = find(group_id)
                gid_weight[node_id] = \
                    (new_group_id, node_weight * group_weight)
            return gid_weight[node_id]

        def union(dividend, divisor, value):
            dividend_gid, dividend_weight = find(dividend)
            divisor_gid, divisor_weight = find(divisor)
            if dividend_gid != divisor_gid:
                # merge the two groups together,
                # by attaching the dividend group to the one of divisor
                gid_weight[dividend_gid] = \
                    (divisor_gid, divisor_weight * value / dividend_weight)

        # Step 1). build the union groups
        for (dividend, divisor), value in zip(equations, values):
            union(dividend, divisor, value)

        results = []
        # Step 2). run the evaluation, with "lazy" updates in find() function
        for (dividend, divisor) in queries:
            if dividend not in gid_weight or divisor not in gid_weight:
                # case 1). at least one variable did not appear before
                results.append(-1.0)
            else:
                dividend_gid, dividend_weight = find(dividend)
                divisor_gid, divisor_weight = find(divisor)
                if dividend_gid != divisor_gid:
                    # case 2). the variables do not belong to the same chain/group
                    results.append(-1.0)
                else:
                    # case 3). there is a chain/path between the variables
                    results.append(dividend_weight / divisor_weight)
        return results


