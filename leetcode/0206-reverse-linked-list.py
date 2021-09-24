##
#### Reverse Linked List (easy)
###################################

# Given the head of a singly linked list,
# reverse the list, and return the reversed list.

# Example 1:
# 1 -> 2 -> 3 -> 4 -> 5
# 5 -> 4 -> 3 -> 2 -> 1
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# 1 -> 2
# 2 -> 1
# Input: head = [1,2]
# Output: [2,1]

# Example 3:
# Input: head = []
# Output: []

# Constraints:
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000

# Follow up: A linked list can be reversed either
# iteratively or recursively. Could you implement both?

######################################################################

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
        
        head.next.next = head;
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


## 
##############################
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass


## 
##############################
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: (Iterative) [Accepted]
#########################################
# Time: O(n) - Assume that n is the list's length, the time complexity is O(n).
# Space: O(1)

## Java
#public ListNode reverseList(ListNode head) {
#    ListNode prev = null;
#    ListNode curr = head;
#    while (curr != null) {
#        ListNode nextTemp = curr.next;
#        curr.next = prev;
#        prev = curr;
#        curr = nextTemp;
#    }
#    return prev;
#}


## Approach 2: (Recursive) [Accepted]
#########################################
# Time: O(n) - Assume that n is the list's length, the time complexity is O(n).
# Space: O(n) - The extra space comes from implicit stack space due to
#               recursion. The recursion could go up to n levels deep.

## Java
#public ListNode reverseList(ListNode head) {
#    if (head == null || head.next == null) return head;
#    ListNode p = reverseList(head.next);
#    head.next.next = head;
#    head.next = null;
#    return p;
#}


