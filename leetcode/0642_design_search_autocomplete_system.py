"""
642. Design Search Autocomplete System (hard)
"""

from collections import defaultdict
from typing import List


class TrieDict:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = self.node = {}
        self.sentence = []

        for sentence, count in zip(sentences, times):
            self.add(sentence, count)

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.add("".join(self.sentence), 1)
            self.sentence.clear()
            self.node = self.root
            return []

        self.sentence.append(c)
        if c not in self.node:
            self.node = {}
            return []

        self.node = self.node[c]
        counts = sorted(self.node["counts"].items(), key=lambda x: (-x[1], x[0]))
        return [count[0] for count in counts[:3]]

    def add(self, sentence: str, count: int) -> None:
        node = self.root
        for char in sentence:
            node = node.setdefault(char, {"counts": {}})
            node["counts"][sentence] = node["counts"].get(sentence, 0) + count


class Node:
    def __init__(self) -> None:
        self.children = {}
        self.counts = defaultdict(int)


class TrieNodeDead:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = self.node = Node()
        self.sentence = []
        self.dead = Node()

        for sentence, count in zip(sentences, times):
            self.add(sentence, count)

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.add("".join(self.sentence), 1)
            self.sentence.clear()
            self.node = self.root
            return []

        self.sentence.append(c)
        self.node = self.node.children.get(c, self.dead)
        if self.node is self.dead:
            return []

        counts = sorted(self.node.counts.items(), key=lambda x: (-x[1], x[0]))
        return [count[0] for count in counts[:3]]

    def add(self, sentence: str, count: int) -> None:
        node = self.root
        for char in sentence:
            node = node.children.setdefault(char, Node())
            node.counts[sentence] += count


class TrieNode:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = self.node = Node()
        self.sentence = []

        for sentence, count in zip(sentences, times):
            self.add(sentence, count)

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.add("".join(self.sentence), 1)
            self.sentence.clear()
            self.node = self.root
            return []

        self.sentence.append(c)
        if c not in self.node.children:
            self.node = Node()
            return []

        self.node = self.node.children[c]
        counts = sorted(self.node.counts.items(), key=lambda x: (-x[1], x[0]))
        return [count[0] for count in counts[:3]]

    def add(self, sentence: str, count: int) -> None:
        node = self.root
        for char in sentence:
            node = node.children.setdefault(char, Node())
            node.counts[sentence] += count


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
