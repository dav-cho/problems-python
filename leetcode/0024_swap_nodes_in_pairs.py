##
#### 24. Swap Nodes in Pairs (medium)
#########################################


from typing import Optional

## Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


## recursive
##############################
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        a, b = head, head.next
        a.next = self.swapPairs(b.next)
        b.next = a

        return b


## iterative
##############################
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(None)
        sentinel.next = head

        prev = sentinel
        while head and head.next:
            a, b = head, head.next

            prev.next = b
            a.next = b.next
            b.next = a

            prev = a
            head = a.next

        return sentinel.next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(None)
        sentinel.next = head
        prev = sentinel
        while head and head.next:
            a, b = head, head.next
            prev.next, a.next, b.next = b, b.next, a
            prev, head = a, a.next

        return sentinel.next
