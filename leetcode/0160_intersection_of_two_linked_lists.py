##
#### 160. Intersection of Two Linked Lists (easy)
#####################################################


from typing import Optional


## Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


## two-pointer
##############################
class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        a = headA
        b = headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        a = headA
        b = headB
        while a != b:
            a = headB if not a else a.next
            b = headA if not b else b.next

        return a


## hash table
##############################
class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        seen = set()
        while headA:
            seen.add(headA)
            headA = headA.next
        while headB:
            if headB in seen:
                return headB
            headB = headB.next

        return


## brute force (TLE)
##############################
class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        while headA:
            b = headB
            while b:
                if headA == b:
                    return headA
                b = b.next
            headA = headA.next

        return


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(
            Solution().getIntersectionNode([4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5]), 8
        )
        self.assertEqual(Solution().getIntersectionNode([1, 9, 1, 2, 4], [3, 2, 4]), 2)
        self.assertEqual(Solution().getIntersectionNode([2, 6, 4], [1, 5]), None)


if __name__ == "__main__":
    unittest.main()
