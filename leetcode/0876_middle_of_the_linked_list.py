"""
876. Middle of the Linked List (easy)
"""

from typing import Optional
import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


## Naive
########################################################################################
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        length = 0
        root = head
        while root:
            length += 1
            root = root.next

        n = length // 2
        for _ in range(n):
            head = head.next
        return head


## Extra memory
########################################################################################
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []

        while head:
            nodes.append(head)
            head = head.next

        return nodes[len(nodes) // 2]


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = [head]
        while nodes[-1].next:
            nodes.append(nodes[-1].next)
        return nodes[len(nodes) // 2]


## Slow and Fast Pointers
########################################################################################
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


## Tests
########################################################################################


class Test(unittest.TestCase):
    def test_cases(self):
        ...


if __name__ == "__main__":
    unittest.main()
