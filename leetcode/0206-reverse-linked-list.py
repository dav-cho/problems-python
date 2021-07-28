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

## Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


## iterative 1
##################
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head    
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            
        return prev


## iterative 2
##################
class Solution:
    def reverse_list(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        return prev


## iterative 3
##################
class Solution:
    def reverse_list(self, head: ListNode) -> ListNode:
        prev = None

        while head:
            head.next, prev, head = prev, head, head.next

        return prev


## recursive
################
class Solution:
    def reverse_list(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        p = self.reverse_list(head.next)
        head.next.next = head
        head.next = None

        return p


## Tests
############

test1 = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]
test2 = [1, 2]              # [2, 1]
test3 = []                  # []


def test(*args):
    count = 1

    def run():
        for test in args:
            nonlocal count
            print("~ test", count)
            count += 1

            if not test:
                print("[]")
                continue

            head = ListNode(test[0])
            current = head

            for i in range(1, len(test)):
                current.next = ListNode(test[i])
                current = current.next

            print_LL(head)
            solution = Solution()
            result = solution.reverse_list(head)
            print_LL(result)

    return run()


def print_LL(head):
    linked_list = []

    while head:
        linked_list.append(head.val)
        head = head.next

    print(linked_list)
        

test(test1, test2, test3)


## Approach 1: Iterative
############################
# time: O(n) - assume that n is the list's length
# space: O(1)

## Python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head    
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            
        return prev

## Java
# public ListNode reverseList(ListNode head) {
#     ListNode prev = null;
#     ListNode curr = head;
#     while (curr != null) {
#         ListNode nextTemp = curr.next;
#         curr.next = prev;
#         prev = curr;
#         curr = nextTemp;
#     }
#     return prev;
# }


## Approach 2: Recursive
############################
# time: O(n) - assume n is the list's length
# space: O(n) - extra space comes from implicit stack due to recursion.
#               recursion can go n levels deep.

## Python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return p


## Java
# public ListNode reverseList(ListNode head) {
#     ListNode prev = null;
#     ListNode curr = head;
#     while (curr != null) {
#         ListNode nextTemp = curr.next;
#         curr.next = prev;
#         prev = curr;
#         curr = nextTemp;
#     }
#     return prev;
# }
