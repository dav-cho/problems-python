##
#### Add Two Numbers (medium)
#################################

# You are given two non-empty linked lists representing two
# non-negative integers. The digits are stored in reverse order,
# and each of their nodes contains a single digit. Add the
# two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any
# leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Constraints:
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number
# that does not have leading zeros.

# Follow up:
# What if the the digits in the linked list are stored in non-reversed order?

# For example:
# (3 -> 4 -> 2) + (4 -> 6 -> 5) = 8 -> 0 -> 7

################################################################################

## Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


## convert to string
########################
class Solution:
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        while l1:
            num1 += str(l1.val)
            l1 = l1.next

        num2 = ""
        while l2:
            num2 += str(l2.val)
            l2 = l2.next

        sum = [int(x) for x in (str(int(num1[::-1]) + int(num2[::-1])))][::-1]
        head = curr = ListNode(sum[0])

        for i in range(1, len(sum)):
            curr.next = ListNode(sum[i])
            curr = curr.next

        return head


## simple math
##################
class Solution:
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sentinel = curr = ListNode(None)
        carry = 0
        while l1 or l2 or carry:
            x = y = 0
            if l1:
                x = l1.val
                l1 = l1.next
            if l2:
                y = l2.val
                l2 = l2.next

            carry, val = divmod(x + y + carry, 10)
            curr.next = ListNode(val)
            curr = curr.next

        return sentinel.next


## simple math 2
####################
class Solution:
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sentinel = curr = ListNode(None)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            carry, val = divmod(carry, 10)
            curr.next = ListNode(val)
            curr = curr.next

        return sentinel.next

## Tests
############

test1 = ([2, 4, 3], [5, 6, 4])  # [7, 0, 8]
test2 = ([0], [0])              # [0]
test3 = (
    [9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9]
)                               # [8, 9, 9, 9, 0, 0, 0, 1]

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
            result = solution.add_two_numbers(head1, head2)
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

## Approach 1: Elementary Math
##################################
# time: O(max(m, n)) - Assume that mm and nn represents the length of l1 and
#                      l2 respectively, the algorithm above iterates at most
#                      max(m, n) times.

# space: O(max(m, n)) - The length of the new list is at most max(m, n) + 1.

# Intuition:
# Keep track of the carry using a variable and simulate digits-by-digits sum
# starting from the head of list, which contains the least-significant digit.

# Algorithm:
# Just like how you would sum two numbers on a piece of paper, we begin by
# summing the least-significant digits, which is the head of l1l1 and l2l2.
# Since each digit is in the range of 0 \ldots 90…9, summing two digits may
# "overflow". For example 5 + 7 = 125+7=12. In this case, we set the current
# digit to 22 and bring over the carry = 1carry=1 to the next iteration.
# carrycarry must be either 00 or 11 because the largest possible sum of
# two digits (including the carry) is 9 + 9 + 1 = 199+9+1=19.

# The pseudocode is as following:
# - Initialize current node to dummy head of the returning list.
# - Initialize carry to 0.
# - Initialize p and q to head of l1 and l2 respectively.
# - Loop through lists l1 and l2 until you reach both ends.
# - Set x node p's value. If p has reached the end of l1, set to 0.
# - Set y to node q's value. If q has reached the end of l2, set to 0.
# - Set sum = x + y + carry.
# - Update carry = sum / 10.
# - Create a new node with the digit value of (sum \bmod 10) and set it to
#   current node's next, then advance current node to next.
# - Advance both p and q.
# - Check if carry = 1, if so append a new node with digit 1 to the returning
#   list.
# - Return dummy head's next node.

# Note that we use a dummy head to simplify the code. Without a dummy head,
# you would have to write extra conditional statements to initialize the
# head's value.

# Take extra caution of the following cases:
# - When one list is longer than the other
#       l1 = [0, 1]
#       l2 = [0, 1, 2]
# - When one list is null, which means an empty list
#       l1 = []
#       l2 = [0, 1]
# - The sum could have an extra carry of one at the end,
#   which is easy to forget
#       l1 = [9, 9]
#       l2 = [1]

# Implementation:

## Java
# public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
#     ListNode dummyHead = new ListNode(0);
#     ListNode p = l1, q = l2, curr = dummyHead;
#     int carry = 0;
#     while (p != null || q != null) {
#         int x = (p != null) ? p.val : 0;
#         int y = (q != null) ? q.val : 0;
#         int sum = carry + x + y;
#         carry = sum / 10;
#         curr.next = new ListNode(sum % 10);
#         curr = curr.next;
#         if (p != null) p = p.next;
#         if (q != null) q = q.next;
#     }
#     if (carry > 0) {
#         curr.next = new ListNode(carry);
#     }
#     return dummyHead.next;
# }


