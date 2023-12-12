"""
1456. Maximum Number of Vowels in a Substring of Given Length (medium)
"""


# Sliding window
# Time: O(n)
# Space: O(1)
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        ans = 0
        for char in s[:k]:
            if char in vowels:
                ans += 1

        curr = ans
        for i in range(k, len(s)):
            curr -= s[i - k] in vowels
            curr += s[i] in vowels
            ans = max(ans, curr)

        return ans
