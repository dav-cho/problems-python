##
#### Alien Dictionary (hard)
########################################

# There is a new alien language that uses the English alphabet. However, the
# order among the letters is unknown to you.

# You are given a list of strings words from the alien language's dictionary,
# where the strings in words are sorted lexicographically by the rules of this
# new language.

# Return a string of the unique letters in the new alien language sorted in
# lexicographically increasing order by the new language's rules. If there is
# no solution, return "". If there are multiple solutions, return any of them.

# A string s is lexicographically smaller than a string t if at the first
# letter where they differ, the letter in s comes before the letter in t in the
# alien language. If the first min(s.length, t.length) letters are the same,
# then s is smaller if and only if s.length < t.length.

# Example 1:
# Input: words = ["wrt","wrf","er","ett","rftt"]
# Output: "wertf"

# Example 2:
# Input: words = ["z","x"]
# Output: "zx"

# Example 3:
# Input: words = ["z","x","z"]
# Output: ""
# Explanation: The order is invalid, so return "".
 
# Constraints:
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of only lowercase English letters.

################################################################################

from collections import defaultdict, Counter, deque


## bfs
##############################
class Solution:
    def alienOrder(self, words: list[str]) -> str:
        adj_list = defaultdict(set)
        indegree = Counter({char: 0 for word in words for char in word})
        for word_a, word_b in zip(words, words[1:]):
            for char_a, char_b in zip(word_a, word_b):
                if char_a != char_b:
                    if char_b not in adj_list[char_a]:
                        adj_list[char_a].add(char_b)
                        indegree[char_b] += 1
                    break
            else:
                if len(word_b) < len(word_a):
                    return ''
                
        res = []
        queue = deque([char for char in indegree if indegree[char] == 0])
        while queue:
            char = queue.popleft()
            res.append(char)
            for neighbor in adj_list[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return ''.join(res) if len(res) == len(indegree) else ''


## dfs
##############################
class Solution:
    def alienOrder(self, words: list[str]) -> str:
        rev_adj_list = {char: [] for word in words for char in word}
        for word_a, word_b in zip(words, words[1:]):
            for char_a, char_b in zip(word_a, word_b):
                if char_a != char_b:
                    rev_adj_list[char_b].append(char_a)
                    break
            else:
                if len(word_b) < len(word_a):
                    return ''

        seen = {}
        res = []
        
        def dfs(node):
            if node in seen:
                return seen[node]
            
            seen[node] = False
            
            for neighbor in rev_adj_list[node]:
                ans = dfs(neighbor)
                if not ans:
                    return False
                
            seen[node] = True
            res.append(node)
            return True
        
        return ''.join(res) if all(dfs(node) for node in rev_adj_list) else ''


class Solution:
    def alienOrder(self, words: list[str]) -> str:
        reverse_adj_list = {char: [] for word in words for char in word}
        for word_a, word_b in zip(words, words[1:]):
            for char_a, char_b in zip(word_a, word_b):
                if char_a != char_b:
                    reverse_adj_list[char_b].append(char_a)
                    break
            else:
                if len(word_b) < len(word_a):
                    return ''

        seen = {}
        res = []
        
        def dfs(node):
            if node in seen:
                return seen[node];
            
            seen[node] = False
            
            for next_node in reverse_adj_list[node]:
                ans = dfs(next_node)
                if not ans:
                    return False
                
            seen[node] = True
            res.append(node)
            
            return True
        
        return ''.join(res) if all(dfs(node) for node in reverse_adj_list) else ''


class Solution:
    def alienOrder(self, words: list[str]) -> str:
        reverse_adj_list = {char: [] for word in words for char in word}
        for word_a, word_b in zip(words, words[1:]):
            for char_a, char_b in zip(word_a, word_b):
                if char_a != char_b:
                    reverse_adj_list[char_b].append(char_a)
                    break
            else:
                if len(word_b) < len(word_a):
                    return ''
                
        seen = {}
        res = []
        
        def dfs(node):
            if node in seen:
                return seen[node]
            
            seen[node] = False
            
            for next_node in reverse_adj_list[node]:
                ans = dfs(next_node)
                if not ans:
                    return False
                
            seen[node] = True
            res.append(node)
            
            return True
        
        if not all(dfs(node) for node in reverse_adj_list):
            return ''
        
        return ''.join(res)


## 
##############################
class Solution:
    def alienOrder(self, words: list[str]) -> str:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().alienOrder(["wrt","wrf","er","ett","rftt"]), "wertf")
        self.assertEqual(Solution().alienOrder(["z","x"]), "zx")
        self.assertEqual(Solution().alienOrder(["z","x","z"]), "")


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Breadth-First Search
#######################################

# - Let N be the total number of strings in the input list.
# - Let C be the total length of all the words in the input list, added together.
# - Let U be the total number of unique letters in the alien alphabet. While
#   this is limited to 26 in the question description, we'll still look at how
#   it would impact the complexity if it was not limited (as this could
#   potentially be a follow-up question).

# Time: O(C)
# - There were three parts to the algorithm; identifying all the relations,
#   putting them into an adjacency list, and then converting it into a valid
#   alphabet ordering.
# - In the worst case, the first and second parts require checking every letter
#   of every word (if the difference between two words was always in the last
#   letter). This is O(C).
# - For the third part, recall that a breadth-first search has a cost of
#   O(V + E), where V is the number of vertices and E is the number of edges.
#   Our algorithm has the same cost as BFS, as it too is visiting each edge and
#   node once (a node is visited once all of its edges are visited, unlike the
#   traditional BFS where it is visited once one edge is visited). Therefore,
#   determining the cost of our algorithm requires determining how many nodes
#   and edges there are in the graph.
# - Nodes: We know that there is one vertex for each unique letter,
#   i.e. O(U) vertices.
# - Edges: Each edge in the graph was generated from comparing two adjacent
#   words in the input list. There are N - 1 pairs of adjacent words, and only
#   one edge can be generated from each pair. This might initially seem a bit
#   surprising, so let's quickly look at an example. We'll use English words.
#       abacus
#       algorithm
# - The only conclusion we can draw is that b is before l. This is the reason
#   abacus appears before algorithm in an English dictionary. The characters
#   afterward are irrelevant. It is the same for the "alien" alphabets we're
#   working with here. The only rule we can draw is the one based on the first
#   difference between the two words.
# - Also, remember that we are only generating rules for adjacent words. We are
#   not adding the "implied" rules to the adjacency list. For example, assume
#   we have the following word list.
#       rgh
#       xcd
#       tny
#       bcd
# - We are only generating the following 3 edges.
#       r -> x
#       x -> t
#       t -> b
# - We are not generating these implied rules (the graph structure shows them
#   indirectly).
#       r -> t
#       r -> b
#       x -> b
# - So with this, we know that there are at most N - 1 edges.
# - There is an additional upper limit on the number of edges too—it is
#   impossible for there to be more than one edge between each pair of nodes.
#   With U nodes, this means there can't be more than U^2 edges.
# - It's not common in complexity analysis that we get two separate upper
#   bounds like this. Because the number of edges has to be lower than both
#   N - 1 and U^2, we know it is at most the smallest of these two values.
#   Mathematically, we can say this is min(U^2, N - 1).
# - Going all the way back to the cost of breadth first search, we can now
#   substiute in the number of nodes and the number of edges:
#   V = U and E = min(U^2, N - 1). This gives us:
#       O(V + E) = O(U + min(U^2, N - 1)) = O(U + min(U^2, N)).
# - Finally, we need to combine the two parts: O(C) for the first and second
#   parts, and O(U + min(U^2, N)) for the third part. When we have two
#   independent parts, we add the costs together, as we don't necessarily know
#   which is larger. After we've done this, we should look at the final formula
#   and see whether or not we can actually draw any conclusions about which is
#   larger. Adding them together, we initially get the following:
#       O(C) + O(U + min(U^2, N)) = O(C + U + min(U^2, N)).
# - So, what do we know about the relative values of N, C, and U? Well, we know
#   that N < C, as each word contains at least one character (remember, C is
#   total characters across the words, not unique characters). Additionally,
#   U < C because there can't be more unique characters than there are
#   characters.
# - In summary, C is the biggest of the three, and N and U are smaller,
#   although we don't know which is smaller out of those two.
# - So for starters, we know that the U bit is insignificant compared to the C.
#   Therefore, we can just remove it:
#       O(C + U + min(U^2, N)) → O(C + min(U^2, N))
# - Now, to simplify the rest, consider two cases:
#       1. If U^2 is smaller than N, then min(U^2, N) = U^2. By definition,
#          we've just said that U^22 is smaller than N, which is in turn
#          smaller than C, and so U^2 is definitely less than C. This leaves us
#          with O(C).
#       2. If U^2 is larger than N, then min(U^2, N) = N. Because C > N, we're
#          left with O(C).
# - So in all cases, we know that C > min(U^2, N). This gives us a final time
#   complexity of O(C).

# Space: O(1) or O(U + min(U^2, N))
# - The adjacency list uses the most auxiliary memory. This list uses O(V + E)
#   memory, where V is the number of unique letters, and E is the number of
#   relations.
# - The number of vertices is simply U; the number of unique letters.
# - The number of edges in the worst case is min(U^2, N),N), as explained in
#   the time complexity analysis.
# - So in total the adjacency list takes O(U + min(U^2, N)) space.
# - So for the question we're given, where U is a constant fixed at a maximum
#   of 26, the space complexity is simply O(1). This is because U is fixed at
#   26, and the number of relations is fixed at 26^2, so
#   O(min(26^2, N)) = O(26^2) = O(1).
# - But when we consider an arbitrarily large number of possible letters, we
#   use the size of the adjacency list; O(U + min(U^2, N)).

from collections import defaultdict, Counter, deque

def alienOrder(self, words: List[str]) -> str:
    
    # Step 0: create data structures + the in_degree of each unique letter to 0.
    adj_list = defaultdict(set)
    in_degree = Counter({c : 0 for word in words for c in word})
            
    # Step 1: We need to populate adj_list and in_degree.
    # For each pair of adjacent words...
    for first_word, second_word in zip(words, words[1:]):
        for c, d in zip(first_word, second_word):
            if c != d:
                if d not in adj_list[c]:
                    adj_list[c].add(d)
                    in_degree[d] += 1
                break
        else: # Check that second word isn't a prefix of first word.
            if len(second_word) < len(first_word): return ""
    
    # Step 2: We need to repeatedly pick off nodes with an indegree of 0.
    output = []
    queue = deque([c for c in in_degree if in_degree[c] == 0])
    while queue:
        c = queue.popleft()
        output.append(c)
        for d in adj_list[c]:
            in_degree[d] -= 1
            if in_degree[d] == 0:
                queue.append(d)
                
    # If not all letters are in output, that means there was a cycle and so
    # no valid ordering. Return "" as per the problem description.
    if len(output) < len(in_degree):
        return ""
    # Otherwise, convert the ordering we found into a string and return it.
    return "".join(output)


## Approach 2: Depth-First Search
#####################################
# Time: O(C)
# - Building the adjacency list has a time complexity of O(C) for the same
#   reason as in Approach 1.
# - Again, like in Approach 1, we traverse every "edge", but this time we're
#   using depth-first-search.
# Space: O(1) or O(U + min(U^2, N))
# - Like in Approach 1, we build an adjacency list. Even though this one is a
#   reversed adjacency list, it still contains the same number of relations.

def alienOrder(self, words: List[str]) -> str:

    # Step 0: Put all unique letters into the adj list.
    reverse_adj_list = {c : [] for word in words for c in word}

    # Step 1: Find all edges and put them in reverse_adj_list.
    for first_word, second_word in zip(words, words[1:]):
        for c, d in zip(first_word, second_word):
            if c != d: 
                reverse_adj_list[d].append(c)
                break
        else: # Check that second word isn't a prefix of first word.
            if len(second_word) < len(first_word): 
                return ""

    # Step 2: Depth-first search.
    seen = {} # False = grey, True = black.
    output = []
    def visit(node):  # Return True iff there are no cycles.
        if node in seen:
            return seen[node] # If this node was grey (False), a cycle was detected.
        seen[node] = False # Mark node as grey.
        for next_node in reverse_adj_list[node]:
            result = visit(next_node)
            if not result: 
                return False # Cycle was detected lower down.
        seen[node] = True # Mark node as black.
        output.append(node)
        return True

    if not all(visit(node) for node in reverse_adj_list):
        return ""

    return "".join(output)


