##
#### Merge Two Sorted Lists (easy)
######################################

# Merge two sorted linked lists and return it as a sorted list. The list
# should be made by splicing together the nodes of the first two lists.

# Example 1:
# [1] -> [2] -> [3] 
# (1) -> (3) -> (4)
# (1) -> [1] -> [2] -> (3) -> [4] -> (4)
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: l1 = [], l2 = []
# Output: []

# Example 3:
# Input: l1 = [], l2 = [0]
# Output: [0]
 
# Constraints:
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both l1 and l2 are sorted in non-decreasing order.

################################################################################

from typing import Optional


## Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


## iterative
##############################
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(None)
        curr = sentinel
        
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
                
            curr = curr.next
            
        curr.next = l1 if l1 else l2
        
        return sentinel.next


## recursive
##############################
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


## first attempt
##############################
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(None)
        curr = sentinel
        
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
                
            curr = curr.next
            
        curr.next = l1 if l1 else l2
        
        return sentinel.next


## Tests
############

test1 = ([1, 2, 4], [1, 3, 4])  # [1, 1, 2, 3, 4, 4]
test2 = ([], [])                # []
test3 = ([], [0])               # [0]

def test(*args):
    count = 1

    def run():
        for test in args:
            nonlocal count
            print(f"~ test{count}")
            count += 1

            if not test[0]:
                head1 = []
            else:
                head1 = ListNode(test[0][0])
            if not test[1]:
                head2 = []
            else:
                head2 = ListNode(test[1][0])

            current1 = head1
            for i in range(1, len(test[0])):
                current1.next = ListNode(test[0][i])
                current1 = current1.next
            current2 = head2
            for i in range(1, len(test[1])):
                current2.next = ListNode(test[1][i])
                current2 = current2.next

            print_LL(head1, 'l1:')
            print_LL(head2, 'l2:')
            solution = Solution()
            result = solution.mergeTwoLists(head1, head2)
            print_LL(result, 'result:')

    return run()


def print_LL(head, msg="print_LL"):
    linked_list = []

    while head:
        linked_list.append(head.val)
        head = head.next

    print(msg, linked_list)


test(test1, test2, test3)


## LeetCode Solutions
#########################

## Approach 1: Recursion
##############################
# Time: O(n + m)
# - Because each recursive call increments the pointer to l1 or l2 by one
#   (approaching the dangling null at the end of each list), there will be
#   exactly one call to mergeTwoLists per element in each list. Therefore, the
#   time complexity is linear in the combined size of the lists.

# Space: O(n + m)
# - The first call to mergeTwoLists does not return until the ends of both l1
#   and l2 have been reached, so n + mn+m stack frames consume O(n + m) space.
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


## Approach 2: Iteration
##############################
# Time: O(n + m)
# - Because exactly one of l1 and l2 is incremented on each loop iteration, the
#   while loop runs for a number of iterations equal to the sum of the lengths
#   of the two lists. All other work is constant, so the overall complexity is
#   linear.

# Space: O(1)
# - The iterative approach only allocates a few pointers, so it has a constant
#   overall memory footprint.

class Solution:
    def mergeTwoLists(self, l1, l2):
        # maintain an unchanging reference to node ahead of the return node.
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next            
            prev = prev.next

        # At least one of l1 and l2 can still have nodes at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next


