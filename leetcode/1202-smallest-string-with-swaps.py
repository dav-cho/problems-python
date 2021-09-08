##
#### Smallest String With Swaps (medium)
############################################

# You are given a string s, and an array of pairs of indices in the string pairs
# where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

# You can swap the characters at any pair of indices in the given pairs any
# number of times.

# Return the lexicographically smallest string that s can be changed to after
# using the swaps.

# Example 1:
# Input: s = "dcab", pairs = [[0,3],[1,2]]
# Output: "bacd"
# Explaination: 
# Swap s[0] and s[3], s = "bcad"
# Swap s[1] and s[2], s = "bacd"

# Example 2:
# Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
# Output: "abcd"
# Explaination: 
# Swap s[0] and s[3], s = "bcad"
# Swap s[0] and s[2], s = "acbd"
# Swap s[1] and s[2], s = "abcd"

# Example 3:
# Input: s = "cba", pairs = [[0,1],[1,2]]
# Output: "abc"
# Explaination: 
# Swap s[0] and [1], s = "bca"
# Swap s[1] and s[2], s = "bac"
# Swap s[0] and s[1], s = "abc"

################################################################################

## union find
##############################

import collections


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: list[list[int]]) -> str:
        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]
        
        def union(pair):
            x, y = map(find, pair)
            if x == y:
                return
            
            if rank[x] < rank[y]:
                root[x] = y
            else:
                root[y] = x
                if rank[x] == rank[y]:
                    rank[x] += 1
        
        n = len(s)
        root = list(range(n))
        rank = [1] * n
        
        for pair in pairs:
            union(pair)
            
        comps = collections.defaultdict(list)
        for i in range(n):
            comps[find(i)].append(s[i])
        for j in comps:
            comps[j].sort(reverse=True)
        
        res = []
        for k in range(n):
            res.append(comps[root[k]].pop())
        
        return ''.join(res)


## same as above but with root_x, root_y instead of x, y
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: list[list[int]]) -> str:
        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]
        
        def union(pair):
            root_x, root_y = map(find, pair)
            if root_x == root_y:
                return
            
            if rank[root_x] < rank[root_y]:
                root[root_x] = root_y
            else:
                root[root_y] = root_x
                if rank[root_x] == rank[root_y]:
                    rank[root_x] += 1
                    
        n = len(s)
        root = list(range(n))
        rank = [1] * n
        
        for pair in pairs:
            union(pair)
            
        comps = collections.defaultdict(list)
        for i in range(n):
            comps[find(i)].append(s[i])
        for j in comps:
            comps[j].sort(reverse=True)
        
        res = []
        for k in range(n):
            res.append(comps[root[k]].pop())
            
        return ''.join(res)


## same as above but with find(k) instead of root[k]
## - find(i) in prior for loop should set all roots to actual roots
##   so no need for find(k). use root[k] for O(1)
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: list[list[int]]) -> str:
        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]
        
        def union(pair):
            root_x, root_y = map(find, pair)
            if root_x == root_y:
                return
            
            if rank[root_x] < rank[root_y]:
                root[root_x] = root_y
            else:
                root[root_y] = root_x
                if rank[root_x] == rank[root_y]:
                    rank[root_x] += 1
                    
        n = len(s)
        root = list(range(n))
        rank = [1] * n
        
        for pair in pairs:
            union(pair)
            
        comps = collections.defaultdict(list)
        for i in range(n):
            comps[find(i)].append(s[i])
        for j in comps:
            comps[j].sort(reverse=True)
        
        res = []
        for k in range(n):
            res.append(comps[find(k)].pop())
        
        return ''.join(res)


## naive quick union instead of union by rank
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: list[list[int]]) -> str:
        n = len(s)
        root = list(range(n))
        rank = [1] * n
        
        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]
        
        def union(x, y):
            root[find(x)] = find(y)
                    
        for x, y in pairs:
            union(x, y)
        
        comps = collections.defaultdict(list)
        for i in range(n):
            comps[find(i)].append(s[i])
        
        for j in comps.keys():
            comps[j].sort(reverse=True)
            
        res = []
        for k in range(n):
            res.append(comps[find(k)].pop())
            
        return ''.join(res)


## dfs recursive
##############################
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: list[list[int]]) -> str:
        def dfs(node):
            if node in seen:
                return
            
            seen.add(node)
            component.append(node)
            
            for neighbor in adj_list[node]:
                dfs(neighbor)
                
        n = len(s)
        adj_list = [[] for _ in range(n)]
        for x, y in pairs:
            adj_list[x].append(y)
            adj_list[y].append(x)
            
        seen = set()
        res = list(s)
        
        for node in range(n):
            if node in seen:
                continue
                
            component = []
            dfs(node)
            component.sort()

            chars = [res[x] for x in component]
            chars.sort()

            for i in range(len(component)):
                res[component[i]] = chars[i]
                    
        return ''.join(res)


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.smallestStringWithSwaps("dcab", [[0,3],[1,2]]), "bacd")
        self.assertEqual(solution.smallestStringWithSwaps("dcab", [[0,3],[1,2],[0,2]]), "abcd")
        self.assertEqual(solution.smallestStringWithSwaps("cba", [[0,1],[1,2]]), "abc")


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


