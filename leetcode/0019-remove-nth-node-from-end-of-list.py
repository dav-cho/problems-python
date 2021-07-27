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


## two pass
###############
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        M = 0
        curr = head
        while curr is not None:
            M += 1
            curr = curr.next

        M -= n
        curr = dummy
        while M > 0:
            M -= 1
            curr = curr.next

        curr.next = curr.next.next

        return head


## one pass
###############
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        left = right = head

        for _ in range(n):
            right = right.next
        
        if not right:
            return head.next

        while right.next:
            right = right.next
            left = left.next

        left.next = left.next.next

        return head


## Tests
############


## LeetCode Solutions
#########################

## Approach 1: Two pass algorithm
#####################################
# time: O(L) - The algorithm makes two traversal of the list, first to
#              calculate list length L and second to find the (L - n)th node.
#              There are 2L-n operations and time complexity is O(L).
# space: O(1) - no extra space used

# Intuition:
# We notice that the problem could be simply reduced to another one:
# Remove the (L - n + 1)th node from the beginning in the list, where L is
# the list length. This problem is easy to solve once we found list length L.

# Algorithm:
# First we will add an auxiliary "dummy" node, which points to the list head.
# The "dummy" node is used to simplify some corner cases such as a list with
# only one node, or removing the head of the list. On the first pass, we find
# the list length L. Then we set a pointer to the dummy node and start to move
# it through the list till it comes to the (L - n)th node. We relink next
# pointer of the (L - n)th node to the (L - n + 2)th node and we are done.

# Implementation:
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pass

## Approach 2: One pass algorithm
#####################################
# time: 
# space: 

# Algorithm:
# The above algorithm could be optimized to one pass. Instead of one pointer,
# we could use two pointers. The first pointer advances the list by n+1 steps
# from the beginning, while the second pointer starts from the beginning of
# the list. Now, both pointers are exactly separated by nn nodes apart. We
# maintain this constant gap by advancing both pointers together until the
# first pointer arrives past the last node. The second pointer will be
# pointing at the nnth node counting from the last. We relink the next pointer
# of the node referenced by the second pointer to point to the node's next
# next node.

# Implementation
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pass


