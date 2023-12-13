"""
708. Insert into a Sorted Circular Linked List (medium)
"""

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val: int, next: Node = None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: Optional[Node], insertVal: int) -> "Node":
        node = Node(insertVal)
        if not head:
            node.next = node
            return node
        curr = head
        while True:
            if curr.val <= insertVal <= curr.next.val:
                break
            if curr.val > curr.next.val and (
                insertVal >= curr.val or insertVal <= curr.next.val
            ):
                break
            curr = curr.next
            if curr == head:
                break
        node.next = curr.next
        curr.next = node
        return head
