##
#### 787. Cheapest Flights Within K Stops (medium)
######################################################


## dijkstra's algorithm
##############################
import heapq


class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        adj_matrix = [[0] * n for _ in range(n)]
        for s, d, cost in flights:
            adj_matrix[s][d] = cost

        dist = {node: float("inf") for node in range(n)}
        stops = {node: float("inf") for node in range(n)}
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
                    heapq.heappush(
                        min_heap, (curr_cost + cost, curr_stops + 1, neighbor)
                    )
                if curr_stops < stops[neighbor]:
                    heapq.heappush(
                        min_heap, (curr_cost + cost, curr_stops + 1, neighbor)
                    )

                stops[neighbor] = curr_stops

        return dist[dst] if dist[dst] < float("inf") else -1


class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        adj_matrix = [[0] * n for _ in range(n)]
        for s, d, cost in flights:
            adj_matrix[s][d] = cost

        dist = [float("inf")] * n
        stops = [float("inf")] * n
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
                    heapq.heappush(
                        min_heap, (curr_cost + cost, curr_stops + 1, neighbor)
                    )
                if curr_stops < stops[neighbor]:
                    heapq.heappush(
                        min_heap, (curr_cost + cost, curr_stops + 1, neighbor)
                    )

                stops[neighbor] = curr_stops

        return dist[dst] if dist[dst] != float("inf") else -1


class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        adj_matrix = [[0] * n for _ in range(n)]
        for node, neighbor, cost in flights:
            adj_matrix[node][neighbor] = cost

        dist = [float("inf")] * n
        stops = [float("inf")] * n
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

        return dist[dst] if dist[dst] < float("inf") else -1


## dfs with memoization
##############################
class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        def dfs(node, stops):
            if node == dst:
                return 0
            if stops < 0:
                return float("inf")
            if (node, stops) in memo:
                return memo[(node, stops)]

            res = float("inf")

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

        return res if res < float("inf") else -1


class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        def dfs(node, stops):
            if node == dst:
                return 0
            if stops < 0:
                return float("inf")
            if (node, stops) in memo:
                return memo[(node, stops)]

            res = float("inf")

            for neighbor in range(n):
                if adj_matrix[node][neighbor] > 0:
                    res = min(
                        res, dfs(neighbor, stops - 1) + adj_matrix[node][neighbor]
                    )

            memo[(node, stops)] = res

            return res

        adj_matrix = [[0] * n for _ in range(n)]
        memo = {}

        for s, d, cost in flights:
            adj_matrix[s][d] = cost

        res = dfs(src, k)

        return res if res < float("inf") else -1


class Solution:
    def find_shortest(self, node, stops, dst, n):
        if node == dst:
            return 0
        if stops < 0:
            return float("inf")
        if (node, stops) in self.memo:
            return self.memo[(node, stops)]

        res = float("inf")

        for neighbor in range(n):
            if self.adj_matrix[node][neighbor] > 0:
                res = min(
                    res,
                    self.find_shortest(neighbor, stops - 1, dst, n)
                    + self.adj_matrix[node][neighbor],
                )

        self.memo[(node, stops)] = res

        return res

    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        self.adj_matrix = [[0] * n for _ in range(n)]
        self.memo = {}

        for s, d, cost in flights:
            self.adj_matrix[s][d] = cost

        res = self.find_shortest(src, k, dst, n)

        return res if res < float("inf") else -1


class Solution:
    def __init__(self):
        self.adj_matrix = None
        self.memo = {}

    def find_shortest(self, node, stops, dst, n):
        if node == dst:
            return 0
        if stops < 0:
            return float("inf")
        if (node, stops) in self.memo:
            return self.memo[(node, stops)]

        res = float("inf")

        for neighbor in range(n):
            if self.adj_matrix[node][neighbor] > 0:
                res = min(
                    res,
                    self.find_shortest(neighbor, stops - 1, dst, n)
                    + self.adj_matrix[node][neighbor],
                )

        self.memo[(node, stops)] = res

        return res

    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        self.adj_matrix = [[0] * n for _ in range(n)]

        for s, d, cost in flights:
            self.adj_matrix[s][d] = cost

        res = self.find_shortest(src, k, dst, n)

        return res if res < float("inf") else -1


## bellman-ford algorithm
##############################
class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        dist = {node: [float("inf")] * n for node in range(n)}
        dist[0][src] = dist[1][src] = 0

        for iteration in range(k + 1):
            for s, d, curr_cost in flights:
                cost = dist[~iteration & 1][s]

                if curr_cost + cost < dist[iteration & 1][d]:
                    dist[iteration & 1][d] = curr_cost + cost

        res = dist[k & 1][dst]

        return res if res < float("inf") else -1


class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        if src == dst:
            return 0

        prev = [float("inf")] * n
        curr = [float("inf")] * n
        prev[src] = 0

        for iteration in range(k + 1):
            prev[src] = 0

            for s, d, cost in flights:
                if prev[s] < float("inf"):
                    curr[d] = min(curr[d], prev[s] + cost)

            prev = curr.copy()

        return curr[dst] if curr[dst] < float("inf") else -1


class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        if src == dst:
            return 0

        prev = [float("inf")] * n
        curr = [float("inf")] * n
        prev[src] = 0

        for iteration in range(k + 1):
            prev[src] = 0

            for source, dest, cost in flights:
                if prev[source] < float("inf"):
                    curr[dest] = min(curr[dest], prev[source] + cost)

            prev = curr.copy()

        return curr[dst] if curr[dst] < float("inf") else -1


class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
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

        return curr[dst] if curr[dst] < float("inf") else -1


class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        dist = {node: [float("inf")] * n for node in range(n)}
        dist[0][src] = dist[1][src] = 0

        for iteration in range(k + 1):
            for s, d, curr_cost in flights:
                cost = dist[1 - iteration & 1][s]

                if curr_cost + cost < dist[iteration & 1][d]:
                    dist[iteration & 1][d] = curr_cost + cost

        return dist[k & 1][dst] if dist[k & 1][dst] < float("inf") else -1


class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        dist = {node: [float("inf")] * n for node in range(n)}
        dist[0][src] = dist[1][src] = 0

        for iteration in range(k + 1):
            for source, destination, curr_cost in flights:
                cost = dist[1 - iteration & 1][source]

                if curr_cost + cost < dist[iteration & 1][destination]:
                    dist[iteration & 1][destination] = curr_cost + cost

        res = dist[k & 1][dst]
        return res if res < float("inf") else -1


class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        distances = [[float("inf")] * n for _ in range(n)]
        distances[0][src] = distances[1][src] = 0

        for iteration in range(k + 1):
            for u, v, wUV in flights:
                dU = distances[1 - iteration & 1][u]
                dV = distances[iteration & 1][v]

                if dU + wUV < dV:
                    distances[iteration & 1][v] = dU + wUV

        return distances[k & 1][dst] if distances[k & 1][dst] < float("inf") else -1


## bfs
##############################
class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(
            solution.findCheapestPrice(
                3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1
            ),
            200,
        )
        self.assertEqual(
            solution.findCheapestPrice(
                3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0
            ),
            500,
        )


if __name__ == "__main__":
    unittest.main()
