"""
208. Implement Trie (Prefix Tree) (medium)
"""

from dataclasses import dataclass, field


class WithDict:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node["end"] = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            node = node.get(char)
            if not node:
                return False
        return node.get("end", False)

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            node = node.get(char)
            if not node:
                return False
        return True


# class Trie:
class FirstAttempt:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node.setdefault(char, {})
            node = node[char]
        node["end"] = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return "end" in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True


@dataclass
class SimpleNode:
    children: dict[str, "SimpleNode"] = field(default_factory=dict)
    end: bool = False


# class Trie:
class WithSimpleNode:
    def __init__(self):
        self.root = SimpleNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node.children.setdefault(char, SimpleNode())
            node = node.children[char]
        node.end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


@dataclass
class FancyNode:
    children: dict[str, "FancyNode"] = field(default_factory=dict)
    end: bool = False

    def setdefault(self, key: str, node: "FancyNode") -> None:
        self.children.setdefault(key, node)

    def __contains__(self, key: str) -> bool:
        return key in self.children

    def __getitem__(self, key: str) -> "FancyNode":
        return self.children[key]


# class Trie:
class WithFancyNode:
    def __init__(self):
        self.root = FancyNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node.setdefault(char, FancyNode())
            node = node[char]
        node.end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node.children[char]
        return node.end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
