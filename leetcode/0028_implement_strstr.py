"""
28. Implement strStr() (easy)
"""


class SlidingWindow:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        for i in range(len(haystack) - n + 1):
            if needle == haystack[i : i + n]:
                return i
        return -1


class FirstAttempt:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        n = len(needle)
        for i in range(len(haystack) - n + 1):
            if needle == haystack[i : i + n]:
                return i
        return -1
