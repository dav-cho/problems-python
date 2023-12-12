"""
2000. Reverse Prefix of Word (easy)
"""


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        try:
            idx = word.index(ch)
            return word[: idx + 1][::-1] + word[idx + 1 :]
        except:
            return word


class Solution2:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)
        if idx:
            return word[: idx + 1][::-1] + word[idx + 1 :]
        return word


class Solution3:
    def reversePrefix(self, word: str, ch: str) -> str:
        prefix = ""
        for i, c in enumerate(word):
            if c == ch:
                return (prefix + c)[::-1] + word[i + 1 :]
            prefix += c
        return prefix


class Attempt1:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word

        idx = word.index(ch)

        return "".join(word[i] for i in range(idx, -1, -1)) + word[idx + 1 :]
