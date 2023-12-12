"""
1832. Check if the Sentence Is Pangram (easy)
"""


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
