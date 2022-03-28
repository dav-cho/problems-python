##
#### 332. Reconstruct Itinerary (medium)
############################################


## backtracking/greedy
##############################
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        self.flight_map = defaultdict(list)
        for origin, dest in tickets:
            self.flight_map[origin].append(dest)

        self.seen = {}
        for origin, itinerary in self.flight_map.items():
            itinerary.sort()
            self.seen[origin] = [False] * len(itinerary)

        self.flights = len(tickets)
        self.res = []
        route = ["JFK"]
        self.backtrack("JFK", route)

        return self.res

    def backtrack(self, origin, route):
        if len(route) == self.flights + 1:
            self.res = route
            return True

        for i, next_dest in enumerate(self.flight_map[origin]):
            if not self.seen[origin][i]:
                self.seen[origin][i] = True
                ret = self.backtrack(next_dest, route + [next_dest])
                self.seen[origin][i] = False

                if ret:
                    return True
        return False


## backtracking
##############################
class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        def backtrack(origin, route):
            if len(route) == len(tickets) + 1:
                self.res = route
                return True

            for i, next_dest in enumerate(flight_map[origin]):
                if not seen[origin][i]:
                    seen[origin][i] = True
                    ret = backtrack(next_dest, route + [next_dest])
                    seen[origin][i] = False

                    if ret:
                        return True
            return False

        flight_map = defaultdict(list)
        for origin, dest in tickets:
            flight_map[origin].append(dest)

        seen = {}
        for origin, itinerary in flight_map.items():
            itinerary.sort()
            seen[origin] = [False] * len(itinerary)

        self.res = []
        route = ["JFK"]
        backtrack("JFK", route)

        return self.res


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        def backtrack(origin, route):
            if len(route) == len(tickets) + 1:
                nonlocal res
                res = route
                return True

            for i, next_dest in enumerate(flight_map[origin]):
                if not seen[origin][i]:
                    seen[origin][i] = True
                    ret = backtrack(next_dest, route + [next_dest])
                    seen[origin][i] = False

                    if ret:
                        return True
            return False

        flight_map = defaultdict(list)
        for origin, dest in tickets:
            flight_map[origin].append(dest)

        seen = {}
        for origin, itinerary in flight_map.items():
            itinerary.sort()
            seen[origin] = [False] * len(itinerary)

        res = []
        route = ["JFK"]
        backtrack("JFK", route)

        return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(
            solution.findItinerary(
                [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
            ),
            ["JFK", "MUC", "LHR", "SFO", "SJC"],
        )
        self.assertEqual(
            solution.findItinerary(
                [
                    ["JFK", "SFO"],
                    ["JFK", "ATL"],
                    ["SFO", "ATL"],
                    ["ATL", "JFK"],
                    ["ATL", "SFO"],
                ]
            ),
            ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"],
        )


if __name__ == "__main__":
    unittest.main()
