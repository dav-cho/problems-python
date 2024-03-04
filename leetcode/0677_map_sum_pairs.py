"""
677. Map Sum Pairs (medium)
"""

from dataclasses import dataclass, field


@dataclass
class Node:
    children: dict[str, "Node"] = field(default_factory=dict)
    score: int = 0


# class MapSum:
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


# class MapSum:
class WithDict:
    def __init__(self):
        self.root = {"children": {}, "score": 0}
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        node = self.root
        node["score"] += delta
        for char in key:
            node = node["children"].setdefault(char, {"children": {}, "score": 0})
            node["score"] += delta

    def sum(self, prefix: str) -> int:
        node = self.root
        for char in prefix:
            if char not in node["children"]:
                return 0
            node = node["children"][char]
        return node["score"]
