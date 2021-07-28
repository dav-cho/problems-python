##
#### Remove Linked List Elements (easy)
###########################################

# Given the head of a linked list and an integer val, remove all the nodes
# of the linked list that has Node.val == val, and return the new head.

# Example 1:
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]

# Example 2:
# Input: head = [], val = 1
# Output: []

# Example 3:
# Input: head = [7,7,7,7], val = 7
# Output: []

# Constraints:
# The number of nodes in the list is in the range [0, 104].
# 1 <= Node.val <= 50
# 0 <= val <= 50

################################################################################

## Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


## sentinel / dummy node
############################
class Solution:
    def remove_elements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        
        prev, curr = dummy, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            
            curr = curr.next
            
        return dummy.next

## sentinel 2
#################
class Solution:
    def remove_elements(self, head: ListNode, val: int) -> ListNode:
        dummy = curr = ListNode(0)
        dummy.next  = head

        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next




## Tests
############

test1 = ([1, 2, 6, 3, 4, 5, 6], 6)  # [1, 2, 3, 4, 5]
test2 = ([], 1)                     # []
test3 = ([7, 7, 7, 7], 7)           # []


def test(*args):
    count = 1

    def run():
        for test in args:
            nonlocal count
            print("~ test", count)
            count += 1

            linked_list, val = test

            if not linked_list:
                print('[]')
                continue

            head = ListNode(linked_list[0])
            current = head

            for i in range(1, len(linked_list)):
                current.next = ListNode(linked_list[i])
                current = current.next

            print_LL(head)
            solution = Solution()
            result = solution.remove_elements(head, val)
            print_LL(result)

    return run()


def print_LL(head):
    linked_list = []

    while head:
        linked_list.append(head.val)
        head = head.next

    print(linked_list)
        

test(test1, test2, test3)


## LeetCode Solutions
#########################

## Approach 1: Sentinel Node
################################
# time: O(n) - it's a one pass solution
# space: O(1) - it's a constant space solution
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel = ListNode(0)
        sentinel.next = head
        
        prev, curr = sentinel, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return sentinel.next


