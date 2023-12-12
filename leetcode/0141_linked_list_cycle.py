##
#### 141. Linked List Cycle (easy)
########################################


## Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


## two-pointer (floyd's algorithm)
######################################
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head

        while fast and fast.next:
            head = head.next
            fast = fast.next.next

            if head == fast:
                return True

        return False


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False

            slow = slow.next
            fast = fast.next.next

        return True


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False

        fast = head.next

        while fast and fast.next:
            if head == fast:
                return True

            head = head.next
            fast = fast.next.next

        return False


## hash table
##############################
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seen = set()

        while head:
            if head in seen:
                return True

            seen.add(head)
            head = head.next

        return False


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seen = {head}

        while head:
            head = head.next

            if head in seen:
                return True

            seen.add(head)

        return False


## first attempt
##############################
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head

        while fast and fast.next:
            head = head.next
            fast = fast.next.next

            if head == fast:
                return True

        return False


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()


if __name__ == "__main__":
    unittest.main()
