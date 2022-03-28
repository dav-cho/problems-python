##
#### 269. Alien Dictionary (hard)
########################################

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
                    return ""

        res = []
        queue = deque([char for char in indegree if indegree[char] == 0])
        while queue:
            char = queue.popleft()
            res.append(char)
            for neighbor in adj_list[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return "".join(res) if len(res) == len(indegree) else ""


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
                    return ""

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

        return "".join(res) if all(dfs(node) for node in rev_adj_list) else ""


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
                    return ""

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

        return "".join(res) if all(dfs(node) for node in reverse_adj_list) else ""


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
                    return ""

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
            return ""

        return "".join(res)


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
        self.assertEqual(
            Solution().alienOrder(["wrt", "wrf", "er", "ett", "rftt"]), "wertf"
        )
        self.assertEqual(Solution().alienOrder(["z", "x"]), "zx")
        self.assertEqual(Solution().alienOrder(["z", "x", "z"]), "")


if __name__ == "__main__":
    unittest.main()
