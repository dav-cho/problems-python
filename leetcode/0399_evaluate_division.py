##
#### 399. Evaluate Division (medium)
########################################


## path search in graph (backtracking w/ dfs)
#################################################
from collections import defaultdict


class Solution:
    def calcEquation(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ) -> list[float]:
        def backtrack(curr, target, products, seen):
            seen.add(curr)
            ans = -1
            neighbors = graph[curr]
            if target in neighbors:
                ans = products * neighbors[target]
            else:
                for neighbor, val in neighbors.items():
                    if neighbor in seen:
                        continue
                    ans = backtrack(neighbor, target, products * val, seen)
                    if ans != -1:
                        break
            seen.remove(curr)
            return ans

        graph = defaultdict(defaultdict)
        for (dividend, divisor), val in zip(equations, values):
            graph[dividend][divisor] = val
            graph[divisor][dividend] = 1 / val

        res = []
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                res.append(-1)
            elif dividend == divisor:
                res.append(1)
            else:
                res.append(backtrack(dividend, divisor, 1, set()))

        return res


class Solution:
    def calcEquation(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ) -> list[float]:
        def backtrack(curr, target, products, seen):
            seen.add(curr)
            ans = -1
            neighbors = graph[curr]
            if target in neighbors:
                ans = products * neighbors[target]
            else:
                for neighbor, val in neighbors.items():
                    if neighbor in seen:
                        continue
                    ans = backtrack(neighbor, target, products * val, seen)
                    if ans != -1:
                        break
            seen.remove(curr)
            return ans

        graph = defaultdict(defaultdict)
        for (dividend, divisor), val in zip(equations, values):
            graph[dividend][divisor] = val
            graph[divisor][dividend] = 1 / val

        res = []
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                ans = -1
            elif dividend == divisor:
                ans = 1
            else:
                seen = set()
                ans = backtrack(dividend, divisor, 1, seen)
            res.append(ans)

        return res


## union find - disjoint set
##############################
class Solution:
    def calcEquation(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ) -> list[float]:
        def find(node):
            # if node not in weights:
            #    weights[node] = (node, 1)
            # group, weight = weights[node]
            group, weight = weights.setdefault(node, (node, 1))
            if node != group:
                new_group, group_weight = find(group)
                weights[node] = (new_group, weight * group_weight)
            return weights[node]

        def union(dividend, divisor, val):
            num, num_weight = find(dividend)
            denom, denom_weight = find(divisor)
            if num != denom:
                weights[num] = (denom, denom_weight * val / num_weight)

        weights = {}
        for (dividend, divisor), val in zip(equations, values):
            union(dividend, divisor, val)

        res = []
        for dividend, divisor in queries:
            if dividend not in weights or divisor not in weights:
                res.append(-1)
            else:
                num, num_weight = find(dividend)
                denom, denom_weight = find(divisor)
                if num != denom:
                    res.append(-1)
                else:
                    res.append(num_weight / denom_weight)

        return res


class Solution:
    def calcEquation(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ) -> list[float]:
        weights = {}

        def find(node):
            # if node not in weights:
            #    weights[node] = (node, 1)
            # group, weight = weights[node]
            group, weight = weights.setdefault(node, (node, 1))
            if group != node:
                new_group, group_weight = find(group)
                weights[node] = (new_group, weight * group_weight)
            return weights[node]

        def union(dividend, divisor, val):
            dividend_group, dividend_weight = find(dividend)
            divisor_group, divisor_weight = find(divisor)
            if dividend_group != divisor_group:
                weights[dividend_group] = (
                    divisor_group,
                    divisor_weight * val / dividend_weight,
                )

        for (dividend, divisor), val in zip(equations, values):
            union(dividend, divisor, val)

        res = []
        for dividend, divisor in queries:
            if dividend not in weights or divisor not in weights:
                res.append(-1)
            else:
                dividend_group, dividend_weight = find(dividend)
                divisor_group, divisor_weight = find(divisor)
                if dividend_group != divisor_group:
                    res.append(-1)
                else:
                    res.append(dividend_weight / divisor_weight)

        return res


class Solution:
    def calcEquation(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ) -> list[float]:
        weights = {}

        def find(node):
            group, weight = weights.setdefault(node, (node, 1))

            if group != node:
                new_group, group_weight = find(group)
                weights[node] = (new_group, weight * group_weight)

            return weights[node]

        def union(dividend, divisor, val):
            dividend_group, dividend_weight = find(dividend)
            divisor_group, divisor_weight = find(divisor)

            if dividend_group != divisor_group:
                weights[dividend_group] = (
                    divisor_group,
                    divisor_weight * val / dividend_weight,
                )

        for (dividend, divisor), val in zip(equations, values):
            union(dividend, divisor, val)

        res = []
        for dividend, divisor in queries:
            if dividend not in weights or divisor not in weights:
                res.append(-1)
            else:
                dividend_group, dividend_weight = find(dividend)
                divisor_group, divisor_weight = find(divisor)

                if dividend_group != divisor_group:
                    res.append(-1)
                else:
                    res.append(dividend_weight / divisor_weight)

        return res


##
##############################
class Solution:
    def calcEquation(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ) -> list[float]:
        pass


##
##############################
class Solution:
    def calcEquation(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ) -> list[float]:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(
            solution.calcEquation(
                [["a", "b"], ["b", "c"]],
                [2.0, 3.0],
                [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
            ),
            [6.00000, 0.50000, -1.00000, 1.00000, -1.00000],
        )
        self.assertEqual(
            solution.calcEquation(
                [["a", "b"], ["b", "c"], ["bc", "cd"]],
                [1.5, 2.5, 5.0],
                [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
            ),
            [3.75000, 0.40000, 5.00000, 0.20000],
        )
        self.assertEqual(
            solution.calcEquation(
                [["a", "b"]], [0.5], [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
            ),
            [0.50000, 2.00000, -1.00000, -1.00000],
        )


if __name__ == "__main__":
    unittest.main()
