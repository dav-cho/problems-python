##
#### Remove Nth Node From End of List (medium)
##################################################

# Given the head of a linked list, remove the nth node from the end of
# the list and return its head.

# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []

# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]
 
# Constraints:
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
 
# Follow up: Could you do this in one pass?

################################################################################

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
        size = 0
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


## 
##############################
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pass


## 
##############################
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
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

## Approach 1: Two pass algorithm
#####################################
# Time: O(L) - The algorithm makes two traversal of the list, first to calculate
#              list length L and second to find the (L−n)th node. There are 2L−n
#              operations and time complexity is O(L).
# Space: O(1) - We only used constant extra space.

## Java
#public ListNode removeNthFromEnd(ListNode head, int n) {
#    ListNode dummy = new ListNode(0);
#    dummy.next = head;
#    int length  = 0;
#    ListNode first = head;
#    while (first != null) {
#        length++;
#        first = first.next;
#    }
#    length -= n;
#    first = dummy;
#    while (length > 0) {
#        length--;
#        first = first.next;
#    }
#    first.next = first.next.next;
#    return dummy.next;
#}


## Approach 2: One pass algorithm
#####################################
# Time: O(L) - The algorithm makes one traversal of the list of L nodes.
#              Therefore time complexity is O(L).
# Space: O(1) - We only used constant extra space.

## Java
#public ListNode removeNthFromEnd(ListNode head, int n) {
#    ListNode dummy = new ListNode(0);
#    dummy.next = head;
#    ListNode first = dummy;
#    ListNode second = dummy;
#    // Advances first pointer so that the gap between first and second is n nodes apart
#    for (int i = 1; i <= n + 1; i++) {
#        first = first.next;
#    }
#    // Move first to the end, maintaining the gap
#    while (first != null) {
#        first = first.next;
#        second = second.next;
#    }
#    second.next = second.next.next;
#    return dummy.next;
#}


