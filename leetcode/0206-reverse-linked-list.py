##
#### 206. Reverse Linked List (easy)
########################################


from typing import Optional

## Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


## iterative
##############################
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            head.next, prev, head = prev, head, head.next

        return prev


## recursive
##############################
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return prev


## first attempt
##############################
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            nxt = head.next

            head.next = prev
            prev = head
            head = nxt

        return prev


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()


if __name__ == "__main__":
    unittest.main()
