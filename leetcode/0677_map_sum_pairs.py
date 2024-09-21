"""
677. Map Sum Pairs (medium)
"""

from dataclasses import dataclass, field


@dataclass
class Node:
    children: dict[str, "Node"] = field(default_factory=dict)
    score: int = 0


class WithNode:
    def __init__(self):
        self.root = Node()
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        node = self.root
        node.score += delta
        for char in key:
            node = node.children.setdefault(char, Node())
            node.score += delta

    def sum(self, prefix: str) -> int:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.score


class WithDict:
    def __init__(self):
        self.root = {}
        self.keys = {}

    def insert(self, key: str, val: int) -> None:
        diff = val - self.keys.get(key, 0)
        self.keys[key] = val
        node = self.root
        node["score"] = node.get("score", 0) + diff
        for char in key:
            node = node.setdefault(char, {})
            node["score"] = node.get("score", 0) + diff

    def sum(self, prefix: str) -> int:
        node = self.root
        for char in prefix:
            if char not in node:
                return 0
            node = node[char]
        return node["score"]


class WithDict2:
    def __init__(self):
        self.trie = {}
        self.keys = {}

    def insert(self, key: str, val: int) -> None:
        diff = val - self.keys.get(key, 0)
        self.keys[key] = val
        node = self.trie
        node["score"] = node.get("score", 0) + diff
        for char in key:
            node = node.setdefault(char, {"score": 0})
            node["score"] += diff

    def sum(self, prefix: str) -> int:
        node = self.trie
        for char in prefix:
            node = node.get(char)
            if not node:
                return 0
        return node["score"]


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
