##
#### 1059. All Paths from Source Lead to Destination (medium)
#################################################################


## dfs
##############################
class Solution:
    GRAY = 1
    BLACK = 2

    def leadsToDestination(
        self, n: int, edges: list[list[int]], source: int, destination: int
    ) -> bool:
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
        self.assertEqual(solution.leadsToDestination(3, [[0, 1], [0, 2]], 0, 2), False)
        self.assertEqual(
            solution.leadsToDestination(4, [[0, 1], [0, 3], [1, 2], [2, 1]], 0, 3),
            False,
        )
        self.assertEqual(
            solution.leadsToDestination(4, [[0, 1], [0, 2], [1, 3], [2, 3]], 0, 3), True
        )
        self.assertEqual(
            solution.leadsToDestination(3, [[0, 1], [1, 1], [1, 2]], 0, 2), False
        )
        self.assertEqual(solution.leadsToDestination(2, [[0, 1], [1, 1]], 0, 1), False)


if __name__ == "__main__":
    unittest.main()
