##
#### 310. Minimum Height Trees (medium)
#############################################


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
        self.assertCountEqual(
            Solution().findMinHeightTrees(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]),
            [3, 4],
        )
        self.assertCountEqual(Solution().findMinHeightTrees(1, []), [0])
        self.assertCountEqual(Solution().findMinHeightTrees(2, [[0, 1]]), [0, 1])


if __name__ == "__main__":
    unittest.main()
