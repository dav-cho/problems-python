##
#### Reconstruct Itinerary (medium)
#######################################

# You are given a list of airline tickets where tickets[i] = [fromi, toi]
# represent the departure and the arrival airports of one flight. Reconstruct
# the itinerary in order and return it.

# All of the tickets belong to a man who departs from "JFK", thus, the itinerary
# must begin with "JFK". If there are multiple valid itineraries, you should
# return the itinerary that has the smallest lexical order when read as a
# single string.

# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than
# ["JFK", "LGB"].
# You may assume all tickets form at least one valid itinerary. You must use all
# the tickets once and only once.

# Example 1:
# Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# Output: ["JFK","MUC","LHR","SFO","SJC"]

# Example 2:
# Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
 
# Constraints:
# 1 <= tickets.length <= 300
# tickets[i].length == 2
# fromi.length == 3
# toi.length == 3
# fromi and toi consist of uppercase English letters.
# fromi != toi

################################################################################

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
        route = ['JFK']
        self.backtrack('JFK', route)
        
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
        route = ['JFK']
        backtrack('JFK', route)
        
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
        route = ['JFK']
        backtrack('JFK', route)
        
        return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]), ["JFK","MUC","LHR","SFO","SJC"])
        self.assertEqual(solution.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]), ["JFK","ATL","JFK","SFO","ATL","SFO"])


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Backtracking + Greedy
########################################
# Time: O(|E|^d) - where |E|∣E∣ is the number of total flights and d is the
#                  maximum number of flights from an airport.
# - It is tricky to estimate the time complexity of the backtracking algorithm,
#   since the algorithm often has an early stopping depending on the input.
# - To calculate a loose upper bound for the time complexity, let us consider
#   it as a combination problem where the goal is to construct a sequence of a
#   specific order, i.e. |V_1V_2...V_n|. For each position V_i, we could have d
#   choices, i.e. at each airport one could have at most d possible
#   destinations. Since the length of the sequence is |E|, the total number of
#   combination would be |E|^d.
# - In the worst case, our backtracking algorithm would have to enumerate all
#   possible combinations.

# Space: O(|V| + |E|) - Where |V| is the number of airports and |E| is the
#                       number of flights.
# - In the algorithm, we use the graph as well as the visit bitmap, which would
#   require the space of |V| + |E|.
# - Since we applied recursion in the algorithm, which would incur additional
#   memory consumption in the function call stack. The maximum depth of the
#   recursion would be exactly the number of flights in the input, i.e. |E|.
# - As a result, the total space complexity of the algorithm would be
#   O(|V| + 2⋅|E|) = O(|V| + |E|).

class Solution(object):
    """  """
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        from collections import defaultdict
        self.flightMap = defaultdict(list)

        for ticket in tickets:
            origin, dest = ticket[0], ticket[1]
            self.flightMap[origin].append(dest)

        self.visitBitmap = {}

        # sort the itinerary based on the lexical order
        for origin, itinerary in self.flightMap.items():
        # Note that we could have multiple identical flights, i.e. same origin and destination.
            itinerary.sort()
            self.visitBitmap[origin] = [False]*len(itinerary)

        self.flights = len(tickets)
        self.result = []
        route = ['JFK']
        self.backtracking('JFK', route)

        return self.result


    def backtracking(self, origin, route):
        if len(route) == self.flights + 1:
            self.result = route
            return True

        for i, nextDest in enumerate(self.flightMap[origin]):
            if not self.visitBitmap[origin][i]:
                # mark the visit before the next recursion
                self.visitBitmap[origin][i] = True
                ret = self.backtracking(nextDest, route + [nextDest])
                self.visitBitmap[origin][i] = False
                if ret:
                    return True

        return False


## Approach 2: Hierholzer's Algorithm
#########################################
# Time: O(|E|log(|E|/|V|)) - Where |E| is the number of edges (flights) in the
#                            input.
# - As one can see from the above algorithm, during the DFS process, we would
#   traverse each edge once. Therefore, the complexity of the DFS function would
#   be |E|.
# - However, before the DFS, we need to sort the outgoing edges for each vertex.
#   And this, unfortunately, dominates the overall complexity.
# - It is though tricky to estimate the complexity of sorting, which depends on
#   the structure of the input graph.
# - In the worst case where the graph is not balanced, i.e. the connections are
#   concentered in a single airport. Imagine the graph is of star shape, in this
#   case, the JFK airport would assume half of the flights (since we still need
#   the return flight). As a result, the sorting operation on this airport would
#   be exceptionally expensive, i.e. NlogN, where N = |E|/2. And this would be
#   the final complexity as well, since it dominates the rest of the
#   calculation.
# - Let us consider a less bad case, or an average case, where the graph is less
#   clustered, i.e. each node has the equal number of outgoing flights. Under
#   this assumption, each airport would have |E|/(2⋅|V|) number of flights
#   (still we need the return flights). Again, we can plug it into the NlogN
#   minimal sorting complexity. In addition, this time, we need to take into
#   consideration all airports, rather than the superhub (JFK) in the above
#   case. As a result, we have |V|⋅(NlogN), where N = |E|/(2⋅|V|). If we expand
#   the formula, we will obtain the complexity of the average case as
#   O((|E|/2)log(|E|/(2⋅|V|))) = O(|E|log(|E|/V))

# Space: O(|V| + |E|) - Where |V| is the number of airports and |E| is the
#                       number of flights.
# - In the algorithm, we use the graph, which would require the space of
#   |V| + |E|.
# - Since we applied recursion in the algorithm, which would incur additional
#   memory consumption in the function call stack. The maximum depth of the
#   recursion would be exactly the number of flights in the input, i.e. |E|.
# - As a result, the total space complexity of the algorithm would be
#   O(|V| + 2⋅|E|) = O(|V| + |E|).

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        from collections import defaultdict
        self.flightMap = defaultdict(list)

        for ticket in tickets:
            origin, dest = ticket[0], ticket[1]
            self.flightMap[origin].append(dest)

        # sort the itinerary based on the lexical order
        for origin, itinerary in self.flightMap.items():
        # Note that we could have multiple identical flights, i.e. same origin and destination.
            itinerary.sort(reverse=True)

        self.result = []
        self.DFS('JFK')

        # reconstruct the route backwards
        return self.result[::-1]

    def DFS(self, origin):
        destList = self.flightMap[origin]
        while destList:
            #while we visit the edge, we trim it off from graph.
            nextDest = destList.pop()
            self.DFS(nextDest)
        self.result.append(origin)


