##
#### 49. Group Anagrams (medium)
########################################

from collections import defaultdict


## letter count
##############################
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1
            res[tuple(count)].append(word)

        return res.values()


## sorting
##############################
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for word in strs:
            res[tuple(sorted(word))].append(word)

        return res.values()


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertCountEqual(
            Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        )
        self.assertCountEqual(Solution().groupAnagrams([""]), [[""]])
        self.assertCountEqual(Solution().groupAnagrams(["a"]), [["a"]])


if __name__ == "__main__":
    unittest.main()
