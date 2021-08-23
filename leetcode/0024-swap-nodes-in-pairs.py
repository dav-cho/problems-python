##
#### Swap Nodes in Pairs (medium)
#####################################

# Given a linked list, swap every two adjacent nodes and return its head. You
# must solve the problem without modifying the values in the list's nodes
# (i.e., only nodes themselves may be changed.)

# Example 1:
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]

# Example 2:
# Input: head = []
# Output: []

# Example 3:
# Input: head = [1]
# Output: [1]
 
# Constraints:
# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100

################################################################################

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


## Tests
#############

#import unittest
#
#
#class Test(unittest.TestCase):
#    def test_cases(self):
#        solution = Solution()
#        head = self.build_ll([1,2,3,4])
#        self.print_ll(head)
#        self.assertEqual(solution.swapPairs(head), [2,1,4,3])
#
#        head = self.build_ll([])
#        self.print_ll(head)
#        #self.assertEqual(solution.swapPairs([]), [])
#
#        head = self.build_ll([1])
#        self.print_ll(head)
#        #self.assertEqual(solution.swapPairs([1]), [1])
#
#    def build_ll(self, arr):
#        head = ListNode(arr[0])
#        prev = head
#        for num in arr[1:]:
#            new = ListNode(num)
#            prev.next = new
#            prev = prev.next
#        return head
#
#    def print_ll(self, head):
#        res = []
#        while head:
#            res.append(head.val)
#            head = head.next
#        print(res)
#        return res
#
#
#if __name__ == "__main__":
#    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Recursive Approach
#####################################
# Time: O(N) - Where N is the size of the linked list.
# Space: O(N) - Stack space utilized for recursion.
class Solution(object):
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # If the list has no node or has only one node left.
        if not head or not head.next:
            return head

        # Nodes to be swapped
        first_node = head
        second_node = head.next

        # Swapping
        first_node.next  = self.swapPairs(second_node.next)
        second_node.next = first_node

        # Now the head is the second node
        return second_node


## Approach 2: Iterative Approach
#####################################
# Time: O(N) - Where N is the size of the linked list.
# Space: O(1)
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Dummy node acts as the prevNode for the head node
        # of the list and hence stores pointer to the head node.
        dummy = ListNode(-1)
        dummy.next = head

        prev_node = dummy

        while head and head.next:

            # Nodes to be swapped
            first_node = head;
            second_node = head.next;

            # Swapping
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # Reinitializing the head and prev_node for next swap
            prev_node = first_node
            head = first_node.next

        # Return the new head node.
        return dummy.next


