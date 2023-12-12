"""
557. Reverse Words in a String III (easy)
"""


# Two Pointers
# time: O(n)
# space: O(1) (or O(n) if we consider the output)
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        for i, word in enumerate(words):
            w = list(word)
            l, r = 0, len(w) - 1
            while l < r:
                w[l], w[r] = w[r], w[l]
                l += 1
                r -= 1
            words[i] = "".join(w)
        return " ".join(words)


# Brute Force
# time: O(n)
# space: O(1) (or O(n) if we consider the output)
class Solution2:
    def reverseWords(self, s: str) -> str:
        words = []

        for word in s.split():
            curr = [c for c in word[::-1]]
            words.append("".join(curr))

        return " ".join(words)
