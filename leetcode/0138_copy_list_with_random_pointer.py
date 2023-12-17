"""
138. Copy List with Random Pointer (medium)
"""

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(
        self, x: int, next: Optional["Node"] = None, random: Optional["Node"] = None
    ):
        self.val = int(x)
        self.next = next
        self.random = random


class Recursive:
    seen = {}

    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None
        if head in self.seen:
            return self.seen[head]
        node = Node(head.val)
        self.seen[head] = node
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node


class Iterative1:
    """Space: O(n)"""

    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        def clone(node: Optional["Node"]) -> Optional["Node"]:
            if not node:
                return None
            if node not in seen:
                seen[node] = Node(node.val)
            return seen[node]

        if not head:
            return None
        seen = {}
        curr = head
        copy = clone(curr)
        while curr:
            copy.next = clone(curr.next)
            copy.random = clone(curr.random)
            curr = curr.next
            copy = copy.next
        return seen[head]


class Iterative2:
    """Space: O(1)"""

    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        curr = head
        while curr:
            clone = Node(curr.val)
            clone.next = curr.next
            curr.next = clone
            curr = clone.next

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        curr = head
        clone = head.next
        clone_head = head.next
        while curr:
            curr.next = curr.next.next
            if clone.next:
                clone.next = clone.next.next
            curr = curr.next
            clone = clone.next

        return clone_head
