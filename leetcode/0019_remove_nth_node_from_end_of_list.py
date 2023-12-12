##
#### 19. Remove Nth Node From End of List (medium)
######################################################


## Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


## one-pass
##############################
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sentinel = ListNode(None, head)
        slow = sentinel
        fast = head

        for _ in range(n):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next if slow.next else None

        return sentinel.next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sentinel = ListNode(None, head)
        left = sentinel
        right = head

        for _ in range(n):
            right = right.next

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return sentinel.next


## two-pass
##############################
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sentinel = ListNode(None, head)
        size = 0
        curr = head

        while curr:
            curr = curr.next
            size += 1

        curr = sentinel

        for i in range(size - n):
            curr = curr.next

        curr.next = curr.next.next

        return sentinel.next


## first attempt
##############################
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return

        sentinel = ListNode(None, head)
        size = 0
        curr = head

        while curr:
            curr = curr.next
            size += 1

        curr = sentinel

        for i in range(size - n):
            curr = curr.next

        curr.next = curr.next.next

        return sentinel.next


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()


if __name__ == "__main__":
    unittest.main()
