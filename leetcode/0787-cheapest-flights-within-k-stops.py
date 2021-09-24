##
#### Cheapest Flights Within K Stops (medium)
#################################################

# There are n cities connected by some number of flights. You are given an array
# flights where flights[i] = [fromi, toi, pricei] indicates that there is a
# flight from city fromi to city toi with cost pricei.

# You are also given three integers src, dst, and k, return the cheapest price
# from src to dst with at most k stops. If there is no such route, return -1.

# Example 1:
# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
# Output: 200
# Explanation: The graph is shown.
# The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as
# marked red in the picture.

# Example 2:
# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
# Output: 500
# Explanation: The graph is shown.
# The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
 
# Constraints:
# 1 <= n <= 100
# 0 <= flights.length <= (n * (n - 1) / 2)
# flights[i].length == 3
# 0 <= fromi, toi < n
# fromi != toi
# 1 <= pricei <= 104
# There will not be any multiple flights between two cities.
# 0 <= src, dst, k < n
# src != dst

################################################################################

## dijkstra's algorithm
##############################
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        adj_matrix = [[0] * n for _ in range(n)]
        for s, d, cost in flights:
            adj_matrix[s][d] = cost
            
        dist = {node: float('inf') for node in range(n)}
        stops = {node: float('inf') for node in range(n)}
        dist[src] = stops[src] = 0
        min_heap = [(0, 0, src)]
        
        while min_heap:
            curr_cost, curr_stops, node = heapq.heappop(min_heap)
            
            if node == dst:
                return curr_cost
            if curr_stops > k:
                continue
                
            for neighbor in range(n):
                cost = adj_matrix[node][neighbor]

                if cost <= 0:
                    continue
                
                if curr_cost + cost < dist[neighbor]:
                    dist[neighbor] = curr_cost + cost
                    heapq.heappush(min_heap, (curr_cost + cost, curr_stops + 1, neighbor))
                if curr_stops < stops[neighbor]:
                    heapq.heappush(min_heap, (curr_cost + cost, curr_stops + 1, neighbor))
                    
                stops[neighbor] = curr_stops
                    
        return dist[dst] if dist[dst] < float('inf') else -1


class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        adj_matrix = [[0] * n for _ in range(n)]
        for s, d, cost in flights:
            adj_matrix[s][d] = cost
            
        dist = [float('inf')] * n
        stops = [float('inf')] * n
        dist[src] = stops[src] = 0
        min_heap = [(0, 0, src)]
        
        while min_heap:
            curr_cost, curr_stops, node = heapq.heappop(min_heap)
            
            if node == dst:
                return curr_cost
            if curr_stops > k:
                continue
                
            for neighbor in range(n):
                if adj_matrix[node][neighbor] == 0:
                    continue
                    
                cost = adj_matrix[node][neighbor]
                
                if curr_cost + cost < dist[neighbor]:
                    dist[neighbor] = curr_cost + cost
                    heapq.heappush(min_heap, (curr_cost + cost, curr_stops + 1, neighbor))
                if curr_stops < stops[neighbor]:
                    heapq.heappush(min_heap, (curr_cost + cost, curr_stops + 1, neighbor))
                    
                stops[neighbor] = curr_stops
                
        return dist[dst] if dist[dst] != float('inf') else -1


class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        adj_matrix = [[0] * n for _ in range(n)]
        for node, neighbor, cost in flights:
            adj_matrix[node][neighbor] = cost
            
        dist = [float('inf')] * n
        stops = [float('inf')] * n
        dist[src], stops[src] = 0, 0
        min_heap = [(0, 0, src)]
        
        while min_heap:
            curr_cost, curr_stops, node = heapq.heappop(min_heap)
            if node == dst:
                return curr_cost
            if curr_stops > k:
                continue

            for neighbor in range(n):
                if adj_matrix[node][neighbor] == 0:
                    continue
                    
                dU = curr_cost
                dV = dist[neighbor]
                wUV = adj_matrix[node][neighbor]
                
                if dU + wUV < dV:
                    dist[neighbor] = dU + wUV
                    heapq.heappush(min_heap, (dU + wUV, curr_stops + 1, neighbor))
                elif curr_stops < stops[neighbor]:
                    heapq.heappush(min_heap, (dU + wUV, curr_stops + 1, neighbor))
                    
                stops[neighbor] = curr_stops
                
        return dist[dst] if dist[dst] < float('inf') else -1


## dfs with memoization
##############################
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        def dfs(node, stops):
            if node == dst:
                return 0
            if stops < 0:
                return float('inf')
            if (node, stops) in memo:
                return memo[(node, stops)]
            
            res = float('inf')
            
            for neighbor in range(n):
                cost = adj_matrix[node][neighbor]

                if cost > 0:
                    res = min(res, dfs(neighbor, stops - 1) + cost)
                    
            memo[(node, stops)] = res
            
            return res
        
        adj_matrix = [[0] * n for _ in range(n)]
        memo = {}
        
        for s, d, cost in flights:
            adj_matrix[s][d] = cost
            
        res = dfs(src, k)
        
        return res if res < float('inf') else -1


class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        def dfs(node, stops):
            if node == dst:
                return 0
            if stops < 0:
                return float('inf')
            if (node, stops) in memo:
                return memo[(node, stops)]
            
            res = float('inf')
            
            for neighbor in range(n):
                if adj_matrix[node][neighbor] > 0:
                    res = min(res, dfs(neighbor, stops - 1) + adj_matrix[node][neighbor])
                    
            memo[(node, stops)] = res
            
            return res
        
        adj_matrix = [[0] * n for _ in range(n)]
        memo = {}
        
        for s, d, cost in flights:
            adj_matrix[s][d] = cost
            
        res = dfs(src, k)
        
        return res if res < float('inf') else -1


class Solution:
    def find_shortest(self, node, stops, dst, n):
        if node == dst:
            return 0
        if stops < 0:
            return float('inf')
        if (node, stops) in self.memo:
            return self.memo[(node, stops)]
        
        res = float('inf')
        
        for neighbor in range(n):
            if self.adj_matrix[node][neighbor] > 0:
                res = min(res, self.find_shortest(neighbor, stops - 1, dst, n) + self.adj_matrix[node][neighbor])
                
        self.memo[(node, stops)] = res
        
        return res
    
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        self.adj_matrix = [[0] * n for _ in range(n)]
        self.memo = {}
        
        for s, d, cost in flights:
            self.adj_matrix[s][d] = cost
            
        res = self.find_shortest(src, k, dst, n)
        
        return res if res < float('inf') else -1


class Solution:
    def __init__(self):
        self.adj_matrix = None
        self.memo = {}
        
    def find_shortest(self, node, stops, dst, n):
        if node == dst:
            return 0
        if stops < 0:
            return float('inf')
        if (node, stops) in self.memo:
            return self.memo[(node, stops)]
        
        res = float('inf')
        
        for neighbor in range(n):
            if self.adj_matrix[node][neighbor] > 0:
                res = min(res, self.find_shortest(neighbor, stops - 1, dst, n) + self.adj_matrix[node][neighbor])
                
        self.memo[(node, stops)] = res
        
        return res
    
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        self.adj_matrix = [[0] * n for _ in range(n)]
        
        for s, d, cost in flights:
            self.adj_matrix[s][d] = cost
            
        res = self.find_shortest(src, k, dst, n)
        
        return res if res < float('inf') else -1


## bellman-ford algorithm
##############################
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        dist = {node: [float('inf')] * n for node in range(n)}
        dist[0][src] = dist[1][src] = 0
        
        for iteration in range(k + 1):
            for s, d, curr_cost in flights:
                cost = dist[~iteration & 1][s]
                
                if curr_cost + cost < dist[iteration & 1][d]:
                    dist[iteration & 1][d] = curr_cost + cost
        
        res = dist[k & 1][dst]
        
        return res if res < float('inf') else -1


class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        if src == dst:
            return 0
        
        prev = [float('inf')] * n
        curr = [float('inf')] * n
        prev[src] = 0
        
        for iteration in range(k + 1):
            prev[src] = 0
            
            for s, d, cost in flights:
                if prev[s] < float('inf'):
                    curr[d] = min(curr[d], prev[s] + cost)
                    
            prev = curr.copy()
                    
        return curr[dst] if curr[dst] < float('inf') else -1


class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        if src == dst:
            return 0

        prev = [float('inf')] * n
        curr = [float('inf')] * n
        prev[src] = 0
        
        for iteration in range(k + 1):
            prev[src] = 0
            
            for source, dest, cost in flights:
                if prev[source] < float('inf'):
                    curr[dest] = min(curr[dest], prev[source] + cost)
                    
            prev = curr.copy()
            
        return curr[dst] if curr[dst] < float('inf') else -1


class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        if src == dst:
            return 0
        
        INF = sys.maxsize
        prev = [INF] * n
        curr = [INF] * n
        prev[src] = 0
        
        for i in range(1, k + 2):
            curr[src] = 0
            
            for prev_flight, curr_flight, cost in flights:
                if prev[prev_flight] < INF:
                    curr[curr_flight] = min(curr[curr_flight], prev[prev_flight] + cost)
            
            prev = curr.copy()
            
        return  curr[dst] if curr[dst] < float('inf') else -1


class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        dist = {node: [float('inf')] * n for node in range(n)}
        dist[0][src] = dist[1][src] = 0
        
        for iteration in range(k + 1):
            for s, d, curr_cost in flights:
                cost = dist[1 - iteration & 1][s]
                
                if curr_cost + cost < dist[iteration & 1][d]:
                    dist[iteration & 1][d] = curr_cost + cost
                    
        return dist[k & 1][dst] if dist[k & 1][dst] < float('inf') else -1


class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        dist = {node: [float('inf')] * n for node in range(n)}
        dist[0][src] = dist[1][src] = 0
        
        for iteration in range(k + 1):
            for source, destination, curr_cost in flights:
                cost = dist[1 - iteration & 1][source]
                
                if curr_cost + cost < dist[iteration & 1][destination]:
                    dist[iteration & 1][destination] = curr_cost + cost
                    
        res = dist[k & 1][dst]
        return res if res < float('inf') else -1


class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        distances = [[float('inf')] * n for _ in range(n)]
        distances[0][src] = distances[1][src] = 0
        
        for iteration in range(k + 1):
            for u, v, wUV in flights:
                dU = distances[1 - iteration & 1][u]
                dV = distances[iteration & 1][v]
                
                if dU + wUV < dV:
                    distances[iteration & 1][v] = dU + wUV
                    
        return distances[k & 1][dst] if distances[k & 1][dst] < float('inf') else -1


## bfs
##############################
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1), 200)
        self.assertEqual(solution.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0), 500)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Dijkstra's Algorithm
#######################################
# Time: O(V^2 ⋅logV)
# - Let E represent the number of flights and V represent the number of cities.
#   The time complexity is mainly governed by the number of times we pop and
#   push into the heap. We will process each node (city) atleast once and for
#   each city popped from the queue, we iterate over its adjacency matrix and
#   can potentially add all its neighbors to the heap. Thus, the time taken for
#   extract min and then addition to the heap (or simply, heap replace) would be
#   O(V^2 ⋅logV).
#       - Let's talk a bit more about the implementation of Dijkstra's here.
#         The traditional algorithm is not exactly written the way we've
#         explained above.
#       - The traditional algorithm adds all the nodes into the heap with the
#         source having a distance value of 0 and all others having a value inf.
#       - When we process the neighbors of a node and find that a particular
#         neighbor can be reached in a shorter distance (or lesser number of
#         stops), we update its value in the heap. In our implementation, we
#         add a new node with updated values rather than updating the value of
#         the existing node. To do that, we will need another dictionary that
#         will probably keep the index location for a node in the heap or
#         something like that. This would be necessary because a heap is not a
#         binary search tree and it doesn't have any search properties for
#         quick search and updates.
#       - If we keep the number of nodes in the heap fixed to V, then the
#         complexity would be O((V+E)⋅logV). Granted, in our case, the heap
#         might contain more than V nodes at some point due to the same city
#         being added multiple times. Therefore, the complexity would be
#         slightly more. That is not being accounted for here since that is an
#         implementation detail and not necessary for the algorithm we
#         discussed here.
#       - Yet another point to keep in mind here is that we are using an
#         adjacency matrix rather than adjacency list here. The typical
#         Dijkstra's algorithm would use an adjacency list and that brings down
#         the complexity slightly because you don't "check" if a connection
#         exists or not unlike in adjacency matrix. However, since the number
#         of nodes are very less for this problem, we preferred to take the
#         route of adjacency matrix as that gives us sequential access to
#         elements and leads to speed-ups due to cache localization.

# Space: O(V^2)
# - O(V) is occupied by the two dictionaries and also by the heap and V^2 by the
#   adjacency matrix structure. As mentioned above, there might be duplicate
#   cities in the heap with different distances and number of stops due to our
#   implementation. But we are not taking that into consideration here. This is
#   the space complexity of the traditional Dijkstra's and it doesn't change
#   with the algorithm modifications (not the implementation modifications)
#   we've done here.

import heapq

class Solution:
    
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        # Build the adjacency matrix
        adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
        for s, d, w in flights:
            adj_matrix[s][d] = w
            
        # Shortest distances array
        distances = [float("inf") for _ in range(n)]
        current_stops = [float("inf") for _ in range(n)]
        distances[src], current_stops[src] = 0, 0
        
        # Data is (cost, stops, node)
        minHeap = [(0, 0, src)]     
        
        while minHeap:
            
            cost, stops, node = heapq.heappop(minHeap)
            
            # If destination is reached, return the cost to get here
            if node == dst:
                return cost
            
            # If there are no more steps left, continue 
            if stops == K + 1:
                continue
             
            # Examine and relax all neighboring edges if possible 
            for nei in range(n):
                if adj_matrix[node][nei] > 0:
                    dU, dV, wUV = cost, distances[nei], adj_matrix[node][nei]
                    
                    # Better cost?
                    if dU + wUV < dV:
                        distances[nei] = dU + wUV
                        heapq.heappush(minHeap, (dU + wUV, stops + 1, nei))
                    elif stops < current_stops[nei]:
                        #  Better steps?
                        heapq.heappush(minHeap, (dU + wUV, stops + 1, nei))
                        
                    current_stops[nei] = stops
            
        return -1 if distances[dst] == float("inf") else distances[dst]


## Approach 2: Depth-First-Search with Memoization
######################################################
# Time: O(V^2 ⋅K)
# - The time complexity for a recursive solution is defined by the number of
#   recursive calls we make and the time it takes to process one recursive
#   call. The number of recursive calls we can potentially make is O(V⋅K). In
#   each recursive call, we iterate over a given node's neighbors. That takes
#   time O(V) because we are using an adjacency matrix. Thus, the overall time
#   complexity is O(V^2 ⋅K).

# Space: O(V⋅K+V^2)
# - Where O(V⋅K) is occupied by the memo dictionary and the rest by the
#   adjacency matrix structure we build in the beginning.

class Solution:
    
    def __init__(self):
        self.adj_matrix = None
        self.memo = {}
    
    def findShortest(self, node, stops, dst, n):
            
        # No need to go any further if the destination is reached    
        if node == dst:
            return 0
        
        # Can't go any further if no stops left
        if stops < 0:
            return float("inf")
        
        # If the result of this state is already cached, return it
        if (node, stops) in self.memo:
            return self.memo[(node, stops)]
        
        # Recursive calls over all the neighbors
        ans = float("inf")
        for neighbor in range(n):
            if self.adj_matrix[node][neighbor] > 0:
                ans = min(ans, self.findShortest(neighbor, stops-1, dst, n) + self.adj_matrix[node][neighbor])
        
        # Cache the result
        self.memo[(node, stops)] = ans        
        return ans
    
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        self.adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
        self.memo = {}
        for s, d, w in flights:
            self.adj_matrix[s][d] = w
        
        result = self.findShortest(src, K, dst, n)
        return -1 if result == float("inf") else result


## Approach 3: Bellman-Ford
###############################
# Time: O(K⋅E) - since we have K+1 iterations and in each iteration, we go over
#                all the edges in the graph.
# Space: O(V) - Occupied by the two distance arrays.
class Solution:
    
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        # We use two arrays for storing distances and keep swapping
        # between them to save on the memory
        distances = [[float('inf')] * n for _ in range(2)]
        distances[0][src] = distances[1][src] = 0
        
        # K + 1 iterations of Bellman Ford
        for iterations in range(K + 1):
            
            # Iterate over all the edges
            for s, d, wUV in flights:
                
                # Current distance of node "s" from src
                dU = distances[1 - iterations&1][s]
                
                # Current distance of node "d" from src
                # Note that this will port existing values as
                # well from the "previous" array if they didn't already exist
                dV = distances[iterations&1][d]
                
                # Relax the edge if possible
                if dU + wUV < dV:
                    distances[iterations&1][d] = dU + wUV
                    
        return -1 if distances[K&1][dst] == float("inf") else distances[K&1][dst]


## Approach 4: Breadth First Search
#######################################
# Time: O(E⋅K)
# - Since we can process each edge multiple times depending upon the improvement
#   in the shortest distances. However, the maximum number of times an edge
#   would be processed is bounded by K + 1 since that's the number of levels we
#   are going to explore in this algorithm.

# Space: O(V^2 + V⋅K)
# - The first part is the standard memory occupied by the adjacency matrix and
#   in addition to that, the distances dictionary can occupy a maximum of
#   O(V⋅K).

class Solution:
    
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        # Build the adjacency matrix
        adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
        for s, d, w in flights:
            adj_matrix[s][d] = w
            
        # Shortest distances dictionary
        distances = {}
        distances[(src, 0)] = 0
        
        # BFS Queue
        bfsQ = deque([src])
        
        # Number of stops remaining
        stops = 0
        ans = float("inf")
        
        # Iterate until we exhaust K+1 levels or the queue gets empty
        while bfsQ and stops < K + 1:
            
            # Iterate on current level
            length = len(bfsQ)
            for _ in range(length):
                node = bfsQ.popleft()
                
                # Loop over neighbors of popped node
                for nei in range(n):
                    if adj_matrix[node][nei] > 0:
                        dU = distances.get((node, stops), float("inf"))
                        dV = distances.get((nei, stops + 1), float("inf"))
                        wUV = adj_matrix[node][nei]
                        
                        # No need to update the minimum cost if we have already exhausted our K stops. 
                        if stops == K and nei != dst:
                            continue
                        
                        if dU + wUV < dV:
                            distances[nei, stops + 1] = dU + wUV
                            bfsQ.append(nei)
                            
                            # Shortest distance of the destination from the source
                            if nei == dst:
                                ans = min(ans, dU + wUV)
            stops += 1   
        
        return -1 if ans == float("inf") else ans


## From Graphs Exlore Card
##############################

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if src == dst:
            return 0
        
        INF = sys.maxsize
        previous = [INF] * n
        current = [INF] * n
        previous[src] = 0
        
        for i in range(1, k + 2):
            current[src] = 0
            for flight in flights:
                previous_flight, current_flight, cost = flight

                if previous[previous_flight] < INF:
                    current[current_flight] = min(current[current_flight],
                                                  previous[previous_flight] + cost)
                    
            previous = current.copy()
            
        return -1 if current[dst] == INF else current[dst]
