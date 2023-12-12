"""
2. Add Two Numbers (medium)
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        sentinel = ListNode(None)
        curr = sentinel
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, val = divmod(carry, 10)
            curr.next = ListNode(val)
            curr = curr.next
        return sentinel.next


class ConvertToString:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        while l1:
            num1 += str(l1.val)
            l1 = l1.next

        num2 = ""
        while l2:
            num2 += str(l2.val)
            l2 = l2.next

        sum = [int(x) for x in (str(int(num1[::-1]) + int(num2[::-1])))][::-1]
        head = curr = ListNode(sum[0])

        for i in range(1, len(sum)):
            curr.next = ListNode(sum[i])
            curr = curr.next

        return head
