##
#### 730. Network Delay Time (medium)
#########################################


## dfs
##############################
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for node, neighbor, time in times:
            graph[node].append((time, neighbor))

        dist = {node: float("inf") for node in range(1, n + 1)}

        def dfs(node, elapsed):
            if elapsed >= dist[node]:
                return

            dist[node] = elapsed

            for time, neighbor in sorted(graph[node]):
                dfs(neighbor, elapsed + time)

        dfs(k, 0)
        res = max(dist.values())

        return res if res < float("inf") else -1


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for (
            u,
            v,
            w,
        ) in times:
            graph[u].append((w, v))

        dist = {node: float("inf") for node in range(1, n + 1)}

        def dfs(node, elapsed):
            if elapsed >= dist[node]:
                return

            dist[node] = elapsed

            for time, neighbor in sorted(graph[node]):
                dfs(neighbor, elapsed + time)

        dfs(k, 0)
        res = max(dist.values())

        return res if res < float("inf") else -1


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for (
            u,
            v,
            w,
        ) in times:
            graph[u].append((v, w))

        dist = {node: float("inf") for node in range(1, n + 1)}

        def dfs(node, elapsed):
            if elapsed >= dist[node]:
                return

            dist[node] = elapsed

            for neighbor, time in sorted(graph[node], key=lambda edge: edge[1]):
                dfs(neighbor, elapsed + time)

        dfs(k, 0)
        res = max(dist.values())

        return res if res < float("inf") else -1


## dijkstra's algorithm - basic
###################################
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {node: float("inf") for node in range(1, n + 1)}
        dist[k] = 0
        seen = set()

        while True:
            cand_node = -1
            cand_dist = float("inf")

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

        return res if res < float("inf") else -1


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for node, neighbor, time in times:
            graph[node].append((neighbor, time))

        dist = {node: float("inf") for node in range(1, n + 1)}
        seen = set()
        dist[k] = 0

        while True:
            cand_node = -1
            cand_dist = float("inf")

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

        return res if res < float("inf") else -1


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
        self.assertEqual(
            solution.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2), 2
        )
        self.assertEqual(solution.networkDelayTime([[1, 2, 1]], 2, 1), 1)
        self.assertEqual(solution.networkDelayTime([[1, 2, 1]], 2, 2), -1)


if __name__ == "__main__":
    unittest.main()
