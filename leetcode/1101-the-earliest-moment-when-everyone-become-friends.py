##
#### The Earliest Moment When Everyone Become Friends (medium)
##################################################################

# There are n people in a social group labeled from 0 to n - 1. You are given an
# array logs where logs[i] = [timestamp_i, x_i, y_i] indicates that x_i and y_i
# will be friends at the time timestamp_i.

# Friendship is symmetric. That means if a is friends with b, then b is friends
# with a. Also, person a is acquainted with a person b if a is friends with b,
# or a is a friend of someone acquainted with b.

# Return the earliest time for which every person became acquainted with every
# other person. If there is no such earliest time, return -1.

# Example 1:
# input: logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], n = 6
# output: 20190301
# explanation: 
# - the first event occurs at timestamp = 20190101 and after 0 and 1 become
#   friends we have the following friendship groups [0,1], [2], [3], [4], [5].
# - the second event occurs at timestamp = 20190104 and after 3 and 4 become
#   friends we have the following friendship groups [0,1], [2], [3,4], [5].
# - the third event occurs at timestamp = 20190107 and after 2 and 3 become
#   friends we have the following friendship groups [0,1], [2,3,4], [5].
# - the fourth event occurs at timestamp = 20190211 and after 1 and 5 become
#   friends we have the following friendship groups [0,1,5], [2,3,4].
# - the fifth event occurs at timestamp = 20190224 and as 2 and 4 are already
#   friends anything happens.
# - the sixth event occurs at timestamp = 20190301 and after 0 and 3 become
#   friends we have that all become friends.

# Example 2:
# input: logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], n = 4
# output: 3

# constraints:
# 2 <= n <= 100
# 1 <= logs.length <= 104
# logs[i].length == 3
# 0 <= timestampi <= 109
# 0 <= xi, yi <= n - 1
# xi != yi
# all the values timestampi are unique.
# all the pairs (xi, yi) occur at most one time in the input.

################################################################################

## union find
##############################
class Solution:
    def earliestAcq(self, logs: list[list[int]], n: int) -> int:
        root = list(range(n))
        rank = [1] * n
        self.count = n
        
        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]
        
        def union(x, y):
            root_x, root_y = map(find, (x, y))
            if root_x == root_y:
                return
            
            if rank[root_x] < rank[root_y]:
                root[root_x] = root_y
            else:
                root[root_y] = root_x
                if rank[root_x] == rank[root_y]:
                    rank[root_x] += 1
            self.count -= 1
                    
        for time, x, y in sorted(logs):
            union(x, y)
            if self.count == 1:
                return time
        
        return -1


class Solution:
    def earliestAcq(self, logs: list[list[int]], n: int) -> int:
        uf = UnionFind(n)
        for time, x, y in sorted(logs):
            uf.union(x, y)
            if uf.count == 1:
                return time
        
        return -1
    

class UnionFind:
    def __init__(self, size):
        self.root = list(range(size))
        self.rank = [1] * size
        self.count = size
        
    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        root_x, root_y = map(self.find, (x, y))
        if root_x == root_y:
            return
        
        if self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = root_y
        else:
            self.root[root_y] = root_x
            if elf.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1
        self.count -= 1


## dfs recursive
##############################
class Solution:
    def earliestAcq(self, logs: list[list[int]], n: int) -> int:
        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            
            for neighbor in adj_list[node]:
                dfs(neighbor)
        
        adj_list = {x: [] for x in range(n)}
        seen = set()
        edges = 0
        for time, x, y in sorted(logs):
            adj_list[x].append(y)
            adj_list[y].append(x)
            edges += 1
            
            if edges < n - 1:
                continue
                
            res = 0
            for node in range(n):
                if node in seen:
                    continue
                    
                res += 1
                dfs(node)
                
            if res == 1:
                return time
            
            seen = set()
        
        return -1


## dfs iterative
##############################
class Solution:
    def earliestAcq(self, logs: list[list[int]], n: int) -> int:
        pass


## bfs iterative
##############################
class Solution:
    def earliestAcq(self, logs: list[list[int]], n: int) -> int:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.earliestAcq([[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], 6), 20190301)
        self.assertEqual(solution.earliestAcq([[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], 4), 3)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: 
##############################
# Time: 
# Space: 


## Approach 2: 
##############################
# Time: 
# Space: 


## Approach 3: 
##############################
# Time: 
# Space: 


