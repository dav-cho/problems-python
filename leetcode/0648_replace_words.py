"""
648. Replace Words (medium)
"""

from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = {}
        for word in dictionary:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node["end"] = word

        def replace(word: str) -> str:
            node = trie
            for char in word:
                if char not in node:
                    break
                node = node[char]
                if "end" in node:
                    return node["end"]
            return word

        return " ".join(map(replace, sentence.split()))


class SecondAttemptImproved:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = {}
        for word in dictionary:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node["end"] = word

        words = []
        for word in sentence.split():
            node = trie
            for char in word:
                if char not in node:
                    break
                node = node[char]
                if "end" in node:
                    words.append(node["end"])
                    break
            if "end" not in node:
                words.append(word)

        return " ".join(words)


# Accepted
class SecondAttempt:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = {}
        for word in dictionary:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node["end"] = True

        words = {(i, word): word for i, word in enumerate(sentence.split())}
        for i, word in words:
            node = trie
            chars = []
            for char in word:
                if char not in node:
                    break
                if "end" in node:
                    words[(i, word)] = [word, "".join(chars)][len(chars) < len(word)]
                    break
                node = node[char]
                chars.append(char)
            if node.get("end"):
                words[(i, word)] = [word, "".join(chars)][len(chars) < len(word)]
        return " ".join(words.values())


# Fail
class FirstAttempt:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = {}
        for word in dictionary:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node["end"] = True

        words = {(i, word): word for i, word in enumerate(sentence.split())}
        for i, word in words:
            node = trie
            chars = []
            for char in word:
                if char not in node:
                    break
                node = node[char]
                chars.append(char)
            if node.get("end"):
                root = "".join(chars)
                words[(i, word)] = [word, root][len(root) < len(word)]
        return " ".join(words.values())
