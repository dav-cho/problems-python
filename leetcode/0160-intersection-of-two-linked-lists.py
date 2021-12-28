##
#### Intersection of Two Linked Lists (easy)
################################################

# Given the heads of two singly linked-lists headA and headB, return the node
# at which the two lists intersect. If the two linked lists have no
# intersection at all, return null.

# For example, the following two linked lists begin to intersect at node c1:
#         a1 -> a2
#                  -> c2 -> c2 -> c3
#   b1 -> b2 -> b3
# The test cases are generated such that there are no cycles anywhere in the
# entire linked structure.

# Note that the linked lists must retain their original structure after the
# function returns.

# Custom Judge:
# The inputs to the judge are given as follows (your program is not given
# these inputs):
#   intersectVal - The value of the node where the intersection occurs.
#                  This is 0 if there is no intersected node.
#   listA - The first linked list.
#   listB - The second linked list.
#   skipA - The number of nodes to skip ahead in listA (starting from the head)
#           to get to the intersected node.
#   skipB - The number of nodes to skip ahead in listB (starting from the head)
#           to get to the intersected node.
# The judge will then create the linked structure based on these inputs and
# pass the two heads, headA and headB to your program. If you correctly return
# the intersected node, then your solution will be accepted.

# Example 1:
# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
# Output: Intersected at '8'
# Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
# From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

# Example 2:
# Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
# Output: Intersected at '2'
# Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
# From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

# Example 3:
# Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# Output: No intersection
# Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
# Explanation: The two lists do not intersect, so return null.
  
# Constraints:
# The number of nodes of listA is in the m.
# The number of nodes of listB is in the n.
# 1 <= m, n <= 3 * 104
# 1 <= Node.val <= 105
# 0 <= skipA < m
# 0 <= skipB < n
# intersectVal is 0 if listA and listB do not intersect.
# intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.

# Follow up: Could you write a solution that runs in O(m + n) time
#            and use only O(1) memory?

################################################################################

from typing import Optional


## Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

## two-pointer
##############################
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
            
        return a


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB
        while a != b:
            a = headB if not a else a.next
            b = headA if not b else b.next
            
        return a


## hash table
##############################
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
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
        self.assertEqual(Solution().getIntersectionNode([4,1,8,4,5], [5,6,1,8,4,5]), 8)
        self.assertEqual(Solution().getIntersectionNode([1,9,1,2,4], [3,2,4]), 2)
        self.assertEqual(Solution().getIntersectionNode([2,6,4], [1,5]), None)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Brute Force
##############################
# Let N be the length of list A and M be the length of list B.

# Time: O(N × M)
# - For each of the N nodes in list A, we are traversing over each of the nodes
#   in list B. In the worst case, we won't find a match, and so will need to do
#   this until reaching the end of list B, giving a worst-case time complexity
#   of O(N × M).
# Space: O(1)
# - We aren't allocating any additional data structures, so the amount of extra
#   space used does not grow with the size of the input.
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        while headA is not None:
            pB = headB
            while pB is not None:
                if headA == pB:
                    return headA
                pB = pB.next
            headA = headA.next

        return None


## Approach 2: Hash Table
##############################
# Time: O(N + M)
# - Firstly, we need to build up the hash table. It costs O(1) to insert an
#   item into a hash table, and we need to do this for each of the M nodes in
#   list B. This gives a cost of O(M) for building the hash table.
# - Secondly, we need to traverse list A, and for each node, we need to check
#   whether or not it is in the hash table. In the worst case, there will not
#   be a match, requiring us to check all N nodes in list A. As it is also
#   O(1) to check whether or not an item is in a hash table, this checking has
#   a total cost of O(N).
# - Finally, combining the two parts, we get O(M) + O(N) = O(M + N).
# Space: O(M)
# - As we are storing each of the nodes from list B into a hash table, the hash
#   table will require O(M) space. Note that we could have instead stored the
#   nodes of list A into the hash table, this would have been a space
#   complexity of O(N). Unless we know which list is longer though, it doesn't
#   make any real difference.
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodes_in_B = set()

        while headB is not None:
            nodes_in_B.add(headB)
            headB = headB.next

        while headA is not None:
            # if we find the node pointed to by headA,
            # in our set containing nodes of B, then return the node
            if headA in nodes_in_B:
                return headA
            headA = headA.next

        return None


## Approach 3: Two Pointers
##############################
# Let N be the length of list A and M be the length of list B.
# Time: O(N + M)
# - In the worst case, each list is traversed twice giving 2⋅M + 2⋅N, which is
#   equivalent to O(N + M). This is because the pointers firstly go down each
#   list so that they can be "lined up" and then in the second iteration, the
#   intersection node is searched for.
# - An interesting observation you might have made is that when the lists are
#   of the same length, this algorithm only traverses each list once. This is
#   because the pointers are already "lined up" from the start, so the
#   additional pass is unnecessary.
# Space: O(1)
# - We aren't allocating any additional data structures, so the amount of extra
#   space used does not grow with the size of the input. For this reason,
#   Approach 3 is better than Approach 2.
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA = headA
        pB = headB

        while pA != pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next

        return pA
        # Note: In the case lists do not intersect, the pointers for A and B
        # will still line up in the 2nd iteration, just that here won't be
        # a common node down the list and both will reach their respective ends
        # at the same time. So pA will be NULL in that case.


