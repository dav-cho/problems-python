##
#### Course Schedule II (medium)
########################################

# There are a total of numCourses courses you have to take, labeled from 0 to
# numCourses - 1. You are given an array prerequisites where
# prerequisites[i] = [a_i, b_i] indicates that you must take course b_i first
# if you want to take course a_i.

# For example, the pair [0, 1], indicates that to take course 0 you have to
# first take course 1.
# Return the ordering of courses you should take to finish all courses. If
# there are many valid answers, return any of them. If it is impossible to
# finish all courses, return an empty array.

# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

# Example 2:
# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

# Example 3:
# Input: numCourses = 1, prerequisites = []
# Output: [0]
 
# Constraints:
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= numCourses * (numCourses - 1)
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# ai != bi
# All the pairs [ai, bi] are distinct.

################################################################################

from collections import defaultdict, deque


## indegree
##############################
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj_list = defaultdict(list)
        indegree = {}
        for dst, src in prerequisites:
            adj_list[src].append(dst)
            indegree[dst] = indegree.get(dst, 0) + 1
            
        res = []
        queue = deque([x for x in range(numCourses) if x not in indegree])
        while queue:
            vertex = queue.popleft()
            res.append(vertex)
            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
                        
        return res if len(res) == numCourses else []


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj_list = defaultdict(list)
        indegree = defaultdict(int)
        for dst, src in prerequisites:
            adj_list[src].append(dst)
            indegree[dst] += 1
            
        res = []
        queue = deque([node for node in range(numCourses) if node not in indegree])
        while queue:
            vertex = queue.popleft()
            res.append(vertex)
            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
                        
        return res if len(res) == numCourses else []


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj_list = defaultdict(list)
        indegree = {}
        for dest, src in prerequisites:
            adj_list[src].append(dest)
            indegree[dest] = indegree.get(dest, 0) + 1
            
        queue = deque([k for k in range(numCourses) if k not in indegree])
        res = []
        while queue:
            vertex = queue.popleft()
            res.append(vertex)
            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
                        
        return res if len(res) == numCourses else []


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj_list = defaultdict(list)
        indegree = {}
        for dest, src in prerequisites:
            adj_list[src].append(dest)
            indegree[dest] = indegree.get(dest, 0) + 1
            
        zero_indegree_queue = deque([k for k in range(numCourses) if k not in indegree])
        topological_sorted_order = []
        while zero_indegree_queue:
            vertex = zero_indegree_queue.popleft()
            topological_sorted_order.append(vertex)
            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        zero_indegree_queue.append(neighbor)
                        
        return topological_sorted_order if len(topological_sorted_order) == numCourses else []


## dfs
##############################
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        res = []
        is_possible = True
        color = {k: 1 for k in range(numCourses)}
        adj_list = defaultdict(list)
        for dest, src in prerequisites:
            adj_list[src].append(dest)
            
        def dfs(node):
            nonlocal is_possible
            if not is_possible:
                return
            
            color[node] = 2
            
            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == 1:
                        dfs(neighbor)
                    elif color[neighbor] == 2:
                        is_possible = False
                        
            color[node] = 3
            res.append(node)
            
        for vertex in range(numCourses):
            if color[vertex] == 1:
                dfs(vertex)
                
        return res[::-1] if is_possible else []


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        WHITE = 1
        GRAY = 2
        BLACK = 3
        
        topological_sorted_order  = []
        is_possible = True
        color = {k: WHITE for k in range(numCourses)}
        adj_list = defaultdict(list)
        for dest, src in prerequisites:
            adj_list[src].append(dest)
            
        def dfs(node):
            nonlocal is_possible
            if not is_possible:
                return
            
            color[node] = GRAY
            
            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == WHITE:
                        dfs(neighbor)
                    elif color[neighbor] == GRAY:
                        is_possible = False
            
            color[node] = BLACK
            topological_sorted_order.append(node)
            
        for vertex in range(numCourses):
            if color[vertex] == WHITE:
                dfs(vertex)
                
        return topological_sorted_order[::-1] if is_possible else []


class Solution:
    WHITE = 1
    GRAY = 2
    BLACK = 3
        
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj_list = defaultdict(list)
        for dest, src in prerequisites:
            adj_list[src].append(dest)
            
        topological_sorted_order  = []
        is_possible = True
        color = {k: Solution.WHITE for k in range(numCourses)}
        
        def dfs(node):
            nonlocal is_possible
            if not is_possible:
                return
            
            color[node] = Solution.GRAY
            
            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == Solution.WHITE:
                        dfs(neighbor)
                    elif color[neighbor] == Solution.GRAY:
                        is_possible = False
            
            color[node] = Solution.BLACK
            topological_sorted_order.append(node)
            
        for vertex in range(numCourses):
            if color[vertex] == Solution.WHITE:
                dfs(vertex)
                
        return topological_sorted_order[::-1] if is_possible else []


## kahn's algorithm
##############################
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        res = [0] * numCourses
        if numCourses == 0:
            return res

        if not prerequisites:
            res = [i for i in range(numCourses)]
            return res

        indegree = [0] * numCourses
        zero_degree = deque()
        for pre in prerequisites:
            indegree[pre[0]] += 1
        for i in range(len(indegree)):
            if indegree[i] == 0:
                zero_degree.append(i)
        if not zero_degree:
            return []

        i = 0
        while zero_degree:
            course = zero_degree.popleft()
            res[i] = course
            i += 1
            for pre in prerequisites:
                if pre[1] == course:
                    indegree[pre[0]] -= 1
                    if indegree[pre[0]] == 0:
                        zero_degree.append(pre[0])

        if any(i for i in indegree):
            return []

        return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertCountEqual(Solution().findOrder(2, [[1,0]]), [0,1])
        self.assertCountEqual(Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]]), [0,2,1,3])
        self.assertCountEqual(Solution().findOrder(1, []), [0])


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Using Depth First Search
###########################################
# Time: O(V + E)
# - Where V represents the number of vertices and E represents the number of
#   edges. Essentially we iterate through each node and each vertex in the
#   graph once and only once.

# Space: O(V + E)
# - We use the adjacency list to represent our graph initially. The space
#   occupied is defined by the number of edges because for each node as the key,
#   we have all its adjacent nodes in the form of a list as the value.
#   Hence, O(E)
# - Additionally, we apply recursion in our algorithm, which in worst case will
#   incur O(E) extra space in the function call stack.
# - To sum up, the overall space complexity is O(V + E).

from collections import defaultdict
class Solution:

    WHITE = 1
    GRAY = 2
    BLACK = 3

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        # Create the adjacency list representation of the graph
        adj_list = defaultdict(list)

        # A pair [a, b] in the input represents edge from b --> a
        for dest, src in prerequisites:
            adj_list[src].append(dest)

        topological_sorted_order = []
        is_possible = True

        # By default all vertces are WHITE
        color = {k: Solution.WHITE for k in range(numCourses)}
        def dfs(node):
            nonlocal is_possible

            # Don't recurse further if we found a cycle already
            if not is_possible:
                return

            # Start the recursion
            color[node] = Solution.GRAY

            # Traverse on neighboring vertices
            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == Solution.WHITE:
                        dfs(neighbor)
                    elif color[neighbor] == Solution.GRAY:
                         # An edge to a GRAY vertex represents a cycle
                        is_possible = False

            # Recursion ends. We mark it as black
            color[node] = Solution.BLACK
            topological_sorted_order.append(node)

        for vertex in range(numCourses):
            # If the node is unprocessed, then call dfs on it.
            if color[vertex] == Solution.WHITE:
                dfs(vertex)

        return topological_sorted_order[::-1] if is_possible else []


## Approach 2: Using Node Indegree
######################################
# Time: O(V + E)
# - Where V represents the number of vertices and E represents the number of
#   edges. We pop each node exactly once from the zero in-degree queue and that
#   gives us V. Also, for each vertex, we iterate over its adjacency list and
#   in totality, we iterate over all the edges in the graph which gives us E.
#   Hence, O(V + E).
# Space: O(V + E)
# - We use an intermediate queue data structure to keep all the nodes with 0
#   in-degree. In the worst case, there won't be any prerequisite relationship
#   and the queue will contain all the vertices initially since all of them will
#   have 0 in-degree. That gives us O(V). Additionally, we also use the
#   adjacency list to represent our graph initially. The space occupied is
#   defined by the number of edges because for each node as the key, we have
#   all its adjacent nodes in the form of a list as the value. Hence, O(E).
#   So, the overall space complexity is O(V + E).

from collections import defaultdict, deque
class Solution:

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        # Prepare the graph
        adj_list = defaultdict(list)
        indegree = {}
        for dest, src in prerequisites:
            adj_list[src].append(dest)

            # Record each node's in-degree
            indegree[dest] = indegree.get(dest, 0) + 1

        # Queue for maintainig list of nodes that have 0 in-degree
        zero_indegree_queue = deque([k for k in range(numCourses) if k not in indegree])

        topological_sorted_order = []

        # Until there are nodes in the Q
        while zero_indegree_queue:

            # Pop one node with 0 in-degree
            vertex = zero_indegree_queue.popleft()
            topological_sorted_order.append(vertex)

            # Reduce in-degree for all the neighbors
            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indegree[neighbor] -= 1

                    # Add neighbor to Q if in-degree becomes 0
                    if indegree[neighbor] == 0:
                        zero_indegree_queue.append(neighbor)

        return topological_sorted_order if len(topological_sorted_order) == numCourses else []


## Approach 3: 
##############################
# Time: 
# Space: 


