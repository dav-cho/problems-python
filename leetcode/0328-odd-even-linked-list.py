##
#### Odd Even Linked List (medium)
########################################

# Given the head of a singly linked list, group all the nodes with odd indices
# together followed by the nodes with even indices, and return the reordered
# list.

# The first node is considered odd, and the second node is even, and so on.

# Note that the relative order inside both the even and odd groups should
# remain as it was in the input.

# You must solve the problem in O(1) extra space complexity and O(n) time
# complexity.

# Example 1:
#   before: 1 -> 2 -> 3 -> 4 -> 5
#   after:  1 -> 3 -> 5 -> 2 -> 4
# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]

# Example 2:
#   before: 2 -> 1 -> 3 -> 5 -> 6 -> 4 -> 7
#   after:  2 -> 3 -> 6 -> 7 -> 1 -> 5 -> 4
# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]
 
# Constraints:
# n == number of nodes in the linked list
# 0 <= n <= 104
# -106 <= Node.val <= 106

################################################################################

from typing import Optional

## Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


## 
##############################
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = head
        even = head.next
        even_head = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
            
        odd.next = even_head
        return head


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().oddEvenList([1,2,3,4,5]), [1,3,5,2,4])
        self.assertEqual(Solution().oddEvenList([2,1,3,5,6,4,7]), [2,3,6,7,1,5,4])


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: 
##############################
# Time: O(n) - There are total n nodes and we visit each node once.
# Space: O(1) - All we need is the four pointers.

## Java
# public class Solution {
#     public ListNode oddEvenList(ListNode head) {
#         if (head == null) return null;
#         ListNode odd = head, even = head.next, evenHead = even;
#         while (even != null && even.next != null) {
#             odd.next = even.next;
#             odd = odd.next;
#             even.next = odd.next;
#             even = even.next;
#         }
#         odd.next = evenHead;
#         return head;
#     }
# }


