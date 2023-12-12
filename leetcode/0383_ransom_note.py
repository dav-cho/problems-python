"""
383. Ransom Note (easy)
"""

from collections import Counter
import unittest


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = Counter(magazine)
        for c in ransomNote:
            if c not in counts:
                return False
            counts[c] -= 1
            if counts[c] < 0:
                return False
        return True


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = [*magazine]
        for c in ransomNote:
            if c not in magazine:
                return False
            magazine.pop(magazine.index(c))
        return True


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        m_counts = Counter(magazine)
        r_counts = Counter(ransomNote)

        for char, count in r_counts.items():
            print(m_counts[char])
            if m_counts[char] < count:
                return False

        return True


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        counts = Counter(magazine)
        for c in ransomNote:
            if counts[c] <= 0:
                return False
            counts[c] -= 1

        return True


## Tests
########################################################################################


class Test(unittest.TestCase):
    def test_cases(self):
        for ransom_note, magazine, expected in [
            ("a", "b", False),
            ("aa", "ab", False),
            ("aa", "aab", True),
        ]:
            self.assertEqual(Solution().canConstruct(ransom_note, magazine), expected)


if __name__ == "__main__":
    unittest.main()
