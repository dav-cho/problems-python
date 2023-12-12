"""
1941. Check if All Characters Have Equal Number of Occurrences (easy)
"""
from collections import Counter
from typing import DefaultDict


class Solution1:
    """First attempt.

    Time complexity: O(n)
    Space complexity: O(k)

    Some people would argue that this is O(1) since the characters come from
    the English alphabet, which is bounded by a constant. A more general answer
    would be to say that the space complexity is O(k), where k is the number of
    characters that could be in the input, which happens to be 26 in this
    problem."""

    def areOccurrencesEqual(self, s: str) -> bool:
        counts = DefaultDict(int)
        for char in s:
            counts[char] += 1

        return len(set(counts.values())) == 1


class Solution2:
    """Using colletions.Counter.

    Time complexity: O(n)
    Space complexity: O(k)
    """

    def areOccurrencesEqual(self, s: str) -> bool:
        return len(set(Counter(s).values())) == 1
