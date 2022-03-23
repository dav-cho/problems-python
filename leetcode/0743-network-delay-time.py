##
#### Network Delay Time (medium)
########################################

# You are given a network of n nodes, labeled from 1 to n. You are also given
# times, a list of travel times as directed edges times[i] = (ui, vi, wi),
# where ui is the source node, vi is the target node, and wi is the time it
# takes for a signal to travel from source to target.

# We will send a signal from a given node k. Return the time it takes for all
# the n nodes to receive the signal. If it is impossible for all the n nodes to
# receive the signal, return -1.

# Example 1:
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2

# Example 2:
# Input: times = [[1,2,1]], n = 2, k = 1
# Output: 1

# Example 3:
# Input: times = [[1,2,1]], n = 2, k = 2
# Output: -1
 
# Constraints:
# 1 <= k <= n <= 100
# 1 <= times.length <= 6000
# times[i].length == 3
# 1 <= ui, vi <= n
# ui != vi
# 0 <= wi <= 100
# All the pairs (ui, vi) are unique. (i.e., no multiple edges.)

################################################################################

## dfs
##############################
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for node, neighbor, time in times:
            graph[node].append((time, neighbor))
            
        dist = {node: float('inf') for node in range(1, n + 1)}
        
        def dfs(node, elapsed):
            if elapsed >= dist[node]:
                return
            
            dist[node] = elapsed
            
            for time, neighbor in sorted(graph[node]):
                dfs(neighbor, elapsed + time)
                
        dfs(k, 0)
        res = max(dist.values())
        
        return res if res < float('inf') else -1


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w, in times:
            graph[u].append((w, v))
            
        dist = {node: float('inf') for node in range(1, n + 1)}
        
        def dfs(node, elapsed):
            if elapsed >= dist[node]:
                return
            
            dist[node] = elapsed
            
            for time, neighbor in sorted(graph[node]):
                dfs(neighbor, elapsed + time)
                
        dfs(k, 0)
        res = max(dist.values())
        
        return res if res < float('inf') else -1


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w, in times:
            graph[u].append((v, w))
            
        dist = {node: float('inf') for node in range(1, n + 1)}
        
        def dfs(node, elapsed):
            if elapsed >= dist[node]:
                return
            
            dist[node] = elapsed
            
            for neighbor, time in sorted(graph[node], key=lambda edge: edge[1]):
                dfs(neighbor, elapsed + time)
                
        dfs(k, 0)
        res = max(dist.values())
        
        return res if res < float('inf') else -1


## dijkstra's algorithm - basic
###################################
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
            
        dist = {node: float('inf') for node in range(1, n + 1)}
        dist[k] = 0
        seen = set()
        
        while True:
            cand_node = -1
            cand_dist = float('inf')

            for node in range(1, n + 1):
                if node not in seen and dist[node] < cand_dist:
                    cand_node = node
                    cand_dist = dist[node]
                    
            if cand_node < 0:
                break
                
            seen.add(cand_node)

            for neighbor, time in graph[cand_node]:
                dist[neighbor] = min(dist[neighbor], dist[cand_node] + time)
                
        res = max(dist.values())

        return res if res < float('inf') else -1


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for node, neighbor, time in times:
            graph[node].append((neighbor, time))

        dist = {node: float('inf') for node in range(1, n + 1)}
        seen = set()
        dist[k] = 0
        
        while True:
            cand_node = -1
            cand_dist = float('inf')

            for node in range(1, n + 1):
                if node not in seen and dist[node] < cand_dist:
                    cand_node = node
                    cand_dist = dist[node]

            if cand_node < 0:
                break
            
            seen.add(cand_node)

            for neighbor, time in graph[cand_node]:
                dist[neighbor] = min(dist[neighbor], dist[cand_node] + time)

        res = max(dist.values())

        return res if res < float('inf') else -1


## dijkstra's algorithm - heap
##################################
import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for node, neighbor, time in times:
            graph[node].append((neighbor, time))
            
        dist = {}
        pq = [(0, k)]

        while pq:
            elapsed, node = heapq.heappop(pq)
            if node in dist:
                continue
                
            dist[node] = elapsed
            
            for neighbor, time in graph[node]:
                if neighbor not in dist:
                    heapq.heappush(pq, (elapsed + time, neighbor))
                    
        return max(dist.values()) if len(dist) == n else -1


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
            
        pq = [(0, k)]
        dist = {}

        while pq:
            elapsed, node = heapq.heappop(pq)
            if node in dist:
                continue
                
            dist[node] = elapsed
            
            for neighbor, time in graph[node]:
                if neighbor not in dist:
                    heapq.heappush(pq, (elapsed + time, neighbor))
                    
        return max(dist.values()) if len(dist) == n else -1


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
            
        # edge weight must come before node because
        # heapq will sort based on first value (weight)
        pq = [(0, k)]
        dist = {}

        while pq:
            d, node = heapq.heappop(pq)
            if node in dist:
                continue
                
            dist[node] = d
            
            for neighbor, d2 in graph[node]:
                if neighbor not in dist:
                    heapq.heappush(pq, (d + d2, neighbor))
                    
        return max(dist.values()) if len(dist) == n else -1


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2), 2)
        self.assertEqual(solution.networkDelayTime([[1,2,1]], 2, 1), 1)
        self.assertEqual(solution.networkDelayTime([[1,2,1]], 2, 2), -1)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Depth-First Search [Accepted]
################################################
# Time: O(N^N + ElogE) - Where E is the length of times. We can only fully visit
#                        each node up to N - 1 times, one per each other node.
#                        Plus, we have to explore every edge and sort them.
#                        Sorting each small bucket outgoing edges is bounded by
#                        sorting all of them, because of repeated use of
#                        inequality xlogx + ylogy <= (x + y)log(x + y).
# Space: O(N + E) - The size of the graph (O(E)), plus the size of the implicit
#                   call stack in our DFS (O(N)).
class Solution(object):
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))

        dist = {node: float('inf') for node in xrange(1, N+1)}

        def dfs(node, elapsed):
            if elapsed >= dist[node]: return
            dist[node] = elapsed
            for time, nei in sorted(graph[node]):
                dfs(nei, elapsed + time)

        dfs(K, 0)
        ans = max(dist.values())
        return ans if ans < float('inf') else -1


## Approach 2: Dijkstra's Algorithm [Accepted]
##################################################
# Time: O(N^2 + E)m - Where E is the length of times in basic implementation,
#                     and O(ElogE) in the heap implmentation, as potentially
#                     every edge gets added to the heap.
# Space: O(N + E) - The size of the graph (O(E)), plus the size of the other 
#                   objects used (O(N)).

## Basic Implementation
class Solution(object):
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {node: float('inf') for node in xrange(1, N+1)}
        seen = [False] * (N+1)
        dist[K] = 0

        while True:
            cand_node = -1
            cand_dist = float('inf')
            for i in xrange(1, N+1):
                if not seen[i] and dist[i] < cand_dist:
                    cand_node = i
                    cand_dist = dist[i]

            if cand_node < 0: break
            seen[cand_node] = True
            for nei, d in graph[cand_node]:
                dist[nei] = min(dist[nei], dist[cand_node] + d)

        ans = max(dist.values())
        return ans if ans < float('inf') else -1


## Heap Implementation
class Solution(object):
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        pq = [(0, K)]
        dist = {}
        while pq:
            d, node = heapq.heappop(pq)
            if node in dist: continue
            dist[node] = d
            for nei, d2 in graph[node]:
                if nei not in dist:
                    heapq.heappush(pq, (d+d2, nei))

        return max(dist.values()) if len(dist) == N else -1


