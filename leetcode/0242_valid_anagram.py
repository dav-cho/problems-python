##
#### 242. Valid Anagram (easy)
########################################


## first attempt
##############################
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts_s = Counter(s)
        counts_t = Counter(t)

        return counts_s == counts_t


## sorting
##############################
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)

        return s == t


## hash table
##############################
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = defaultdict(int)

        for i in range(len(s)):
            counts[s[i]] += 1
            counts[t[i]] -= 1

        for count in counts.values():
            if count != 0:
                return False

        return True


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = [0] * 26

        for i in range(len(s)):
            counts[ord(s[i]) - 97] += 1
            counts[ord(t[i]) - 97] -= 1

        for count in counts:
            if count != 0:
                return False

        return True


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.isAnagram("anagram", "nagaram"), True)
        self.assertEqual(solution.isAnagram("rat", "car"), False)
        self.assertEqual(solution.isAnagram("a", "ab"), False)


if __name__ == "__main__":
    unittest.main()
