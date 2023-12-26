"""
83. Remove Duplicates from Sorted List (easy)
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class FirstAttempt:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr:
            if curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next
                continue
            curr = curr.next
        return head
