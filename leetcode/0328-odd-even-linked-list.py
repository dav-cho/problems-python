##
#### Odd Even Linked List (medium)
######################################

# Given the head of a singly linked list, group all the nodes with odd
# indices together followed by the nodes with even indices, and return
# the reordered list.

# The first node is considered odd, and the second node is even, and so on.

# Note that the relative order inside both the even and odd groups should
# remain as it was in the input.

# You must solve the problem in O(1) extra space complexity
# and O(n) time complexity.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]

# Example 2:
# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]
 
# Constraints:
# n == number of nodes in the linked list
# 0 <= n <= 104
# -106 <= Node.val <= 106

################################################################################

## Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def odd_even_list(self, head: ListNode) -> ListNode:
        if not head:
            return None

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
############

test1 = [1, 2, 3, 4, 5]         # [1, 3, 5, 2, 4]
test2 = [2, 1, 3, 5, 6, 4, 7]   # [2, 3, 6, 7, 1, 5, 4]


def test(*args):
    count = 1

    def run():
        for test in args:
            nonlocal count
            print("~ test", count)
            count += 1

            if not test:
                print('[]')
                continue

            head = ListNode(test[0])
            current = head

            for i in range(1, len(test)):
                current.next = ListNode(test[i])
                current = current.next

            print_LL(head)
            solution = Solution()
            result = solution.odd_even_list(head)
            print_LL(result)

    return run()


def print_LL(head):
    linked_list = []

    while head:
        linked_list.append(head.val)
        head = head.next

    print(linked_list)
        

test(test1, test2)

## LeetCode Solutions
#########################


## Approach 1: 
#################
# time: O(n) - there are total n nodes and we visit each node once
# space: O(1) - all we need is the four pointers

## Python
class Solution:
    def odd_even_list(self, head: ListNode) -> ListNode:
        if not head:
            return None

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

