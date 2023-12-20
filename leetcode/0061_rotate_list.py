"""
61. Rotate List (medium)
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head

        curr = head
        size = 1
        while curr.next:
            curr = curr.next
            size += 1
        curr.next = head
        k %= size

        tail = head
        for _ in range(size - k - 1):
            tail = tail.next
        new_head = tail.next
        tail.next = None

        return new_head
