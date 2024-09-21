"""
242. Valid Anagram (easy)
"""

from collections import Counter


class LoopOnce:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        if n != len(t):
            return False

        counts = {}
        for i in range(n):
            counts[s[i]] = counts.setdefault(s[i], 0) + 1
            counts[t[i]] = counts.setdefault(t[i], 0) - 1

        return all(v == 0 for v in counts.values())


class NoCounter:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = {}
        for char in s:
            counts[char] = counts.setdefault(char, 0) + 1

        for char in t:
            if char not in counts:
                return False
            counts[char] -= 1
            if counts[char] == 0:
                del counts[char]

        return True


class WithCounter:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = Counter(s)
        for char in t:
            if char not in counts:
                return False
            counts[char] -= 1
            if counts[char] == 0:
                del counts[char]

        return True
