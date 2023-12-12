"""
430. Flatten a Multilevel Doubly Linked List (medium)
"""

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Iterative:
    def flatten(self, head: Optional[Node]) -> Optional[Node]:
        curr = head
        while curr:
            if not curr.child:
                curr = curr.next
                continue
            tail = curr.child
            while tail.next:
                tail = tail.next
            tail.next = curr.next
            if curr.next:
                curr.next.prev = tail
            curr.next = curr.child
            curr.child.prev = curr
            curr.child = None
        return head


class Recursive:
    def flatten(self, head: Optional[Node]) -> Optional[Node]:
        def _flatten(prev: Node, curr: Optional[Node]) -> ...:
            if not curr:
                return prev
            prev.next = curr
            curr.prev = prev
            nxt = curr.next
            tail = _flatten(curr, curr.child)
            curr.child = None
            return _flatten(tail, nxt)

        sentinel = Node(None, None, head, None)
        _flatten(sentinel, head)
        if sentinel.next:
            sentinel.next.prev = None
        return sentinel.next


## stack
############
class Solution:
    def flatten(self, head: "Node") -> "Node":
        if not head:
            return

        sentinel = Node(None, None, head, None)
        stack = [head]
        prev = sentinel
        while stack:
            curr = stack.pop()
            curr.prev = prev
            prev.next = curr

            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
            prev = curr

        sentinel.next.prev = None
        return sentinel.next


### dfs recursive
#####################
class Solution:
    def flatten(self, head: "Node") -> "Node":
        if not head:
            return

        sentinel = Node(None, None, head, None)
        self.flatten_dfs(sentinel, head)
        sentinel.next.prev = None

        return sentinel

    def flatten_dfs(self, prev, curr):
        if not curr:
            return prev

        curr.prev, prev.next = prev, curr
        temp_next = curr.next
        tail = self.flatten_dfs(curr, curr.child)
        curr.child = None

        return self.flatten_dfs(tail, temp_next)


## dfs iterative
####################
class Solution:
    def flatten(self, head: "Node") -> "Node":
        if not head:
            return

        sentinel = Node(None, None, head, None)
        prev = sentinel

        stack = [head]
        while stack:
            curr = stack.pop()
            prev.next, curr.prev = curr, prev

            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
                curr.child = None

            prev = curr

        sentinel.next.prev = None

        return sentinel.next
